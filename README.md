# Valorant Experience Farm
*Designed, written and documented by David Liu*

### Table of Contents:
0. [User Notes](#0-user-notes)
1. [Overview](#1-overview)
2. [User Setup](#2-user-setup)
3. [User Operation](#3-user-operation-for-run-deathmatch-only)
4. [Problems and Questions](#4-problems-and-questions)
5. [Planned improvements](#5-planned-improvements)

***

## (0) User Notes
Hello. Welcome to my implementation of an experience farm for Valorant. I will briefly explain what you, the user, should be aware of before choosing to run this sort of program on your computer or account.

### (0.1) Intended usage 
As of 9/27/20, this program expects the following inputs and prerequisites:
- 1920 x 1080 resolution monitor (you can change your computer resolution on some monitors) 
- Windows 8 or 10 (better on Windows 10)
- Valorant installed
- Python installed

This bot is intended to used by anyone who plays Valorant. That said, this bot _performs best when a player is also active on the account_. The fastest ways to level up a battlepass are by playing games and by completing the daily and weekly missions. Though, theortically speaking, one could level through the entire battlepass with just the bot by running it for approximately 400 hours (~1,600,000 XP divided by 4,000 XP per hour).

It is recommended to use this bot when not actively needing to use the computer. I usually leave this bot running on my PC overnight.

### (0.2) Risk acknowledgement
I am not responsible for the possible ban or termination of an account for using this program. Riot (the developer) _likely_ does not condone this. Though, over three separate accounts, I have ran this bot for over 60 hours cumulatively (as of 9/27/20), and have not recieved any warning or ban. See (1.3) for possible reasons why I have not been banned. 

***

## (1) Overview 
Now I will cover the basics of what everything is for those who have not heard of or have not played Valorant before. Then I will cover what this program does explicitly.  

### (1.1) Valorant
Valorant is a free-to-play multiplayer tactical first-person shooter. Quickly summarized, there exists a **battlepass**, which is a 50-tier system designed to give rewards to those who gain enough **experience points**. Playing any game mode reaps experience points, or **XP**. One game mode, **deathmatch**, lasts for approximately 5-10 minutes. This is the only game mode that does not require a team, as it is a **free-for-all**, everyone fending for themselves. 

### (1.2) The program
This program comes in three parts. I will first explain the in-game part.

Obviously as a free-for-all, it will not hurt anyone if you do not contribute to the game. But as for most kinds of games, Valorant software can detect if you are **away from the keyboard**, or **AFK**. AFK  can be flagged if a player is not moving, shooting, etc. This usually means the player is doing other things and not actively playing. If you are flagged AFK, then you will not recieve XP for a game. To counter that, this program will do is move, shoot, and even buy guns for you. Thus, you are now AFK proof.

The second part is automating the process of starting games. This program will check to see if Valorant is currently in one of three states: **ready for a game, in queue,** or **in game**. If it is ready for a game, then go into the **queue**, which is essentially a waiting lobby for your turn to join a game. If it is not ready for a game, and also not in queue, then it is in game, and proceed to do AFK-proof movements. 

The third part is automating the log-in aspect of Valorant. (Though, I plan on separating this function from the actual XP bot.) This is extremely useful if you have multiple accounts. Users enter the account nickname, and the program will automatically do the rest for them by inputing all the credentials in and then opening Valorant. 

Note: For those who do not know, a **farm** is slang for any easy way to cultivate something. An **AFK XP farm** means an easy way to gain XP while being AFK.  

### (1.3) Features
As of 9/28/20, the following list are additional features of the program:

**Game Features**
- **Random** movement and shooting length of time. This likely helps prevent flagging of the bot, as it may deal some damage. 
- Buying random guns from armory.
- Smooth and random mouse movements and click area. 
- v1.1: Movement is a random combination of adjacent wasd keys (wa, sd, wd, etc.). 
- v1.1: Program checks for update after 6 minutes of being in game to reduce time wasted and have smoother movements. 

**User Features**
- Automatic status update if game state is changed.
- Status updates with key presses.
- Time updates with key presses.
- Summary statistics of XP, time, rounds played after program ends.
- Update how much lifetime XP made from program. 

### (1.4) Efficiency and storage
This program runs fairly efficiently, as the only significant time consumption is by choice with time.sleep(). The game state will update at most every 15 seconds to check what is happening. In addition, it reads in the credentials text file, and writes into the lifetime XP textfile. Some other things to note are that the folder _saved_Images_ contains all the necessary images to run the program (game state checking). 

***

## (2) User Setup
Now I will cover how to set up this program to run fluidly, and optimally. Assuming having read section (0.1), let's begin.

### (2.1) Download source code folder
In this GitHub repository main page, there is a green button to download the ZIP file of **VXPF**. Download it.
After downloading it, open it to reveal its contents. Move this folder to your **Desktop**. 

### (2.2) Fill in necessary files: For Open Valorant Only
Skip this section (2.3) if you do not intend to use the auto-login part of the program. 

In the credentials.txt, fill in your account information. Accounts are separated by lines. Alias, username, and password are separated by commas. Do not deviate from this format, nor have a comma in your password. For alias, you will choose the nickname for this account (it can just be the username too. I use 'david'.) 

Check everything is downloaded successfully. lifetime_XP.txt should just have the value 0 in it. In the saved_Images folder, there should be two images: the loginInterface.png, and playdefault.png. 

### (2.3) Install Python packages 
Open your terminal, or command line (on your computer, go to the search bar, and type in "command", and it should be a black box.) Now work within the terminal.

1. Type in and enter **py -V** to sure Python was installed successfully. If an error arises, download Python here: https://www.python.org/downloads/
2. Type in and enter **py -m pip install pyautogui keyboard**. This downloads the necessary Python packages to run. Wait for this to finish. 

### (2.4) Start program
Continue working in the terminal. 

1. Drag the terminal window and move it against the bottom left of your screen. 
2. Type and enter **cd Desktop\VXPF-1.1**.
3. Type and enter **py valorant_XP_Farm.py**.
4. It will prompt you what you would like to do. 1: Open Valorant, 2: Open Valorant and run the XP bot, 3: Run the XP bot, or 4: exit. Type in the number for what you want. 

A. Chose to open Valorant (1):
1. It will ask you for the alias associated with the account located in file. After entering a valid alias, it will load Valorant. _Do not move your mouse after countdown._

B. Chose to open and run (2):
1. Choose this only after knowing that doing the two operations separately (open and run) work properly. Read A and C for information.  

C. Chose to run XP bot (3):
1. Have Valorant logged in, open, at the home screen, and in window mode (not fullscreen). Press the 'F11' key to go from fullscreen to window (vice versa). <ins>This is crucial, and bot will not work if Valorant is in full screen.<ins> (will provide an IMAGE)
2. It will ask for how many hours you would like the bot to run. Preferably, do not put a number over 5.
3. It will then proceed to work in Valorant. _Do not move your mouse after countdown._
  
***
  
## (3) User Operation: For Run Deathmatch Only
This section (3) is only for running the XP bot, or the deathmatch program. 

I will go over the simple in-program user functions I implemented to help users understand what is going on. These work _after_ the countdown is done, so it can be called during queue and in game. 

Summary of keys: **'ESC', 'U', 'I'**

- 'ESC': Exit program: Hold the 'ESC' key (for at least 10 seconds) to leave the program. This will stop the bot in its tracks. So if your mouse moves where you do not want it to, just hold down the 'ESC' key and wait.
- 'U': Update game state: Hold the 'U' key to get a update on whether the game is still in queue or in game. Will also show local time.
- 'I': Time elapsed and left: Hold the 'I' key to get an update on how many minutes passed, and how many minutes are left to run. 

If there is any problem happening (queue not starting, error messages), try starting again from (2.4) step C. 

***

## (4) Problems and Questions
- Problem: I don't want my mouse to move anymore!
  - Solution: Hold 'ESC' key. You can also try quickly moving to the terminal and press control and C (CTRL + C).
- P: I get an error message in the terminal.
  - S: Check all the files exist from the instructions. You should not be getting any error if all the files exist.
- P: The deathmatch is not queueing.
  - S: Make sure all your windows are closed, except for the terminal and the Valorant windows. Sometimes, the code (image searching algorithm) can bug out. 
- P: I want to play this game of deathmatch instead of the bot.
  - S: Just hold the 'ESC' key. 

*** 

## (5) Planned Improvements 
I plan on continuing to work on this project to make it even more foolproof. Here are some ideas I plan on continuing:
- Moving the mouse 
- Constraining the maximum time in game
- Have AFK movement timing be more consistent
- Popping a button up instead of working in terminal

_Thanks for your time._
_This project is still in development._
