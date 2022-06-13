
class Queue:
    """キュー"""

    def __init__(self, max):
        """コンストラクタ"""
        self._buff = [None] * max
        self._head = max - 1
        self._tail = max - 1

    def enqueue(self, data):
        """エンキュー"""
        pos = (self._tail + 1) % len(self._buff)
        if pos == self._head:
            raise MemoryError
        self._buff[pos] = data
        self._tail = pos

    def dequeue(self):
        """デキュー"""
        if self._head == self._tail:
            raise MemoryError
        pos = (self._head + 1) % len(self._buff)
        data = self._buff[pos]
        self._head = pos
        return data
        
    def __str__(self):
        """文字列表現"""
        return f'{self._head}, {self._tail}, {self._buff}'


class QueuePythonic:
    """キュー(Python風)"""

    def __init__(self):
        """コンストラクタ"""
        self._buff = []

    def enqueue(self, data):
        """エンキュー"""
        self._buff.append(data)

    def dequeue(self):
        """デキュー"""
        if len(self._buff) == 0:
            raise MemoryError
        return self._buff.pop(0)

    def __str__(self):
        """文字列表現"""
        return f'{self._buff}'


if __name__ == '__main__':
    q = Queue(4)
    q.enqueue(1)
    print(q)
    q.enqueue(2)
    print(q)
    q.enqueue(3)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    
    print()

    qp = QueuePythonic()
    qp.enqueue(1)
    print(qp)
    qp.enqueue(2)
    print(qp)
    qp.enqueue(3)
    print(qp)
    print(qp.dequeue())
    print(qp)
    print(qp.dequeue())
    print(qp)
    print(qp.dequeue())
    print(qp)
