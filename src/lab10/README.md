## Лабораторная работа 10
### Теоретическая часть

#### Стек (Stack)
**Стек** — структура данных типа LIFO (Last In, First Out — «последним пришёл, первым вышел»). Элементы добавляются и удаляются с одного конца (вершины стека).

**Основные операции:**
- `push(item)` — добавить элемент на вершину стека, **O(1)**
- `pop()` — удалить и вернуть элемент с вершины, **O(1)**
- `peek()` — посмотреть элемент на вершине без удаления, **O(1)**
- `is_empty()` — проверить, пуст ли стек, **O(1)**

**Применение:** управление вызовами функций, отмена действий (undo), проверка сбалансированности скобок.

#### Очередь (Queue)
**Очередь** — структура данных типа FIFO (First In, First Out — «первым пришёл, первым вышел»). Элементы добавляются в конец, а удаляются из начала.

**Основные операции:**
- `enqueue(item)` — добавить элемент в конец очереди, **O(1)**
- `dequeue()` — удалить и вернуть элемент из начала, **O(1)**
- `peek()` — посмотреть первый элемент без удаления, **O(1)**
- `is_empty()` — проверить, пуста ли очередь, **O(1)**

**Применение:** планировщики задач, обработка запросов, BFS в графах.

#### Односвязный список (Singly Linked List)
**Связный список** — динамическая структура данных, состоящая из узлов (Node), каждый из которых содержит значение и ссылку на следующий узел.

**Основные операции:**
- `append(value)` — добавить в конец, **O(1)** (с tail) / **O(n)** (без tail)
- `prepend(value)` — добавить в начало, **O(1)**
- `insert(idx, value)` — вставить по индексу, **O(n)**
- `remove(value)` — удалить по значению, **O(n)**
- `remove_at(idx)` — удалить по индексу, **O(n)**
- Итерация по элементам, **O(n)**
- Доступ по индексу, **O(n)**

**Преимущества перед массивами:**
- Динамическое изменение размера
- Быстрое добавление/удаление в начале (O(1) против O(n) у массива)

**Недостатки:**
- Медленный доступ по индексу (требуется последовательный проход)
- Больше используемой памяти (хранение ссылок)

---

### Реализованные классы

#### Класс Stack (файл `structures.py`)

```python
class Stack:
    def __init__(self):
        self._data = []  # основан на list

    def push(self, item):      # O(1)
    def pop(self):             # O(1)
    def peek(self):            # O(1)
    def is_empty(self):        # O(1)
    def __len__(self):         # O(1)
```

**Пример использования:**
```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())   # 3 (LIFO)
print(stack.peek())  # 2
print(len(stack))    # 2
```

#### Класс Queue (файл `structures.py`)

```python
class Queue:
    def __init__(self):
        self._data = deque()  # основан на collections.deque

    def enqueue(self, item):   # O(1)
    def dequeue(self):         # O(1)
    def peek(self):            # O(1)
    def is_empty(self):        # O(1)
    def __len__(self):         # O(1)
```

**Пример использования:**
```python
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print(queue.dequeue())  # A (FIFO)
print(queue.peek())     # B
print(len(queue))       # 2
```

#### Класс SinglyLinkedList (файл `linked_list.py`)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):    # O(1)
    def prepend(self, value):   # O(1)
    def insert(self, idx, value):  # O(n)
    def remove(self, value):    # O(n)
    def remove_at(self, idx):   # O(n)
    def __iter__(self):         # O(n)
    def __len__(self):          # O(1)
```

**Пример использования:**
```python
lst = SinglyLinkedList()
lst.append(10)
lst.append(20)
lst.prepend(5)
lst.insert(2, 15)
print(list(lst))  # [5, 10, 15, 20]
lst.remove(15)
print(len(lst))   # 3
```
# Выводы по бенчмаркам

## Результаты тестирования производительности

Проведено тестирование на 10 000 операций для каждой структуры:

```
Stack (10k push/pop):     0.003 сек
Queue (10k enqueue/dequeue): 0.004 сек  
LinkedList (10k append/prepend): 0.012 сек
```

## Анализ результатов

### 1. **Стек (Stack) - самый быстрый**
- **Сложность операций:** O(1) для `push()` и `pop()`
- **Причины высокой скорости:**
  - Основан на встроенном списке Python (`list`)
  - Операции `append()` и `pop()` у `list` оптимизированы до O(1)
  - Минимальные накладные расходы на управление памятью
  - Использует непрерывный блок памяти (массив)

### 2. **Очередь (Queue) - очень быстрая, немного медленнее стека**
- **Сложность операций:** O(1) для `enqueue()` и `dequeue()`
- **Причины скорости:**
  - Основан на `collections.deque` (двусторонняя очередь)
  - `deque` специально оптимизирован для операций с обоих концов
  - Реализован на Си, использует кольцевой буфер
- **Почему медленнее стека:**
  - Дополнительные проверки при работе с обоими концами
  - Более сложная внутренняя структура

### 3. **Односвязный список (SinglyLinkedList) - медленнее в 3-4 раза**
- **Сложность операций:**
  - `append()`, `prepend()`: O(1) (с tail)
  - `insert()`, `remove()`, `remove_at()`: O(n)
  - Доступ по индексу: O(n)

### Практическая часть 
#### Задание А - Реализовать Stack и Queue (src/lab10/structures.py)
```
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
```
![im01.png](/images/lab10/im01.png)
#### Задание B - Реализовать SinglyLinkedList (src/lab10/linked_list.py)
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"index {idx} out of range")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self._size += 1

    def remove(self, value):
        if self.is_empty():
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self._size -= 1
                return True
            current = current.next
        return False

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError(f"index {idx} out of range")
        
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            value = current.next.value
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"SinglyLinkedList({list(self)})"


if __name__ == "__main__":
    print("ТЕСТЫ SinglyLinkedList")
    
    lst = SinglyLinkedList()
    print(f"Создан: {lst}, пуст: {lst.is_empty()}")
    
    print("\n1. Добавление:")
    for i in [10, 20, 30]:
        lst.append(i)
    print(f"   append(10,20,30) → {lst}")
    
    lst.prepend(5)
    print(f"   prepend(5) → {lst}")
    
    lst.insert(2, 15)
    print(f"   insert(2,15) → {lst}")
    
    print(f"   Размер: {len(lst)}")
    print(f"   Элементы: {list(lst)}")
    
    print("\n2. Удаление:")
    lst.remove(15)
    print(f"   remove(15) → {lst}")
    
    removed = lst.remove_at(1)
    print(f"   remove_at(1) → {removed}, список: {lst}")
    
    print(f"\n3. Крайние случаи:")
    empty = SinglyLinkedList()
    print(f"   Пустой список: {empty}")
    print(f"   remove(99) на пустом: {empty.remove(99)}")
    
    try:
        empty.remove_at(0)
    except IndexError as e:
        print(f"   Ошибка remove_at(0): {e}")
```
![im02.png](/images/lab10/im02.png)