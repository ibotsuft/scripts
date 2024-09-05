import sys
import threading
import subprocess
import pyautogui
import signal
import time
import os

iteration = 0
process = None

# Função para ignorar o sinal de interrupção temporariamente
def ignore_signal(sig, frame):
    print("Ignoring signal")

def startGame():
    global process
    global iteration

    iteration = iteration + 1
        
    def killGame():
        if process is not None:
            print('I believe the game is over. Killing process.')
            pgrp = os.getpgid(process.pid)
            try:
                os.killpg(pgrp, signal.SIGINT)
                process.wait()  # Aguarda o término completo do processo
            except Exception as e:
                print(f"Error killing process: {e}")
            finally:
                process.terminate()  # Garante a finalização do processo
        return
    
    def startGameProcess():
        global process
        global iteration
        ourTeamName = f"iBots_Dev_{iteration}"
        theirTeamName = f"HeliosBase_{iteration}"
        bash = ['bash', 'quickStartGame.sh', ourTeamName, theirTeamName]
        dir = '/home/kali/ibots/scripts/automated_tests/'
        process = subprocess.Popen(bash, preexec_fn=os.setsid, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir)
        process.communicate()

        return

    # Start the game in a separate thread
    thread = threading.Thread(target=startGameProcess)
    thread.start()

    try:
        # Aumenta o tempo de espera para garantir que o jogo está pronto para receber o atalho
        time.sleep(10)  # Aumentei o tempo de espera para 10 segundos
        print('Connecting now')

        # Temporarily ignore Ctrl+C (SIGINT)
        original_handler = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGINT, ignore_signal)

        pyautogui.hotkey('ctrl', 'c', interval=0.1)

        # Restore original handler
        signal.signal(signal.SIGINT, original_handler)

        time.sleep(5)
        print('Starting now')
        pyautogui.hotkey('ctrl', 'k', interval=0.1)
        time.sleep(420)
        print('I believe the first half ended now. Starting again.')
        pyautogui.hotkey('ctrl', 'k', interval=0.1)
        time.sleep(450)

    except KeyboardInterrupt:
        print('Game interrupted by user.')
        killGame()

    killGame()
    thread.join()

try:
    while True:
        if iteration == 2:
            print('End of execution')
            exit()
        print("Iteration:", iteration)
        startGame()

except KeyboardInterrupt:
    print("Execution interrupted by user. Exiting gracefully...")
    if process:
        killGame()
