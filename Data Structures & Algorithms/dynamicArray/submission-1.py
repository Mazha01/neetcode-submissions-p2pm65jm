class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.data = [0] * capacity


    def get(self, i: int) -> int:
       if 0 <= i < self.len:
            return self.data[i] 
       return -1


    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.len:
            self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        
        self.data[self.len] = n
        self.len += 1   
    

    def popback(self) -> int:
        if self.len == 0:
            return -1
        self.len -= 1
        popped = self.data[self.len]
        return popped

    def resize(self) -> None:
        self.capacity *= 2
        new_date = [0] * self.capacity
        for i in range(self.len):
            new_date[i] = self.data[i]
        self.data = new_date


    def getSize(self) -> int:
        return self.len
        
    
    def getCapacity(self) -> int:
        return self.capacity
