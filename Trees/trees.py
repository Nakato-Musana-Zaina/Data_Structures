class Node:
    def __init__(self, number):
        self.leftPointer = None
        self.rightPointer = None
        self.value = number


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, number):
        if self.root is None:
            self.root = Node(number)
        else:
            self._insert_recursively(self.root, number)

    def _insert_recursively(self, current_node, number):
        if number < current_node.value:
            if current_node.leftPointer is None:
                current_node.leftPointer = Node(number)
            else:
                self._insert_recursively(current_node.leftPointer, number)
        else:
            if current_node.rightPointer is None:
                current_node.rightPointer = Node(number)
            else:
                self._insert_recursively(current_node.rightPointer, number)

    def search(self, number):
        return self._search_recursively(self.root, number)

    def _search_recursively(self, current_node, number):
        if current_node is None or current_node.value == number:
            return current_node
        if number < current_node.value:
            return self._search_recursively(current_node.leftPointer, number)
        return self._search_recursively(current_node.rightPointer, number)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, current_node):
        return (self._inorder_traversal(current_node.leftPointer) if current_node.leftPointer else []) + \
               [current_node.value] + \
               (self._inorder_traversal(current_node.rightPointer) if current_node.rightPointer else [])
    

if __name__ == "__main__":
    tree = BinaryTree()
    elements = [7, 3, 9, 1, 5, 8, 10]

    for element in elements:
        tree.insert(element)

    print("Inorder Traversal:", tree.inorder_traversal())
    
    search_number = 5
    found_node = tree.search(search_number)
    if found_node:
        print(f"Node {search_number} found in the tree.")
    else:
        print(f"Node {search_number} not found in the tree.")