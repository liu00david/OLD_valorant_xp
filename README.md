# Valorant Experience Farm
*Designed by David Liu*

### Table of Contents:
0. User Notes
1. Overview
2. Functionality
3. User Setup 
4. User Operation 
5. Planned improvements

***

## (0) User Notes
Hello. Welcome to my implementation of an experience farm for Valorant. I will briefly explain what you, the user, should be aware of before choosing to run this sort of program on your computer or account.

### (0.1) Intended usage 
As of 9/27/20, this program expects the following inputs and prerequisites:
- 1920x1080 resolution monitor 
- Windows 8 or 10
- Valorant installed
- Python installed

This bot is intended to used by anyone who plays Valorant. That said, this bot _performs best when a player is also active on the account_. The fastest ways to level up a battlepass are by playing games and by completing the daily and weekly missions. Though theortically speaking, one could level through the entire battlepass with just the bot by running it for approximately 400 hours (~1,600,000 XP divided by 4,000 XP per hour).

### (0.2) Risk acknowledgement
I am not responsible for the possible ban or termination of an account for using this program. Riot (the developer) _likely_ does not condone this. Though, over three separate accounts, I have ran this bot for over 40 hours cumulatively (as of 9/27/20), and have not recieved any warning or ban. See (1.3) for possible reasons why I have not been banned. 

***

## (1) Overview 
Now I will cover the basics of what everything is for those who have not heard of or have not played Valorant before. Then I will cover what this program does explicitly.  

### (1.1) Valorant
Valorant is a free-to-play multiplayer tactical first-person shooter. Quickly summarized, there exists a **battlepass**, which is a 50-tier system designed to give rewards to those who gain enough **experience points**. To Playing any game mode reaps experience points **XP**. One game mode is called **deathmatch**. Deathmatch games last for approximately 5-10 minutes. This is the only game mode that does not require a team, as it is a **free-for-all**, everyone fending for themselves. 

## (1.2) The Program
This program comes in three parts. I will first explain the in-game part.

Obviously as a free-for-all, it will not hurt anyone if you do not contribute to the game. But as for most kinds of games, Valorant software can detect if you are **away from the keyboard**, or **AFK**. Being AFK means not moving, shooting, etc. If you are flagged AFK, then you will not recieve XP for a game. To counter that, this program will do is move, shoot, and even buy guns for you. Thus, you are now AFK proof.

The second part is automating the process of starting games. This program will check to see if Valorant is currently in one of three states: **ready for a game, in queue,** or **in game**. If it is ready for a game, then go into the **queue**, which is essentially a waiting lobby for your turn to join a game. If it is not ready for a game, and also not in queue, then it is in game, and proceed to do AFK-proof movements. 

The third part is automating the log-in aspect of Valorant. (Though, I plan on separating this function from the actual XP bot.) This is extremely useful if you have multiple accounts. Users enter the account nickname, and the program will automatically do the rest for them by inputing all the credentials in and then opening Valorant. 

## (1.3) Features
As of 9/27/20, the following list are additional features of the program:
**Game Features**
- **Random** movement direction and length of time
- Buying random guns
- Smooth and random mouse movements
**User Features**
- Status updates
- Time updates
- Summary statistics of XP, time, rounds played
- Keeps track of how lifetime XP made from program

# (2) Setup

# (3) Operation

# (4) Future work 
moving mouse, constraining time in game, guns 


I created this program to make progressing through the battlepass faster. 
limit time 
This project is still in development, and supports 
