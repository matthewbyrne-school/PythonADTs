'''
    Linked lists
'''
__author__ = "Matthew Byrne"
__date__ = "10/12/19"

# Main Node Class
class node:
    def __init__(self, val, next=None, last=None):
        self.val = val
        self.next = next
        self.last = last

    def __str__(self):
        return str(self.val)
        # return repr(self)

    def __repr__(self):
        return f"n({str(self.val)}, {str(self.next.val) if self.next else 'None'}, {str(self.last.val) if self.last else 'None'})"

# Main LL class
class LinkedList:
    def __init__(self, *items):
        self.head = node(None)
        self.end = node(None, None, self.head)
        self.head.next = self.end
        self.pointer = self.head

        for i in items:
            self.push(i)

    def advance(self):
        if self.pointer.next.val:
            self.pointer = self.pointer.next

        else:
            raise Exception("Cannot advance")

    def regress(self):
        if self.pointer.last.val:
            self.pointer = self.pointer.last

        else:
            raise Exception("Cannot regress")

    def __iter__(self):
        self.pointer = self.head
        return self

    def __next__(self):
        try:
            self.advance()
            return self.pointer

        except Exception:
            raise StopIteration

    def __str__(self):
        return " <=> ".join(map(str, [i for i in self]))

    def __len__(self):
        total = 0
        for i in a:
            total += 1

        return total

    def __getitem__(self, name):
        for i, I in enumerate(a):
            if i == name:
                return I


    def push(self, item):
        if type(item) is int or type(item) is str:
            Node = node(item, self.end, self.end.last)

            self.end.last.next = Node
            self.end.last = Node

        elif type(item) is list:
            for i in item:
                self.push(i)

    def pop(self, index):
        total = -1
        for i in self:
            total += 1
            if total == index:
                i.next.last = i.last
                i.last.next = i.next

                x = i
                i = self.head

                return x


    def __add__(self, other):
        a = [i for i in self]
        b = [i for i in other]
        c = a + b
        c = [i.val for i in c]
        new = LinkedList(*c)
        return new

