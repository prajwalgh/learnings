# from tkinter import *
# import global_var , main
# class GameOfLifeApp:
#     def __init__(self,master,grid):
#         self.master=master
#         self.grid=grid
#         master.title("Game of Life")
#         master.geometry("370x300")
#         self.setup_grid()
#
#
#     def setup_grid(self):
#         while True  :
#             for i in range(global_var.n):
#                 for j in range(global_var.n):
#                     a=self.grid[i][j]
#                     if a==0:
#                         Label(root, text=a, bg='gray', bd=5, relief='groove').grid(column=i, row=j, sticky="nsew")
#                     elif a==1:
#                         Label(root, text=a, bg='yellow', bd=5, relief='groove').grid(column=i, row=j, sticky="nsew")
#             self.grid=main.traverse_grid(self.grid,)
#     def run(self):
#         self.master.mainloop()
#
#
# if __name__=="__main__":
#     root=Tk()
#     grid=main.create_grid_from_db()
#     app=GameOfLifeApp(root,grid)
#     app.run()


import tkinter as tk
import global_var
import main
import time
class GameOfLifeApp:
    def __init__(self, master, grid):
        self.master = master
        self.grid = grid
        master.title("Game of Life")
        master.geometry("500x500")
        self.setup_grid()

    def setup_grid(self):
        for i in range(global_var.n):
            for j in range(global_var.n):
                cell_value = self.grid[i][j]
                bg_color = 'blue' if cell_value == 0 else 'yellow'
                label = tk.Label(self.master, text=str(cell_value), bg=bg_color, bd=5, relief='groove')
                label.grid(column=i, row=j, sticky="nsew")

    def update_grid(self, new_grid):
        self.grid = new_grid
        self.setup_grid()

    def run(self):
        print("run.....")
        self.setup_grid()
        print("......")
        self.update_grid(self.grid)
        for _ in range(7):
            print("pp")
            self.master.update()
            self.master.after(1000, self.update_grid, main.traverse_grid(self.grid))
            time.sleep(1)
        self.master.mainloop()

    # def run(self):
    #     print("run.....")
    #     self.setup_grid()
    #     print("......")
    #     time.sleep(10)
    #     self.update_grid(self.grid)
    #     for i in range(3):
    #         time.sleep(1)
    #         a=main.traverse_grid(self.grid)
    #         self.update_grid(a)
    #     self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    grid = main.create_grid_from_db()
    app = GameOfLifeApp(root, grid)
    app.run()
    root.mainloop()
