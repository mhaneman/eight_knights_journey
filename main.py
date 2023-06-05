import matplotlib.pyplot as plt

from board import Board
from knight import Knight


class TKJ:
    def __init__(self) -> None:
        self.board = Board()
        self.knights = [Knight([0, 0], 0), Knight([0, 0], 8)]


    def traverse_board(self):
        for i in self.knights:
            i.move(self.board)


    def plot_sim(self):
        # self.board.show()

        for i in self.knights:
            i.show()
        plt.show()




if __name__ == "__main__":
    tkj = TKJ()

    for _ in range(0, 1_880):
        tkj.traverse_board()
        
    tkj.plot_sim()

    