# ========================================
# To-Do List Project using Linked List
# Each task is stored as a Node
# ========================================

# Node class (represents a single task)
class Node:
    def __init__(self, data):
        self.data = data      # store the task (string)
        self.next = None      # pointer to the next task


# Linked List implementation for To-Do List
class ToDoList:
    
    def __init__(self):
        self.head = None      # start with an empty to-do list
    
    def add_task(self, task):
        """Add a new task at the end of the list"""
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def remove_task(self, task):
        """Remove a task if it exists"""
        current = self.head
        prev = None
        while current:
            if current.data == task:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    
    def search_task(self, task):
        """Check if a task exists in the list"""
        current = self.head
        while current:
            if current.data == task:
                return True
            current = current.next
        return False
    
    def show_tasks(self):
        """Print all tasks in the list"""
        current = self.head
        if not current:
            print("No tasks in the list!")
            return
        while current:
            print(f"- {current.data}")
            current = current.next


# ========================================
# Example usage
# ========================================
if __name__ == "__main__":
    todo = ToDoList()

    # Add tasks
    todo.add_task("Study Python")
    todo.add_task("Do Homework")
    todo.add_task("Go to Gym")
    todo.add_task("Read a Book")

    print(" Your To-Do List:")
    todo.show_tasks()

    # Search for tasks
    print("\n Searching for 'Go to Gym':", todo.search_task("Go to Gym"))      # True
    print(" Searching for 'Cook Dinner':", todo.search_task("Cook Dinner"))    # False

    # Remove a task
    print("\n Removing 'Do Homework'...")
    todo.remove_task("Do Homework")

    print("\n Updated To-Do List:")
    todo.show_tasks()
