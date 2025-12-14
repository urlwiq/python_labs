from collections import deque

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        return self._data[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Queue({list(self._data)})"


if __name__ == "__main__":
 
    print("ТЕСТЫ: Stack и Queue")
    
    # Тесты Stack
    print("\n1. Stack (LIFO):")
    s = Stack()
    
    print(f"   Создан: {s}")
    print(f"   Пуст: {s.is_empty()}")
    
    s.push(10); s.push(20); s.push(30)
    print(f"   push(10,20,30) → {s}")
    print(f"   Размер: {len(s)}")
    print(f"   peek(): {s.peek()}")
    
    print(f"   pop(): {s.pop()} → {s}")
    print(f"   pop(): {s.pop()} → {s}")
    print(f"   Пуст: {s.is_empty()}")
    
    # Тесты Queue
    print("\n2. Queue (FIFO):")
    q = Queue()
    
    print(f"   Создана: {q}")
    print(f"   Пуста: {q.is_empty()}")
    
    q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
    print(f"   enqueue(A,B,C) → {q}")
    print(f"   Размер: {len(q)}")
    print(f"   peek(): {q.peek()}")
    
    print(f"   dequeue(): {q.dequeue()} → {q}")
    print(f"   dequeue(): {q.dequeue()} → {q}")
    print(f"   Пуста: {q.is_empty()}")
    
    # Обработка ошибок
    print("\n3. Обработка ошибок:")
    
    try:
        empty_stack = Stack()
        empty_stack.pop()
    except IndexError as e:
        print(f"   Stack.pop() из пустого: {e}")
    
    try:
        empty_queue = Queue()
        empty_queue.dequeue()
    except IndexError as e:
        print(f"   Queue.dequeue() из пустой: {e}")

    print("\n4. Сравнение поведения:")
    print("   Stack: push(1,2,3) → pop() вернет 3,2,1")
    print("   Queue: enqueue(1,2,3) → dequeue() вернет 1,2,3")
    
