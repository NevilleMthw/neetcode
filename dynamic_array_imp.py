class DynamicArray:

    def __init__(self, capacity: int):
        self.newArray = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.newArray[i]

    def set(self, i: int, n: int) -> None:
        self.newArray[i] = n

    def pushback(self, n: int) -> None:
        if len(self.newArray) < self.capacity:
            self.newArray[len(self.newArray):] = [n]
        else:
            self.resize()
            self.newArray[len(self.newArray):] = [n]

    def popback(self) -> int:
        return self.newArray.pop()

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return len(self.newArray)

    def getCapacity(self) -> int:
        return self.capacity

