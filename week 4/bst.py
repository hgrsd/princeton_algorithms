class BST:

    def __init__(self):
        self.root = None

    def __len__(self):
        return BST.size(self.root)

    def put(self, key, value):
        self.root = self.put_recurse(self.root, key, value)

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
        self.root = BST.delete_recurse(self.root, key)

    def del_min(self):
        self.root = BST.del_min_recurse(self.root)

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

    def rank(self, key):
        return BST.rank_recurse(self.root, key)

    @staticmethod
    def put_recurse(scan, key, value):
        if not scan:
            return Node(key, value)
        if key < scan.key:
            scan.left = BST.put_recurse(scan.left, key, value)
        elif key > scan.key:
            scan.right = BST.put_recurse(scan.right, key, value)
        else:
            scan.value = value
        scan.size = 1 + BST.size(scan.left) + BST.size(scan.right)
        return scan

    @staticmethod
    def del_min_recurse(scan):
        if not scan.left:
            return scan.right
        scan.left = BST.del_min_recurse(scan.left)
        scan.size = 1 + BST.size(scan.left) + BST.size(scan.right)
        return scan
    
    @staticmethod
    def delete_recurse(scan, key):
        if not scan:
            return None
        if key < scan.key:
            scan.left = BST.delete_recurse(scan.left, key)
        elif key > scan.key:
            scan.right = BST.delete_recurse(scan.right, key)
        else:
            if not scan.right:
                return scan.left
            if not scan.left:
                return scan.right
            temp = scan
            scan = BST.min(temp.right)
            scan.right = BST.del_min_recurse(temp.right)
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
    def rank_recurse(scan, key):
        if not scan:
            return 0
        if key < scan.key:
            return BST.rank_recurse(scan.left, key)
        elif key > scan.key:
            return 1 + BST.size(scan.left) + BST.rank_recurse(scan.right, key)
        else:
            return BST.size(scan.left)

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
