
class Stack:
    def __init__(self):
        self.items = []

    def check_empty(self):
        return len(self.items) == 0

    def AddItems(self, item):
        self. items.append(item)

    def RemoveItems(self):
        if self.check_empty():
            raise IndexError("An empty stack")
        return self.items.pop()

    def element(self):
        if self.check_empty():
            raise IndexError("An empty stack")
        return self.items[-1]

    def Length(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.AddItems("green")
    stack.AddItems("blue")
    stack.AddItems("yellow")
    stack.AddItems("red")
    print("Top element:", stack.element())  
    print("Stack size:", stack.Length())    
    print("Popped element:", stack.RemoveItems())  
    print("Is stack empty?", stack.check_empty())  
