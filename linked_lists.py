# Algorithm add first(L,e):
# newest = Node(e) {create new node instance storing reference to element e}
# newest.next = L.head {set new node’s next to reference the old head node}
# L.head = newest {set variable head to reference the new node}
# L.size = L.size+1 {increment the node count}

# Algorithm add last(L,e):
# newest = Node(e) {create new node instance storing reference to element e}
# newest.next = None {set new node’s next to reference the None object}
# L.tail.next = newest {make old tail node point to new node}
# L.tail = newest {set variable tail to reference the new node}
# L.size = L.size+1 {increment the node count}
class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError('Empty Queue')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Empty Queue')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1


if __name__ == '__main__':
    S = LinkedStack()
    S.push(4)
    print(S.top())
    S.push(67)
    print(S.top())
    S.pop()
    print(S.top())

    Q = LinkedQueue()
    print(Q.is_empty())
    Q.enqueue(45)
    print(Q.first())
    Q.enqueue(67)
    print(Q.first())
    Q.dequeue()
    print(Q.first())
