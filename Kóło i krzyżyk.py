import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, root):
        # Глобальні змінні
        self.current_player = "X"
        self.player_choice = None  # "X" і "O" - вибір гравця

        # Players information
        self.players = {
            "X": "Player Bot",
            "O": "Player Human"
        }

        # Виграшні комбінації
        self.winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        # Порожні клітинки
        self.empty_cells = [(i, j) for i in range(3) for j in range(3)]

        # Створення кнопок
        self.buttons = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                              command=lambda i=i, j=j: self.button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        # Додайте кнопки вибору гравця
        player_x_button = tk.Button(root, text=self.players["X"], font=('normal', 16), width=10, height=2,
                                    command=lambda: self.set_player_choice("X"))
        player_O_button = tk.Button(root, text=self.players["O"], font=('normal', 16), width=10, height=2,
                                    command=lambda: self.set_player_choice("O"))
        player_x_button.grid(row=3, column=0)
        player_O_button.grid(row=3, column=1)

        reset_button = tk.Button(root, text="Reset", font=('normal', 20), width=10, height=2, command=self.reset_board)
        reset_button.grid(row=3, column=2)

    def check_winner(self):
        for combination in self.winning_combinations:
            if all(self.buttons[i][j]['text'] == self.current_player for i, j in combination):
                self.highlight_winner_buttons(combination)
                return True
        if not any("" in self.buttons[i][j]['text'] for i, j in self.empty_cells):
            messagebox.showinfo("premis", "Mecz zakończył się remisem!")
            self.reset_board()
            return True
        return False

    def highlight_winner_buttons(self, combination):
        for i, j in combination:
            self.buttons[i][j].config(bg="green")

    def button_click(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
            self.empty_cells.remove((row, col))
            if self.check_winner():
                messagebox.showinfo("Player " + self.current_player + " wygrany!", "Gratulacje!")
                self.reset_board()
            else:
                self.switch_players()

                # Якщо граєте проти ШІ, змусьте ШІ рухатися
                if self.player_choice == "X" and self.current_player == "O":
                    self.ai_make_move()

    def switch_players(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j]['bg'] = "white"
        self.current_player = "X"
        self.empty_cells = [(i, j) for i in range(3) for j in range(3)]

    def ai_make_move(self):
        # Простий ШІ: навмання виберіть порожню клітинку
        if self.empty_cells:
            ai_move = random.choice(self.empty_cells)
            self.buttons[ai_move[0]][ai_move[1]]['text'] = self.current_player
            self.empty_cells.remove(ai_move)
            if self.check_winner():
                messagebox.showinfo("Player " + self.current_player + " wygrany!", "Gratulacje!")
                self.reset_board()
            else:
                self.switch_players()

    def set_player_choice(self, choice):
        self.player_choice = choice

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()