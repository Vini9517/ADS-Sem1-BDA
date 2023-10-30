from queues import *
#----------------------------------
#q1

def test_simple_queue():
    # Test enqueue and dequeue
    q = SimpleQueue()
    q.enqueue(1)
    assert q.dequeue() == 1

    # Test is_empty
    assert q.is_empty() == True

    # Test size
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 2
    q.dequeue()
    assert q.size() == 1

if __name__ == "__main__":
    test_simple_queue()
    print("All tests passed for simple queue!")
#------------------------------------------------------
#q2
def test_simple_queue_limited():
    # Test enqueue and dequeue
    q = SimpleQueueLimited(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1

    # Test is_empty and is_full
    assert not q.is_empty()
    assert not q.is_full()

    # Test size
    q.enqueue(4)
    assert q.size() == 3
    assert q.is_full()

    # Test attempting to enqueue when full
    try:
        q.enqueue(5)
    except ValueError as e:
        assert str(e) == "Queue is full"

if __name__ == "__main__":
    test_simple_queue_limited()
    print("All tests passed in q2!")
#-------------------------------------------
#q3
def test_flexi_queue():
    # Test enqueue and dequeue
    q = FlexiQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1

    # Test is_empty
    assert not q.is_empty()

    # Test size
    assert q.size() == 2

    # Test shrink
    q.shrink()
    assert q.size() == 1  
    # Test expand
    q.enqueue(4)
    q.enqueue(5)
    q.expand()
    assert q.size() == 4

if __name__ == "__main__":
    test_flexi_queue()
    print("All tests passed q3!")
#----------------------------------------------
#q4
def test_stack_with_queues():
    # Test push and pop
    stack = StackWithQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()

    # Test is_empty and size
    assert stack.is_empty() == True
    stack.push(4)
    assert stack.is_empty() == False
    assert stack.size() == 1

    # Test popping from an empty stack
    try:
        stack.pop()
    except IndexError as e:
        assert str(e) == "Stack is empty"

if __name__ == "__main__":
    test_stack_with_queues()
    print("All tests passed in q4!")

#-------------------------------------------
#q5
def test_queue_with_stacks():
    # Test enqueue and dequeue
    queue = QueueWithStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()

    # Test is_empty and size
    assert queue.is_empty() == True
    queue.enqueue(4)
    assert queue.is_empty() == False
    assert queue.size() == 1

    # Test dequeue from an empty queue
    try:
        queue.dequeue()
    except IndexError as e:
        assert str(e) == "Queue is empty"

if __name__ == "__main__":
    test_queue_with_stacks()
    print("All tests passed in q5!")

#--------------------------------------------------------
#q6
def test_queue_with_rotate():
    # Test enqueue and dequeue
    queue = QueueWithRotate()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()

    # Test is_empty and size
    assert queue.is_empty() == True
    queue.enqueue(4)
    assert queue.is_empty() == False
    assert queue.size() == 1

    # Test rotate
    queue.enqueue(5)
    queue.enqueue(6)
    queue.rotate()
    assert queue.dequeue() == 5
    assert queue.dequeue() == 6
    assert queue.is_empty()

if __name__ == "__main__":
    test_queue_with_rotate()
    print("All tests passed in q6!")

#---------------------------------------------
# q7
def test_queue_with_find_max():
    # Test findMax on an empty queue
    queue = QueueWithFindMax()
    try:
        max_val = queue.findMax()
    except ValueError as e:
        assert str(e) == "Queue is empty"

    # Test findMax on a non-empty queue
    queue.put(1)
    queue.put(3)
    queue.put(2)
    max_val = queue.findMax()
    assert max_val == 3  # Maximum value in the queue should be 3
    assert queue.qsize() == 3  # The queue size should remain unchanged

    # Test findMax on a queue with negative values
    queue = QueueWithFindMax()
    queue.put(-1)
    queue.put(-3)
    queue.put(-2)
    max_val = queue.findMax()
    assert max_val == -1  # Maximum value in the queue should be -1

if __name__ == "__main__":
    test_queue_with_find_max()
    print("All tests passed in q7!")

#----------------------------------------------------------------
