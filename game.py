import tkinter as tk
from tkinter import messagebox
import random
from tkinter import font

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ADVENTURE GAME")
        self.create_widgets()
        self.player_name = ""
        self.score = 0
        self.inventory = []
        self.position = 0
        self.game_over = False
        self.setup_game()

    def setup_game(self):
        self.update_text("Welcome to the Adventure Game!\n")
        self.create_name_entry()
        self.update_text("\nLet's begin the adventure.")
        self.update_ui()

    def create_name_entry(self):
        self.name_label = tk.Label(self.root, text="Enter your name",font='ariel, 12 bold')
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.name_entry.bind('<Return>', self.set_player_name)

    def set_player_name(self, event):
        self.player_name = self.name_entry.get().strip()
        if self.player_name:
            self.name_label.destroy()
            self.name_entry.destroy()
            self.update_text(f"Hello, {self.player_name}!\n")
        else:
            self.update_text("Please enter a valid name.")

    def create_widgets(self):
        self.label = tk.Label(self.root, text="ADVENTURE GAME",font='ariel, 20 bold', width=90, bd=5, bg='#b19cd9' ,fg='BLACK')
        self.label.pack()

        self.text_font = font.nametofont("TkDefaultFont")
        self.text_font.configure(weight="bold")

        self.text_box = tk.Text(self.root, height=40, width=100, state=tk.DISABLED)
        self.text_box.config(font=self.text_font)
        self.text_box.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.button_forward = tk.Button(self.button_frame, text="Go Forward", command=self.go_forward, bg="green", fg="white")
        self.button_forward.pack(side=tk.LEFT)

        self.button_backward = tk.Button(self.button_frame, text="Go Backward", command=self.go_backward, bg="blue", fg="white")
        self.button_backward.pack(side=tk.LEFT)

        self.button_left = tk.Button(self.button_frame, text="Go Left", command=self.go_left, bg="orange", fg="white")
        self.button_left.pack(side=tk.LEFT)

        self.button_right = tk.Button(self.button_frame, text="Go Right", command=self.go_right, bg="red", fg="white")
        self.button_right.pack(side=tk.LEFT)

        self.button_inventory = tk.Button(self.button_frame, text="View Inventory", command=self.view_inventory, bg="purple", fg="white")
        self.button_inventory.pack(side=tk.LEFT)

        self.button_quit = tk.Button(self.root, text="Quit", command=self.quit_game, bg="gray", fg="white")
        self.button_quit.pack()

    def update_text(self, message):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, message + "\n")
        self.text_box.see(tk.END)
        self.text_box.config(state=tk.DISABLED)

    def go_forward(self):
        self.score += 5
        self.position += 1
        self.check_location()

    def go_backward(self):
        self.score += 5
        self.position -= 1
        self.check_location()

    def go_left(self):
        self.score += 10
        item = random.choice(["Health Potion", "Shield", "Gold"])
        self.inventory.append(item)
        self.update_text(f"You went left and found a {item}!")

    def go_right(self):
        if random.choice([True, False]):
            self.score += 20
            item = random.choice(["Sword", "Shield", "Diamond"])
            self.inventory.append(item)
            self.update_text(f"You went right and defeated a dragon! You found a {item}.")
        else:
            self.update_text("You went right and encountered a dragon. The dragon defeated you. Game over!")
            self.game_over = True

    def quit_game(self):
        self.update_text("Thanks for playing!")
        self.root.destroy()

    def view_inventory(self):
        if self.inventory:
            self.update_text(f"Inventory: {', '.join(self.inventory)}")
        else:
            self.update_text("Your inventory is empty.")

    def check_location(self):
        if self.position == 0:
            self.update_text("You are at the starting point.")
        elif self.position == 1:
            self.update_text("You moved forward and reached a new location.")
        elif self.position == -1:
            self.update_text("You moved backward and returned to the starting point.")
        else:
            self.update_text("You reached an unknown location.")

    def update_ui(self):
        self.button_forward.config(state="normal" if not self.game_over else "disabled")
        self.button_backward.config(state="normal" if not self.game_over else "disabled")
        self.button_left.config(state="normal" if not self.game_over else "disabled")
        self.button_right.config(state="normal" if not self.game_over else "disabled")
        self.button_inventory.config(state="normal" if not self.game_over else "disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()
