# Binary Search Tree

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.parent = None 
        self.left = None 
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node 
        else:
            iter = self.root
            while True:
                if iter.value > value:
                    # go left
                    if iter.left is None:
                        iter.left = node 
                        node.parent = iter
                        return
                    else:
                        iter = iter.left
                else: 
                    # go right
                    if iter.right is None:
                        iter.right = node 
                        node.parent = iter
                        return
                    else:
                        iter = iter.right

    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)    

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)    

    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)   
            print(node.value)


if __name__ == '__main__':
    tree = BST()
    tree.add(100)
    tree.add(70)
    tree.add(150)
    tree.add(50)
    tree.add(30)
    tree.add(80)
    tree.add(75)
    tree.add(90)
    tree.add(120)
    tree.add(180)
    tree.add(160)
    tree.add(200)

    tree.postorder(tree.root)