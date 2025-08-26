import tkinter as tk
import random

class CoinWeighingGame:
    def __init__(self, master):
        self.master = master
        master.title("12-Coin Weighing Puzzle")

        # Initialize coins: 12 normal, 1 odd
        self.coins = ["Coin " + str(i+1) for i in range(12)]
        self.odd_coin = random.randint(0, 11)
        self.is_heavier = random.choice([True, False])  # odd coin can be heavy or light

        self.weigh_count = 0

        # UI Elements
        self.info_label = tk.Label(master, text="Select coins to place on Left and Right pans.")
        self.info_label.pack()

        self.left_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE, exportselection=False)
        self.right_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE, exportselection=False)

        for coin in self.coins:
            self.left_listbox.insert(tk.END, coin)
            self.right_listbox.insert(tk.END, coin)

        tk.Label(master, text="Left Pan").pack()
        self.left_listbox.pack()

        tk.Label(master, text="Right Pan").pack()
        self.right_listbox.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.weigh_button = tk.Button(master, text="Weigh", command=self.weigh)
        self.weigh_button.pack()

        self.reveal_button = tk.Button(master, text="Reveal Odd Coin", command=self.reveal)

        self.reveal_button.pack()
        # Bind selection events for dynamic coin display
        self.left_listbox.bind('<<ListboxSelect>>', self.update_right_listbox)
        self.right_listbox.bind('<<ListboxSelect>>', self.update_left_listbox)

    def update_right_listbox(self, event=None):
        left_selected = set(self.left_listbox.curselection())
        for i in range(len(self.coins)):
            if i in left_selected:
                self.right_listbox.itemconfig(i, {'fg': 'gray'})
                self.right_listbox.selection_clear(i)
            else:
                self.right_listbox.itemconfig(i, {'fg': 'black'})

    def update_left_listbox(self, event=None):
        right_selected = set(self.right_listbox.curselection())
        for i in range(len(self.coins)):
            if i in right_selected:
                self.left_listbox.itemconfig(i, {'fg': 'gray'})
                self.left_listbox.selection_clear(i)
            else:
                self.left_listbox.itemconfig(i, {'fg': 'black'})
        def update_right_listbox(self, event=None):
            left_selected = set(self.left_listbox.curselection())
            for i in range(len(self.coins)):
                if i in left_selected:
                    self.right_listbox.itemconfig(i, {'fg': 'gray'})
                    self.right_listbox.selection_clear(i)
                else:
                    self.right_listbox.itemconfig(i, {'fg': 'black'})

        def update_left_listbox(self, event=None):
            right_selected = set(self.right_listbox.curselection())
            for i in range(len(self.coins)):
                if i in right_selected:
                    self.left_listbox.itemconfig(i, {'fg': 'gray'})
                    self.left_listbox.selection_clear(i)
                else:
                    self.left_listbox.itemconfig(i, {'fg': 'black'})
    def weigh(self):
        if self.weigh_count >= 3:
            self.result_label.config(text="No more weighings allowed!")
            return

        left_indices = self.left_listbox.curselection()
        right_indices = self.right_listbox.curselection()

        if not left_indices or not right_indices:
            self.result_label.config(text="Select at least one coin on each side!")
            return

        left_weight = sum([1 for i in left_indices])
        right_weight = sum([1 for i in right_indices])

        # Adjust for odd coin
        if self.odd_coin in left_indices:
            left_weight += (1 if self.is_heavier else -1)
        if self.odd_coin in right_indices:
            right_weight += (1 if self.is_heavier else -1)

        self.weigh_count += 1

        if left_weight > right_weight:
            self.result_label.config(text=f"Weighing {self.weigh_count}: Left side is heavier")
        elif right_weight > left_weight:
            self.result_label.config(text=f"Weighing {self.weigh_count}: Right side is heavier")
        else:
            self.result_label.config(text=f"Weighing {self.weigh_count}: Balanced")

    def reveal(self):
        odd_name = self.coins[self.odd_coin]
        nature = "heavier" if self.is_heavier else "lighter"
        self.result_label.config(text=f"The odd coin is {odd_name} ({nature})")


if __name__ == "__main__":
    root = tk.Tk()
    game = CoinWeighingGame(root)
    root.mainloop()

