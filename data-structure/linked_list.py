


class List:
    """"""
    class Node:
        """"""
        def __init__(self, data=None, next=None):
            """"""
            self.data = data
            self.next = next

    def __init__(self):
        """"""
        self._head = self.Node()
        
    def __str__(self):
        """"""
        str = ''
        cur = self._head.next
        while cur:
            str += f'{cur.data} -> '
            cur = cur.next
        str += 'End'
        return str

    def __getitem__(self, index):
        """"""
        cur = self._head
        for i in range(index + 1):
            cur = cur.next
            if not cur:
                raise IndexError
        return cur.data
        
    def __setitem__(self, index, data):
        """"""
        cur = self._head
        for i in range(index + 1):
            cur = cur.next
            if not cur:
                raise IndexError
        cur.data = data
        
    def append(self, data):
        """"""
        cur = self._head
        while cur.next:
            cur = cur.next
        newdata = self.Node(data)
        cur.next = newdata

    def remove(self, index):
        """"""
        pre = None
        cur = self._head
        for i in range(index + 1):
            pre = cur
            cur = cur.next
            if not cur:
                raise IndexError
        pre.next = cur.next


if __name__ == '__main__':
    l = List()
    l.append(1)
    print(l)
    l.append(2)
    print(l)
    l.append(3)
    print(l)
    l.append(4)
    print(l)
    
    print()

    print(l[1])
    l[1] = 5
    print(l)

    print()

    l.remove(2)
    print(l)