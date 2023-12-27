import subprocess
import threading
import time
import pyautogui

class GameAutomator:
    def __init__(self):
        self.num_games = 5  # Número de jogos que você deseja executar simultaneamente
        self.num_iterations = 20  # Número de iterações desejadas
        self.games = []

    def start_game(self, game_id):
        for iteration in range(self.num_iterations):
            print(f"Starting game {game_id}, iteration {iteration + 1}")
            # Adicione a lógica específica para iniciar o jogo aqui
            # Certifique-se de iniciar o servidor, o monitor e as equipes conforme necessário

            time.sleep(3)
            print(f'Connecting to game {game_id} now')
            pyautogui.hotkey('ctrl', 'c', interval=0.1)
            time.sleep(5)
            print(f'Starting game {game_id} now')
            pyautogui.hotkey('ctrl', 'k', interval=0.1)
            time.sleep(420)
            print(f'I believe the first half of game {game_id} ended now. Starting again.')
            pyautogui.hotkey('ctrl', 'k', interval=0.1)
            time.sleep(450)

    def run_game(self, game_id):
        while True:
            self.start_game(game_id)

    def run_game_loop(self):
        for game_id in range(self.num_games):
            command = ["sh", "quickStartGame.sh"]  # Substitua isso pelo comando correto para executar o seu script shell
            game_thread = threading.Thread(target=self.run_game, name=str(game_id), args=(command,))
            self.games.append(game_thread)
            game_thread.start()

        for game_thread in self.games:
            game_thread.join()

if __name__ == "__main__":
    game_automator = GameAutomator()
    game_automator.run_game_loop()
