'''
    Stack data struct
'''
__author__ = "Matthew Byrne"
__date__ = "10/12/19"


# QS
def quicksort(arr):
    if len(arr) > 1:
        p = arr[1]

        l = []
        r = []

        piv = []

        for i in arr:
            if i < p:
                l.append(i)

            elif i > p:
                r.append(i)

            elif i == p:
                piv.append(i)

        return quicksort(l) + piv + quicksort(r)        

    else:
        return arr

# Class
class Stack:
    def __init__(self, *items, limit=None):
        self.items = list(items)

        self.limit = limit if limit else len(self)*2

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        self.pointer = -1
        return self

    def __next__(self):
        self.pointer += 1
        if self.pointer < len(self):
            return self.items[self.pointer]

        else:
            raise StopIteration

    def push(self, item):
        if len(self) < self.limit:
            self.items = self.items + [item]

        else:
            raise OverflowError("Stack Overflow!")

    def pop(self, index=-1):
        if len(self) > 0:
            if index >= len(self.items):
                raise Exception("Given index higher than max of stack")

            *self.items[:index+1], x = self.items[:index+1]

            return x

        else:
            raise OverflowError("Stack Underflow!")

    def __str__(self):
        return f"Stack({', '.join(map(str, self.items))})\t=>\t{self.limit}"

    def __add__(self, other):
        return Stack(*self.items, *other.items, limit=self.limit+other.limit)

    def sort(self):
        x = quicksort(self.items)
        self.items = x
        return self


a = Stack(4, 5, 6, 3)
print(a)
print(sorted(a))
a.sort()
print(a)