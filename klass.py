from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        return Matrix()

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))


exec(stdin.read())
