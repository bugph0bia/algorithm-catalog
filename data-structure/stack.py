

class StackClassic:
    """スタック"""

    def __init__(self, max):
        """コンストラクタ"""
        self._buff = [None] * max
        self._sp = 0

    def push(self, data):
        """プッシュ"""
        if self._sp >= len(self._buff):
            raise MemoryError
        self._buff[self._sp] = data
        self._sp += 1

    def pop(self):
        """ポップ"""
        if self._sp <= 0:
            raise MemoryError
        self._sp -= 1
        return self._buff[self._sp]
        
    def __str__(self):
        """文字列表現"""
        return f'{self._sp}, {self._buff}'


class Stack:
    """スタック"""

    def __init__(self):
        """コンストラクタ"""
        self._buff = []

    def push(self, data):
        """プッシュ"""
        self._buff.append(data)

    def pop(self):
        """ポップ"""
        if len(self._buff) == 0:
            raise MemoryError
        return self._buff.pop(-1)

    def __str__(self):
        """文字列表現"""
        return f'{self._buff}'

    def __bool__(self):
        """真偽"""
        return bool(self._buff)


if __name__ == '__main__':
    s = StackClassic(4)
    s.push(1)
    print(s)
    s.push(2)
    print(s)
    s.push(3)
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)

    print()

    s = Stack()
    s.push(1)
    print(s)
    s.push(2)
    print(s)
    s.push(3)
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s)
