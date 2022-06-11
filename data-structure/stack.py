

class Stack:
    """スタック"""

    def __init__(self, max):
        """コンストラクタ"""
        self._stack = [None] * max
        self._sp = 0

    def push(self, data):
        """プッシュ"""
        if self._sp >= len(self._stack):
            raise MemoryError
        self._stack[self._sp] = data
        self._sp += 1

    def pop(self):
        """ポップ"""
        if self._sp <= 0:
            raise MemoryError
        self._sp -= 1
        return self._stack[self._sp]


class StackPythonic:
    """スタック(Python風)"""

    def __init__(self):
        """コンストラクタ"""
        self._stack = []

    def push(self, data):
        """プッシュ"""
        self._stack.append(data)

    def pop(self):
        """ポップ"""
        return self._stack.pop(-1)


if __name__ == '__main__':
    s = Stack(4)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())

    sp = StackPythonic()
    sp.push(1)
    sp.push(2)
    sp.push(3)
    print(sp.pop())
    print(sp.pop())
    print(sp.pop())

