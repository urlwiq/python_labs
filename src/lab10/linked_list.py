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
    print("=" * 40)
    print("ТЕСТЫ SinglyLinkedList")
    print("=" * 40)
    
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