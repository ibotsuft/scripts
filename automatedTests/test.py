import sys
import threading
import subprocess
import signal
import pyautogui
import time
import os

class TestRunner:
    def __init__(self):
        self.iteration = 0
        self.process = None
        self.lock = threading.Lock()

    def killGame(self):
        with self.lock:
            if self.process:
                print('I believe the game is over. Killing process.')
                pgrp = os.getpgid(self.process.pid)
                try:
                    os.killpg(pgrp, signal.SIGINT)
                except Exception as e:
                    print(f"Error killing process: {e}")

    def startGame(self):
        with self.lock:
            if self.process:
                print('Game is already running. Skipping start.')
                return
            try:
                ourTeamName = f"iBots_Dev_{self.iteration}"
                theirTeamName = f"RoboCin_{self.iteration}"
                bash = ['bash', 'quickStartGame.sh', ourTeamName, theirTeamName]
                dir = '/home/kali/ibots/scripts/automatedTests/'
                self.process = subprocess.Popen(bash, preexec_fn=os.setsid, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir)
                self.process.communicate()
            except Exception as e:
                print(f"Error starting game: {e}")

    def runTests(self):
        with self.lock:
            self.iteration += 1

        thread = threading.Thread(target=self.startGame)
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
        self.killGame()
        thread.join()

if __name__ == "__main__":
    test_runner = TestRunner()

    while True:
        if test_runner.iteration == 15:
            print('End of execution')
            exit()
        print("Iteration:", test_runner.iteration)
        test_runner.runTests()
