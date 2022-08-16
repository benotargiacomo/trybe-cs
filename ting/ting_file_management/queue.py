class Queue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        return self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._queue):
            raise IndexError('Index out of range')
        return self._queue[index]
