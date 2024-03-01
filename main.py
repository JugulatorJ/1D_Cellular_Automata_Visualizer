import numpy as np
import streamlit as st
from matplotlib import pyplot as plt


class Rule:

    @staticmethod
    def take_number() -> int:

        while True:
            try:
                rule_number = int(input('Provide integer number in range 0 - 255: '))
                if 0 <= rule_number <= 255:
                    return rule_number
                else:
                    print("Number out of range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def convert_to_binary(int_rule_number) -> list:

        bi_rule_number = [int(x) for x in np.binary_repr(int_rule_number, width=8)]

        return bi_rule_number


class Canvas:

    @staticmethod
    def take_columns() -> int:

        while True:
            try:
                number_of_columns = int(input('Provide odd integer number: '))
                if number_of_columns % 2 != 0:
                    return number_of_columns
                else:
                    print("Number of columns is even. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an odd integer.")

    @staticmethod
    def make_rows(columns) -> int:
        rows = int(columns / 2) + 1
        return rows

    @staticmethod
    def make_canvas(columns, rows):

        canvas = np.zeros([rows, columns + 2])
        canvas[0, int(columns / 2) + 1] = 1
        return canvas


class PossiblePatterns:
    input_pattern = np.array([[int(x) for x in np.binary_repr(7 - i, width=3)] for i in range(8)])

    def __init__(self):
        pass


class Filler:

    def __init__(self, my_canvas, col, row, patterns, binary_rule):

        self.my_canvas = my_canvas
        self.col = col
        self.row = row
        self.patterns = patterns
        self.binary_rule = binary_rule

    def fill(self):

        for i in np.arange(0, self.row - 1):
            for j in np.arange(0, self.col - 1):
                for k in range(8):
                    if np.array_equal(self.patterns[k, :], self.my_canvas[i, j:j + 3]):
                        self.my_canvas[i + 1, j + 1] = self.binary_rule[k]

        return self.my_canvas


class Plotter:

    def __init__(self, fill_canvas, col, rule):
        self.fill_canvas = fill_canvas
        self.col = col
        self.rule = rule

    def plot(self):
        fig, ax = plt.subplots()
        ax.imshow(self.fill_canvas[:, 1:self.col + 1], cmap='rainbow')
        title_font = {'family': 'serif', 'color': 'green', 'size': 15}
        ax.set_title(f"Rule {self.rule}", fontdict=title_font)
        return fig


def main():

    st.title("1-Dimensional Cellular Automata Visualizer")

    rule = st.number_input("Provide integer number in range 0 - 255 for the rule:", min_value=0, max_value=255, value=110)
    binary_rule = Rule.convert_to_binary(rule)
    col = st.slider("Select number of columns (must be odd):", min_value=3, max_value=499, value=51, step=2)
    row = Canvas.make_rows(col)
    my_canvas = Canvas.make_canvas(col, row)
    patterns = PossiblePatterns().input_pattern
    filled_canvas = Filler(my_canvas, col, row, patterns, binary_rule).fill()
    plotter = Plotter(filled_canvas, col, rule)

    st.pyplot(plotter.plot())

if __name__=='__main__':
    main()

