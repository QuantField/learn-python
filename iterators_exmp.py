

# Take aways
# 1 - iter method is called when the collection is traversed, therefore the __itet__ method must return
#     the obect reference
# 2 - next mehtod is called , __next__ must be implemented, this returns the next element in the collection.

class myiter:
    def __init__(self, sequence):
        self.data = sequence
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos>=len(self.data):
            raise StopIteration
        else:
            val = self.data[self.pos]
            self.pos += 1
            return val


z = myiter([2,3,5,6,7])

for r in z:
    print(r)
