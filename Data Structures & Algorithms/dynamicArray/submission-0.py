class DynamicArray:
    
    def __init__(self, capacity: int):
       self.capacity = capacity
       self.size = 0
       self.Array = [0] * capacity

    def get(self, i: int) -> int:
        return self.Array[i]

    def set(self, i: int, n: int) -> None:
        self.Array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.Array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.Array[self.size]

    def resize(self) -> None:
       self.capacity *= 2
       new_array = [0] * self.capacity
       for i in range(self.size):
           new_array[i] = self.Array[i]
       self.Array = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity