
from stack import Stack
from queue import Queue


class BinaryTree:
    """二分木"""
    
    class Node:
        """ノード"""
        
        def __init__(self, data=None, left=None, right=None):
            """コンストラクタ"""
            self.data = data
            self.left = left
            self.right = right
    
    def __init__(self):
        """コンストラクタ"""
        # 本来はセッターを作るべきだが、
        # 固定値で初期化する
        self._root = self.Node(
            data=1,
            left=self.Node(
                data=2,
                left=self.Node(4),
                right=self.Node(5)
            ),
            right=self.Node(
                data=3,
                left=self.Node(6),
                right=self.Node(7)
            )
        )
        
    def get_breadth_first(self):
        """幅優先探索"""
        ret = []
        # ルートからノードをキューに出し入れしながら
        # 辿ることで幅優先探索となる
        queue = Queue()
        queue.enqueue(self._root)
        while queue:
            d = queue.dequeue()
            if d.left:
                queue.enqueue(d.left)
            if d.right:
                queue.enqueue(d.right)
            ret.append(d.data)
        return ret

    def get_depth_first(self):
        """深さ優先探索"""
        ret = []
        # ルートからノードをスタックに出し入れしながら
        # 辿ることで深さ優先探索となる
        stack = Stack()
        stack.push(self._root)
        while stack:
            d = stack.pop()
            # スタックには右→左の順に積むとこで
            # 取り出すときに左→右の順になる
            if d.right:
                stack.push(d.right)
            if d.left:
                stack.push(d.left)
            ret.append(d.data)
        return ret


if __name__ == '__main__':
    bt = BinaryTree()
    print(bt.get_breadth_first())
    print(bt.get_depth_first())
    