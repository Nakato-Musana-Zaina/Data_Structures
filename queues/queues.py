class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("An empty queue")
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        self.size -= 1
        return dequeued_value

    def peek(self):
        if self.is_empty():
            raise IndexError("An empty queue")
        return self.front.value

    def get_size(self):
        return self.size


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Front element:", queue.peek())  
    print("Queue size:", queue.get_size())  
    print("Dequeued element:", queue.dequeue()) 
    print("Is queue empty?", queue.is_empty())  