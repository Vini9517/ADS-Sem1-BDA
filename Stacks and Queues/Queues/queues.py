#implement simple queue using list data structure
class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
#-------------------------------------------------------------
#Modify Q1 such that Simple Queue can contain limited amount of elements.
class SimpleQueueLimited:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
        else:
            raise ValueError("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def size(self):
        return len(self.queue)
#----------------------------------------------------------------------
# Implement “FlexiQueue” with capacity to expand and shrunk based on elements to be added or deleted.
class FlexiQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def shrink(self):
        if len(self.queue) <= 0.25 * len(self.queue):
            self.queue = self.queue[:len(self.queue) // 2]

    def expand(self):
        if len(self.queue) == len(self.queue):
            self.queue += [None] * len(self.queue)

#----------------------------------------------------------
#Implement Stack using two Queues
class StackWithQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue1.put(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        top_item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1 
        return top_item

    def is_empty(self):
        return self.queue1.qsize() == 0

    def size(self):
        return self.queue1.qsize()
#---------------------------------------------------------------------
#Implement Queue using two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)
#------------------------------------------------------------
"""Assume that we have Queue with some elements. Write method rotate() which added 
the existing elements in the reverse order."""
class QueueWithRotate:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def rotate(self):
        if not self.is_empty():
            self.queue = self.queue[::-1]

#----------------------------------------------------------------------
"""Implement findMax() method, which return the maximum value of element present in 
the queue. After finding maximum element, queue content should be same as original"""
class QueueWithFindMax(Queue):
    def findMax(self):
        """Find and return the maximum value of elements in the queue."""
        if self.empty():
            raise ValueError("Queue is empty")

        max_value = float('-inf')  # Initialize max_value with negative infinity
        for i in range(self.qsize()):
            item = self.get()
            max_value = max(max_value, item)
            self.put(item)  # Put the item back into the queue
        return max_value
#--------------------------------------------------------------
