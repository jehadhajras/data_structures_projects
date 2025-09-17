class Node:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.left = None
        self.right = None


class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, student_id, name):
        new_node = Node(student_id, name)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if student_id < current.student_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # Inorder Traversal: left → root → right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"ID: {node.student_id}, Name: {node.name}")
            self.inorder(node.right)

    # Search by student_id
    def search(self, node, student_id):
        if node is None:
            return None
        if node.student_id == student_id:
            return node
        elif student_id < node.student_id:
            return self.search(node.left, student_id)
        else:
            return self.search(node.right, student_id)


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    students = StudentBST()

    students.insert(102, "Sara")
    students.insert(55, "Ahmed")
    students.insert(98, "Omar")
    students.insert(150, "Lina")
    students.insert(43, "Hamza")
    students.insert(1, "Joe")

    print("\nAll Students in order By ID:")
    students.inorder(students.root)

    print("\nSearching for a student:")
    result = students.search(students.root, 150)
    if result:
        print(f"We Found ID: {result.student_id}, Name: {result.name}")
    else:
        print("Student Not Found!")
