import matplotlib.pyplot as plt

class Knight:
    def __init__(self, init_pos, target) -> None:

        self.position_history = [tuple(init_pos)]
        self.position = init_pos

        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


    def move(self, board):
        next_square = self.find_next_square(board)
        if next_square is None:
            print("stuck knight", len(self.position_history))
            return
        else:
            next_square = tuple(next_square)
            self.position_history.append(next_square)

        board.grid[next_square] *= -1
        self.position = next_square

    # need to rewrite this 
    def find_next_square(self, board):
        next_pos = None
        next_val = None
        for i in self.moves:
            pos = [sum(i) for i in zip(self.position, i)]
            val = board.grid[tuple(pos)]

            if (next_val is None or val < next_val) and val > 0:
                next_val = val
                next_pos = pos

        return next_pos
    

    def show(self):
        plt.plot(*zip(*self.position_history))
        x, y = self.position_history[-1]
        plt.plot(x, y, marker="o", markersize=5, markerfacecolor="green")
            
