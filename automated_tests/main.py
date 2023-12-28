import sys
import threading
import subprocess
import pyautogui
import signal
import time
import os

iteration = 0
process = None

def startGame():
    
    global process
    global iteration

    iteration = iteration + 1
        
    def killGame():
        print('I believe the game is over. Killing process.')
        pgrp = os.getpgid(process.pid)
        try:
            os.killpg(pgrp, signal.SIGINT)
        except Exception as e:
            return
        return
    
    def startGame():
        global process
        global iteration
        ourTeamName = f"iBots_Dev_{iteration}"
        theirTeamName = f"RoboCin_{iteration}"
        bash = ['bash', 'quickStartGame.sh', ourTeamName, theirTeamName]
        dir = '/home/kali/ibots/scripts/automatedTests/'
        process = subprocess.Popen(bash, preexec_fn=os.setsid, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir)
        process.communicate()

        return

    thread = threading.Thread(target=startGame)
    thread.start()

    time.sleep(3)
    print('Connecting now')
    pyautogui.hotkey('ctrl', 'c', interval=0.1)
    time.sleep(5)
    print('Starting now')
    pyautogui.hotkey('ctrl', 'k', interval=0.1)
    time.sleep(420)
    print('I believe the first half ended now. Starting again.')
    pyautogui.hotkey('ctrl', 'k', interval=0.1)
    time.sleep(450)
    killGame()
    thread.join()

while True:
    if iteration == 15:
        print('End of execution')
        exit()
    print("Iteration:", iteration)
    startGame()
    

