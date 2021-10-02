# NewWorldQueue

This program is targeted toward people with no coding experience since anyone with it would have written this 3 days ago. I purposefully ignore any pep-standards in order to make the code more readable for people who lack programming experience. 

In order to make this program work as desired a few steps need to be completed by the user. Installing Python, pip and pyautogui. The first step is to check if these programs are already installed on your computer. To do this you simply search for the **command prompt** in your Windows search bar and run it as **administrator**. Once you are inside the command prompt, i.e. a black window where you can write things. Input the following followed by pressing **enter** after typing it:

>python --version

If you receive a version number for python it is installed. If that version number is lower than 3 I would recommend you install a later version of python. Instructions on how to do this can be found [here](https://phoenixnap.com/kb/how-to-install-python-3-windows).

After installing python (if necessary) run the previous command to make sure everything worked. You may have to run

>python3 --version

to see the version number of your newer installation.

Now we have to install pip, first check if it exist with the commands:

>pip --version 
>pip3 --version

If either of those 2 commands work you do not have to install pip. Otherwise a guide to do so might be found [here](https://phoenixnap.com/kb/install-pip-windows). Once pip is installed and working you want to run the following commands.

>pip install pyautogui
>pip3 install pyautogui

If the first command works and installs the package you do not have to use the second command. After this all you need to do is download the file **NewWorld.py** from this repository in any way you see fit. After this you will want to go in to that file, using the normal notepad works fine. In there you will want to change the variables listed, for example screen resolution to your own and time until you join the queue. The time until joining the queue starts when you run the program. To run the program you will want to save the file with your own settings and preferably have it saved on your desktop. You then want to navigate to your desktop in the **command prompt** window. [Read more here](https://www.quora.com/How-do-I-navigate-to-a-desktop-in-CMD). 

When you are ready to start the countdown until you join queue you simply have to run the command:

>python3 NewWorld.py

If there are any errors when trying to run this program make sure the earlier steps are completed or send me an email at *adamengman1@gmail.com* and will try to assist you.

After this you should lose your cursor in the command prompt and a information message should appear. Do not close the command prompt. Now you can start up New World and navigate until you reach the screen with the **PLAY** button that enters you in to a queue. Now you can turn off your monitor and go to bed and tommorow morning the computer will press play at the time you set, placing you in the queue.

If you accidentally started the program or want to change the time, press **ctrl-z** when in the command prompt and the program should terminate.

Notes: I chose not to create this program as an executable with a simple GUI simply because Windows antivirus and defender would go crazy and no one would dare to download and start that file, and rightly so. 
