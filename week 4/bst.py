class BST:

    def __init__(self):
        self.root = None

    def __len__(self):
        return BST.size(self.root)

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def get(self, key):
        scan = self.root
        while scan:
            if scan.key == key:
                return scan.value
            elif key < scan.key:
                scan = scan.left
            else:
                scan = scan.right
        raise IndexError("Key not found.")

    def delete(self, key):
        self.root = BST._delete(self.root, key)

    def del_min(self):
        self.root = BST._del_min(self.root)

    def generate_tree(self):
        if len(self) == 0:
            return None
        if len(self) == 1:
            return [self.root]
        queue = [self.root]
        tree = []
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            tree.append(cur)
        return tree

    @staticmethod
    def _put(scan, key, value):
        if not scan:
            return Node(key, value)
        if key < scan.key:
            scan.left = self._put(scan.left, key, value)
        elif key > scan.key:
            scan.right = self._put(scan.right, key, value)
        else:
            scan.value = value
        scan.size = 1 + BST.size(scan.left) + BST.size(scan.right)
        return scan

    @staticmethod
    def _del_min(scan):
        if not scan.left:
            return scan.right
        scan.left = BST._del_min(scan.left)
        scan.size = 1 + BST.size(scan.left) + BST.size(scan.right)
        return scan
    
    @staticmethod
    def _delete(scan, key):
        if not scan:
            return None
        if key < scan.key:
            scan.left = BST._delete(scan.left, key)
        elif key > scan.key:
            scan.right = BST._delete(scan.right, key)
        else:
            if not scan.right:
                return scan.left
            if not scan.left:
                return scan.right
            temp = scan
            scan = BST._min(temp.right)
            scan.right = BST._del_min(temp.right)
            scan.left = temp.left
        scan.size = 1 + BST.size(scan.left) + BST.size(scan.right)
        return scan

    @staticmethod
    def min(scan):
        while scan.left:
            scan = scan.left
        return scan

    @staticmethod
    def max(scan):
        while scan.right:
            scan = scan.right
        return scan

    @staticmethod
    def size(node):
        if node:
            return node.size
        else:
            return 0


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def __len__(self):
        return self.size
