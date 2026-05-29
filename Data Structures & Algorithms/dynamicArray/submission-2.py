class DynamicArray:
    
    def __init__(self, capacity: int):

        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        # Items set in the array can't exceed capacity
        self.array = []
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        if self.array == []:
            return []

        if i < 0 or i >= self.size:
            raise IndexError("The index value is not valid")

        return self.array[i]

    def set(self, i: int, n: int) -> None:
        # if i > self.capacity - 1:
        #     raise IndexError("The index value is not valid")

        # Check to see if the actual indices exist in the array
        while len(self.array) <= i:
            # Start padding out 
            self.array.append(None)
            self.size += 1
        
        if i < self.size and i >= 0:
            self.array[i] = n
        else:
            raise IndexError("The index value is not valid")

    def pushback(self, n: int) -> None:        
        if self.size == self.capacity:
            self.resize()

        # self.array[self.size] = n
        self.array.append(n)
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            element = self.array.pop()
            self.size -=1
            return element
        else:
            raise IndexError("Cannot pop from empty array.")
        

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity