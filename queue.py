'''
    Queue data struct
'''
__author__ = "Matthew Byrne"
__date__ = "10/12/19"


# Class
class Queue:
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

    def enqueue(self, item):
        if len(self) < self.limit:
            self.items = self.items + [item]

        else:
            raise OverflowError("Queue Overflow!")

    def dequeue(self, index=0):
        if len(self) > 0:
            if index >= len(self.items):
                raise OverflowError("Given index higher than max of queue")

            x, *self.items[index:] = self.items[index:]

            return x

        else:
            raise OverflowError("Queue Underflow!")

    def __str__(self):
        return f"Queue({', '.join(map(str, self.items))})\t=>\t{self.limit}"

    def __add__(self, other):
        return Queue(*self.items, *other.items, limit=self.limit+other.limit)


