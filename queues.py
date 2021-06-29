class ArrayQueue:
    QUEUE_DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.QUEUE_DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        else:
            return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


class DequeArray:
    QUEUE_DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * DequeArray.QUEUE_DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        else:
            return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        else:
            return self._data[(self._front + self._size - 1) % len(self._data)]

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        answer = self._data[(self._front + self._size - 1) % len(self._data)]
        self._data[(self._front + self._size - 1) % len(self._data)] = None
        self._front = (self._front - 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(3)
    print(Q.first())
    Q.enqueue(56)
    print(Q.first())
    Q.dequeue()
    print(Q.first())

    D = DequeArray()
    D.add_first(3)
    print(D.first())
    D.add_last(6)
    print(D.last())
    D.add_first(78)
    print(D.first())
    print(D.last())
    D.delete_last()
    print(D.last())
