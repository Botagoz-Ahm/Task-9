from sys import stdin
from copy import deepcopy


class Matrix:
    def __add__(self, other):
        return Matrix(list(map(
                        lambda x, y: list(map(lambda z, w: z + w, x, y)),
                        self.matrix, other.matrix)))

    def __mul__(self, other):
        return Matrix([[i * other for i in list] for list in self.matrix])

    __rmul__ = __mul__


exec(stdin.read())
