'''
Vectors
'''

# Imports
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from math import sqrt, sin, cos
from random import choice as ch

# Main class
class Vector:
    dimensions = ["x", "y", "z", "t"]
    def __init__(self, *coordinates):
        self.x = 0
        self.y = 0
        self.z = 0
        self.t = 0

        self.coords = list(coordinates)
        self.dim = len(coordinates)

        for idx, dim in enumerate(Vector.dimensions):
            try:
                exec(f"self.{dim} = coordinates[{idx}]")

            except:
                break


    def __add__(self, other):
        if type(other) is int:
            a = [other] + [0 for x in range(len(self.coords)-1)]

        if self.dim != other.dim:
            raise ValueError("Cannot add vectors of different dimensions")
        
        new = []

        for i, j in zip(self.coords, other.coords):
            new.append(i+j)

        return Vector(*new)

    def __getitem__(self, name):
        return self.coords[name]

    def __mul__(self, other):
        if type(other) is int:
            return Vector(*[coord*other for coord in self.coords])

        elif type(other) is Vector:
            new = Vector(*[0 for _ in self.coords])
            for idx, i in enumerate(self.coords):
                new.coords[idx] = i*other[idx]

            return new

        elif type(other) is Matrix:
            return other * self

    def dot(self, other):
        total = 0
        for i, j in zip(self.coords, other.coords):
            total += i*j 

        return total

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k + {self.t}l".replace(" + 0k", "").replace(" + 0j", "").replace(" + 0l", "").replace("0i + ", "").replace("+ -", "- ")

    def __repr__(self):
        return f"→({', '.join(map(str, self.coords))})"

    def __pow__(self, power):
        product = self

        for _ in range(power-1):
            product = self * product

        return product

    def __truediv__(self, other):
            a = self * other
            b = other ** 2

            return a/b

    def magnitude(self):
        return sqrt(sum([i**2 for i in self.coords]))

    def __int__(self):
        return int(self.magnitude())

    def __float__(self):
        return self.magnitude()

    def plot(self, colour="r", start=(0, 0), figure=plt):
    	#figure.arrow(start[0], start[1], self.x, self.y, color=colour, length_includes_head=True, head_width=0.25, head_length=0.5)
        figure.plot([start[0], self.x], [start[1], self.y], color=colour)


class Matrix:
    def __init__(self, *rows):
        self.matrix = list(rows)
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError("Cannot add matrices of different dimensions")

        new = []

        for idx, row in enumerate(self.matrix):
            new.append([])
            for jdx, item in enumerate(row):
                new[idx].append(item + other.matrix[idx][jdx])

        return Matrix(*new)

    def __getitem__(self, name):
        return self.matrix[name]

    def __str__(self):
        output = "Matrix:"
        for row in self.matrix:
            output += "\n" + ", ".join(map(str, row))

        return output

    def rotate(self):
        new = Matrix(*[[0 for _ in self.matrix] for _ in self.matrix[0]])

        for m, row in enumerate(self.matrix):
            for n, col in enumerate(row):
                new[n][m] = col

        return new


    def __mul__(self, other):
        if type(other) is int:
            new = []
            for idx, row in enumerate(self.matrix):
                new.append([])
                for jdx, item in enumerate(row):
                    new[idx].append(item*other)
            return Matrix(*new)

        elif type(other) is Vector:
            
            coords = []

            for row in self.matrix:
                total = 0
                
                for coord, item in zip(other.coords, row):
                    total += coord*item
                
                coords.append(total)

            return Vector(*coords)


        elif type(other) is Matrix:
            if self.n == other.m:
                new = Matrix(*[[0 for _ in other.matrix[0]] for _ in other.matrix])

                rotated = other.rotate()

                for i in range(new.m):
                    for j in range(new.n):
                        total = 0

                        for x, y in zip(self[i], rotated[j]):
                            total += x*y

                        new[i][j] = total
            
                return new


            elif self.m == other.n:
                return other * self

            else:
                raise ValueError("Cannot multiply two matrices of incompatable dimensions")
        
        


if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([-10, 10], [0, 0], "b--")
    ax.plot([0, 0], [-10, 10], "b--")
    
    v3 = Vector(6,6)

    x = 31/180

    rm = Matrix(
    	[cos(x), sin(x)],
    	[-sin(x), cos(x)]
    )

    print(rm)

    v3.plot(figure = ax)

    colours = ["black"]

    v4 = v3*rm
    v5 = v4*rm
    v6 = v5*rm    

    for _ in range(10):
        v4.plot(ch(colours), figure = ax)
        v4 *= rm

    #v5.plot("pink", figure = ax)
    #v6.plot("green", figure = ax)
    ax.set_aspect(1)
    plt.legend(["x Axis", "y Axis", "Original", "Rotations"])

    plt.show()


