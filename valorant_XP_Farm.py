# This is the public version. 
import pyautogui
import time
import sys
import random
import math
import keyboard

################################################################################
# DICTIONARIES
#------------------------------------------------------------------------------#
# All locations for clicking (x,y)
# Locations are center coordinates

# open_Valorant
loc_Dict = {}
loc_Dict["toolbar"] =       (114,1061)
loc_Dict["valorantApp"] =   (102,510)
loc_Dict["loginInterface"]= (719,523)
loc_Dict["username"] =      (399,402)
loc_Dict["password"] =      (393,465)
loc_Dict["login"] =         (516,659)

# run_Deathmatch
loc_Dict["playA"] =         (859,111)       #(934,21)
loc_Dict["playB"] =         (865,111)
loc_Dict["queueA"] =        (859,112)       #(849,25)
loc_Dict["queueB"] =        (989,110)
loc_Dict["deathmatch"] =    (1076,175)      #(1100,103)
loc_Dict["start"] =         (924,908)       #(932,984)
# run_Deathmatch: in game mode
loc_Dict["weapons"] =       (924,536)       #(920,300)
loc_Dict["weaponsX"] =      (1689,160)      #(1858,53)

#------------------------------------------------------------------------------#
# Make a dictionary of locations' (x,y) error, or distance from center
# Essentially creating a box area to click within

# open_Valorant
loc_Error_Dict = {}
loc_Error_Dict["toolbar"] =         (1,1)
loc_Error_Dict["valorantApp"] =     (1,1)
loc_Error_Dict["loginInterface"]=   (50,15)
loc_Error_Dict["username"] =        (1,1)
loc_Error_Dict["password"] =        (1,1)
loc_Error_Dict["login"] =           (1,1)

# run_Deathmatch
loc_Error_Dict["playA"] =           (5,7)
loc_Error_Dict["playB"] =           (7,5)
loc_Error_Dict["queueA"] =          (7,5)
loc_Error_Dict["queueB"] =          (5,7)
loc_Error_Dict["deathmatch"] =      (30,5)
loc_Error_Dict["start"] =           (50,25)
# run_Deathmatch: in game mode
loc_Error_Dict["weapons"] =         (329,191)
loc_Error_Dict["weaponsX"] =        (3,3)

#------------------------------------------------------------------------------#
# Make a dictionary of all login information

def load_Credentials(filename):
    credentials_Dict = {}
    try:
        with open(filename) as fh:
            line_Num = 0
            for line in fh:
                try:
                    (alias,username,password) = line.split(',')
                    credentials_Dict[alias] = (username,password[:-1])
                except:
                    print("Invalid line at line " + str(line_Num))
                    continue
                line_Num += 1
        fh.close()
    except:
        print("Error: file not found or cannot be opened.")
    return credentials_Dict

credentials_Dict = load_Credentials("credentials.txt")

#------------------------------------------------------------------------------#
# Loads lifetime xp from file. Updates global param.
def load_Lifetime_XP():
    global lifetime_XP
    try:
        with open("lifetime_XP.txt","r") as fh:
            for line in fh:
                pass
            last_Line = str(line)
            lifetime_XP = int(last_Line)
        fh.close()
    except:
        print("Invalid input file or corrupted numbers.")
    return

# Writes or appends lifetime xp to file. Takes global variables rounds played and lifetime xp
def write_Lifetime_XP():
    global rounds_Played, lifetime_XP
    try:
        with open("lifetime_XP.txt","a+") as fh:
            for line in fh:
                pass
            fh.write("\n" + str(rounds_Played*500 + lifetime_XP))
        fh.close()
    except:
        print("Invalid input file or corrupted numbers.")
    return

################################################################################
# GLOBAL VARS

# open_State: keeps track of state of opening Valorant:
#   -1: Not initialized
#    0: Ready to start
#    1: Opened Valorant app, waiting for login interface
#    2: Loaded Valorant login interface
#    3: Inputed Credentials and logged in
open_State = -1

# rounds_Played: keeps track of how many rounds played
rounds_Played = -1

# game_State: keeps track of state of Valorant:
#   -1: Not initialized
#    0: Initialized, ready to queue. Play button seen.
#    1: Waiting in queue. Queue button seen.
#    2: In a game. Neither play nor queue button seen.
game_State = -1

# game_State_Prev
game_State_Prev = -1

# start_Time_Deathmatch
start_Time_Deathmatch = -1

lifetime_XP = -1

################################################################################
# MAIN FUNCTIONS

#------------------------------------------------------------------------------#
# Open Valorant
# PARAM: N/A; RETURN: N/A
def open_Valorant():
    global open_State
    # Ask for what account: open_State set to 0.
    user = enter_Alias()

    # Preparation time.
    prep_Time(5)

    # Load Valorant valorant app: open_State set to 1.
    load_Valorant_App()

    # Log in with credentials: open_State set to 2, then 3.
    input_Credentials(user)

    print("Logged in and opened Valorant. Exiting program.")

    return

#------------------------------------------------------------------------------#
# Run deathmatch
# PARAM: hours to run; RETURN: N/A

def run_Deathmatch(runtime_Hours):
    global game_State, game_State_Prev, rounds_Played, start_Time_Deathmatch
    # Initialize game_State.
    game_State = 0

    # Preparation time.
    prep_Time(5)

    # Record time of start.
    start_Time_Deathmatch = time.time()
    # Duration to run turned to seconds.
    time_To_Run = 60*60*runtime_Hours

    # Take screenshot captures of play button. This will be the default.
    capture_Save("playA")
    capture_Save("playB")

    # While time is not up, loop.
    while time.time() - start_Time_Deathmatch < time_To_Run:
        # Let ESC key be exit button.
        if keyboard.is_pressed('\x1b'):
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            load_Lifetime_XP()
            write_Lifetime_XP()
            print("Exit key pressed. Quitting program.")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            exit()
        # Let 'u' key be update key. make game_State_Prev = -1 to trigger status update
        elif keyboard.is_pressed('u'):
            game_State_Prev = -1
        # Let 'i' key be time check key.
        elif keyboard.is_pressed('i'):
            time_Elapsed = math.floor((time.time() - start_Time_Deathmatch)/60)
            time_Left = math.floor(time_To_Run/60 - time_Elapsed)
            print("\n------------------------------------------")
            print("Time elapsed (minutes): ", time_Elapsed, "\nTime left (minutes): ", time_Left)

        # Update game state.
        update_Game_State()

        # If prev and curr game states changed, print new status
        if game_State_Prev != game_State:
            print("\n------------------------------------------")
            if game_State == 0:
                # Increment rounds played. (if new, -1 -> 0)
                rounds_Played += 1
                print("Status: Go in queue.")
            elif game_State == 1:
                print("Status: Waiting in queue.")
            elif game_State == 2:
                print("Status: In game.")
            else:
                print("ERROR: game mode = -1")
                exit()
            # Print the current xp, time
            xp_Current()
            local_Time = time.ctime()
            print("Local time:", local_Time)
        game_State_Prev = game_State

        # Action according to game state.
        if game_State == 0:
            # Ready to queue.
            go_Queue()
        elif game_State == 1:
            # Waiting in queue.
            wait_In_Queue()
        elif game_State == 2:
            # In game.
            AFK_Movement()
        else:
            print("ERROR: game mode = -1")
            exit()

    # Find how many minutes passed, and XP per hour.
    deathmatch_Summary()
    return


################################################################################
# HELPER FUNCTIONS

#------------------------------------------------------------------------------#
# UNIVERSAL HELPERS------------------------------------------------------------#
#------------------------------------------------------------------------------#
# prep_Time prints a timer of len number of seconds
# PARAM: length of time, RETURN: N/A
def prep_Time(len):
    print("Do not move mouse.")
    while len >= 0:
        print("Start in "+ str(len) + " seconds...")
        time.sleep(1)
        len -= 1
    return

#------------------------------------------------------------------------------#
# uniform_Location: outputs random tuple coordinate to click
# PARAM: location key in dictionary, RETURN: location tuple
def uniform_Location(dict_Key):
    if dict_Key not in loc_Dict or dict_Key not in loc_Error_Dict:
        print("ERROR: " + dict_Key + " not found. Did you include this location in the dictionary?")
        exit()
    return (random.uniform(loc_Dict[dict_Key][0]-loc_Error_Dict[dict_Key][0],
                            loc_Dict[dict_Key][0]+loc_Error_Dict[dict_Key][0]),
            random.uniform(loc_Dict[dict_Key][1]-loc_Error_Dict[dict_Key][1],
                            loc_Dict[dict_Key][1]+loc_Error_Dict[dict_Key][1]))

# smooth_Click: combines uniform_Location with movement and click
# PARAM: location key in dictionary, RETURN: N/A
def smooth_Click(dict_Key):
    pyautogui.moveTo(uniform_Location(dict_Key),duration=random.uniform(0.3,0.7))
    pyautogui.click()
    return

#------------------------------------------------------------------------------#
# Given key, return screenshot value
# PARAM: dictionary key; RETURN: screenshot value
def screenshot_Location(dict_Key):
    if dict_Key not in loc_Dict or dict_Key not in loc_Error_Dict:
        exit()
    left = loc_Dict[dict_Key][0]-loc_Error_Dict[dict_Key][0]
    top = loc_Dict[dict_Key][1]-loc_Error_Dict[dict_Key][1]
    width = 2 * loc_Error_Dict[dict_Key][0]
    height = 2 * loc_Error_Dict[dict_Key][1]
    return pyautogui.screenshot(region=(left,top,width,height))

# capture_Save: takes picture of the location of key, saves it
# PARAM: dictionary key; RETURN: N/A
def capture_Save(dict_Key):
    image_Saved = screenshot_Location(dict_Key)
    image_Saved.save(dict_Key + ".png")
    return

#------------------------------------------------------------------------------#
# OPENING HELPERS--------------------------------------------------------------#
#------------------------------------------------------------------------------#
# enter_Alias: Prompts and asks for login alias.
# open_State -1 -> 0
# PARAM: N/A, RETURN: user alias
def enter_Alias():
    global open_State
    user = str(input("Enter alias (press enter if signed in): \n")).lower()
    while user not in credentials_Dict and user != "" and user != "quit":
        user = str(input("Account not found. Try again. (press enter if signed in, or 'quit' to quit): \n"))
    if user == "quit":
        print("Quitting.")
        exit()

    open_State = 0
    return user

#------------------------------------------------------------------------------#
# load_Valorant_App: toolbar, types in, clicks app.
# open_State 0 -> 1
# PARAM: N/A, RETURN: N/A
def load_Valorant_App():
    global open_State
    # Open toolbar
    smooth_Click("toolbar")
    time.sleep(1)
    # Type in Valorant
    pyautogui.typewrite("VALORANT")
    time.sleep(1)
    # Click on Valorant to run
    smooth_Click("valorantApp")

    open_State = 1
    return

#------------------------------------------------------------------------------#
# input_Credentials: Types in username, password, then click log in
# open_State 1 -> 3
# PARAM: alias, RETURN: N/A
def input_Credentials(user):
    global open_State
    # If no input, then just return.
    if user == "":
        # open_State 1 -> 3
        open_State = 3
        return
    time.sleep(2)
    # wait for the login interface to open. Look for pre-saved an image of it.
    # if image can't be found, then just wait 20 seconds. Then take picture.
    try:
        while pyautogui.locateOnScreen('loginInterface.png') == None:
            print("Status: Waiting for login interface...")
            time.sleep(2)
    except:
        print("loginInterface.png not found. Waiting 20 seconds to open.")
        prep_Time(20)
        # Take an image of the loginInterface.
        capture_Save("loginInterface")

    # Now loaded interface. open_State 1 -> 2
    open_State = 2

    # Begin inputing credentials.
    time.sleep(0.5)
    smooth_Click("username")
    time.sleep(0.5)
    pyautogui.typewrite(credentials_Dict[user][0])
    time.sleep(0.5)
    smooth_Click("password")
    time.sleep(0.5)
    pyautogui.typewrite(credentials_Dict[user][1])
    # Seems like Riot detects logins that are too fast. Sleep (2) seconds.
    time.sleep(1)
    smooth_Click("login")

    # Now loaded interface. open_State 2 -> 3
    open_State = 3
    return


#------------------------------------------------------------------------------#
# DEATHMATCH HELPERS-----------------------------------------------------------#
#------------------------------------------------------------------------------#
# runtime_Hours_Input: Prompt ask how many hours to run
# PARAM: N/A; RETURN: runtime hours int
def runtime_Hours_Input():
    runtime_Hours = input("How many hours would you like this to run?\n")
    while True:
        try:
            runtime_Hours = float(runtime_Hours)
            break
        except:
            runtime_Hours = input("Invalid input. How many hours would you like this to run?\n")
    return runtime_Hours

#------------------------------------------------------------------------------#
# xp_Current: Prints the amount of XP so far
# PARAM: N/A; RETURN: N/A
def xp_Current():
    global rounds_Played
    # To cover -1 case. Only happens once.
    if rounds_Played < 0:
        print("Games played: " + str(rounds_Played+1) + "\t\tXP: " + str((rounds_Played+1) * 500))
    else:
        print("Games played: " + str(rounds_Played) + "\t\tXP: " + str(rounds_Played * 500))
    return

#------------------------------------------------------------------------------#
# update_Game_State: Updates game state by checking play, queue buttons
# PARAM: N/A; RETURN: N/A
def update_Game_State():
    global rounds_Played, game_State
    # If play button is seen, then game state is 0.
    if (pyautogui.locateOnScreen('playA.png') != None) or (pyautogui.locateOnScreen('playB.png') != None):
        game_State = 0
    # If queue button is seen, then game state is 1.
    elif (pyautogui.locateOnScreen('queueA.png') != None) or (pyautogui.locateOnScreen('queueB.png') != None):
        game_State = 1
    # If neither is seen, then game state is 2.
    else:
        game_State = 2
    return

#------------------------------------------------------------------------------#
# go_Queue(): Goes from play to queue.
# PARAM: N/A; RETURN: N/A
def go_Queue():
    # Home page -> Play page
    smooth_Click("playA")
    time.sleep(0.5)
    # Play page -> Deathmatch
    smooth_Click("deathmatch")
    time.sleep(0.5)
    # Deathmatch -> Start queue
    smooth_Click("start")
    time.sleep(0.5)
    print("Status: Begun queue")

    # Sleep to make sure queue button is updated for what we expect.
    time.sleep(3)
    # Take screenshot of how queue button looks
    capture_Save("queueA")
    capture_Save("queueB")

    # Wait a bit.
    time.sleep(2)
    return

#------------------------------------------------------------------------------#
# wait_In_Queue: waits in queue by time.sleep.
def wait_In_Queue():
    # In queue. Wait 5 seconds, then try again.
    time.sleep(5)
    return

#------------------------------------------------------------------------------#
# AFK_Movement: in game, so do AFK functions
def AFK_Movement():
    # Begin AFK functions
    AFK_time = random.uniform(1,3.5)
    action = random.choice(["buy","fire","move","moveNfire","nothing"])
    time_Start = time.time()
    while time.time() - time_Start <= AFK_time:
        if action == "buy":
            # b for armory
            pyautogui.press("b")
            time.sleep(0.2)
            # move to weapon wanted
            pyautogui.moveTo(uniform_Location("weapons"),duration=random.uniform(0.3,0.4))
            pyautogui.click()
            time.sleep(0.2)
            # move to exit
            pyautogui.moveTo(uniform_Location("weaponsX"),duration=random.uniform(0.3,0.4))
            pyautogui.click()
            move_And_Fire(AFK_time)

        elif action == "fire":
            # drag randomly left or right for left click
            fire_Weapon(AFK_time)

        elif action == "move":
            # hold one or two keys down
            hold_Key(AFK_time)

        elif action == "moveNfire":
            move_And_Fire(AFK_time)

        else:
            # I removed nothing
            move_And_Fire(AFK_time)
    return

#------------------------------------------------------------------------------#
# Auto holding key
def hold_Key(hold_time):
    key1, key2 = "w", random.choice(["w","a","d"])
    time_Start = time.time()
    while(time.time() - time_Start < hold_time):
        pyautogui.keyDown(key1)
        pyautogui.keyDown(key2)
    pyautogui.keyUp(key1)
    pyautogui.keyUp(key2)
    return

# Auto firing key
def fire_Weapon(hold_time):
    time_Start = time.time()
    while(time.time() - time_Start < hold_time):
        pyautogui.click()
        time.sleep(random.uniform(0.02,0.1))

# Move and Fire
def move_And_Fire(hold_time):
    key1, key2 = "w", random.choice(["w","a","d"])
    time_Start = time.time()
    while(time.time() - time_Start < hold_time):
        pyautogui.keyDown(key1)
        pyautogui.keyDown(key2)
        fire_Weapon(hold_time)
    pyautogui.keyUp(key1)
    pyautogui.keyUp(key2)
    return

#------------------------------------------------------------------------------#
# deathmatch_Summary: summarizes time, xp, xpPH
# PARAM: N/A; RETURN: N/A
def deathmatch_Summary():
    global start_Time_Deathmatch, rounds_Played
    # Load lifetime XP. Will update global var from last line of textfile.
    load_Lifetime_XP()
    # Write into the file. Will not update the lifetime xp var.
    write_Lifetime_XP()

    minutes_Operation = math.floor((time.time()-start_Time_Deathmatch)/60)
    xp_PH = math.floor((rounds_Played * 500) / (minutes_Operation / 60))

    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Finished deathmatch. \nTime elapsed (minutes): ", minutes_Operation)
    xp_Current()
    print("XP per hour: ", xp_PH, "\tLifetime XP: ", (rounds_Played*500 + lifetime_XP))
    print("Quitting program.")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return

################################################################################
# BEGIN INTERACTIVE
#------------------------------------------------------------------------------#
# Introduction
def introduction():

    choices_String = "What would you like to do? (enter number): \n\
        1: Open Valorant \n\
        2: Open Valorant, run Deathmatch \n\
        3: Run Deathmatch \n\
        4: Quit \n"

    # Take in selection number
    selection = str(input("Welcome. " + choices_String))

    while selection not in ["1","2","3","4"]:
        selection = str(input("Invalid input. " + choices_String))

    # 1: Open
    if selection == "1":
        open_Valorant()
    # 2: Open and Run
    elif selection == "2":
        # Prompt num of hours.
        runtime_Hours = runtime_Hours_Input()
        # Start. Open Valorant first
        open_Valorant()
        print("Status: Loading game.")
        time.sleep(15)

        # Time just in case it never loads
        timer_Temp = 0
        # Check if play button exists
        while pyautogui.locateOnScreen('playdefault.png') == None:
            if timer_Temp >= 60:
                print("Error: Load timeout")
                exit()
            print("Status: Waiting for game to load.")
            timer_Temp += 3
            time.sleep(3)
        print("Status: Game loaded. Begin running deathmatch.")

        run_Deathmatch(runtime_Hours)
    # 3: Run
    elif selection == "3":
        runtime_Hours = runtime_Hours_Input()
        run_Deathmatch(runtime_Hours)
    # 4: Quit
    else:
        print("Quitting program.")
        exit()

# START
introduction()



















#
