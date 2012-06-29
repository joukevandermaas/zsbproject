# Technical Details
Required materials:
- Computer with Python 2.7
- Nao robot (tested on a Nao with a 3.0 body and a 4.0 head)
- WiFi connection for both the computer and the Nao.

The scripts were not tested on the Nao itself, they were always ran remotely. The Naos tend to heat up quickly when running the script. The reaction is that the stiffness of the joints is lowered, causing the robot to fall. The script can only be run a couple of times before the Naos do this. Once it happens, it takes about thirty minutes for the Nao to reset the stiffness.

For the scripts used during development, a command line or terminal is required as they need arguments to run. The other files can be run from a command line as well as a gui.

# Files
All files were written by Jouke van der Maas, Wessel Klijnsma, Marysia Winkels and Koen Keune, unless specified otherwise. Even if the files were written by others, they were edited to fit in with the rest of the files.

## Required
- **kickmotions.py**
Defines the different moves the Nao needs to perform the kick.
- **robocupmotion.py**
Defines additional movements. This file was written by the Dutch Nao Team.
- **standup.py**
Makes the robot stand up when run. No arguments or other input is required.
- **dokick.py**
Performs all movements needed to do a kick. Run right after standup.py. You will be prompted to give the robot the ball.
- **config.py**
Defines configuration options to make the other scripts simpler. The ip-address of the Nao is read from here and used by all other scripts (including robocupmotion.py). This file was written by Aldabaran.

## Used during development
- **record.py**
Records the angles of the joints of the Nao when the user presses <enter>. The script requires the name of the joint or joint group to record as a command-line argument. It writes a text file with the name of that joint to a folder called 'data'.
- **setstiffness.py**
Sets the stiffness of a joint or joint group. Useful when testing or recording using record.py, to move certain limbs around. It requires two command line arguments: the joint or joint group to set and the stiffness (from 0.0 to 1.0) to give it.

# Use Guide
Once the network has been set up, ask the Nao for each IP adress. Edit the file config.py to enter it. You can test the connection to the Nao using **setstiffness.py** or any other harmless script.

Before doing the kick, make sure the Nao is standing up. If this is not the case, run **standup.py**. Once the robot is standing, run **dokick.py** to raise the robot's arms. The script will ask you to press enter once the ball is in the robot's arms. Once you do, the kick will be performed.

There is no way to reset the robot's position from the end of the kick. If necessary, put the robot down manually and call **standup.py**. The Nao can only perform the kick a few times before it becomes too hot and lowers it stiffness.