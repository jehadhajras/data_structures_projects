# ========================================
# Doubly Linked List Implementation
# University Queue Example
# ========================================

class Node:
    def __init__(self, data):
        self.data = data     # store student name
        self.next = None     # pointer to next student
        self.prev = None     # pointer to previous student


class DoublyLinkedList:
    def __init__(self):
        self.head = None     # start of the queue
        self.tail = None     # end of the queue
    
    def insert_at_end(self, data):
        """Add a new student at the end of the queue"""
        new_node = Node(data)
        
        if self.head is None:   # if the queue is empty
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    def delete_node(self, key):
        """Remove a student by name if exists"""
        current = self.head
        
        while current:   # search for the student
            if current.data == key:
                if current.prev:    # if not the first student
                    current.prev.next = current.next
                else:   # if it's the first student
                    self.head = current.next
                
                if current.next:    # if not the last student
                    current.next.prev = current.prev
                else:   # if it's the last student
                    self.tail = current.prev
                return
            current = current.next
    
    def search_node(self, key):
        """Search for a student in the queue"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def print_list(self):
        """Print the queue from start to end"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# ------------------------
# Example Usage
# ------------------------

if __name__ == "__main__":
    queue = DoublyLinkedList()

    # Students arrive to the queue
    queue.insert_at_end("Ali")
    queue.insert_at_end("Sara")
    queue.insert_at_end("Omar")
    queue.insert_at_end("Lina")

    print("Queue after students arrive:")
    queue.print_list()

    # Search for students
    print("Is Sara in the queue?", queue.search_node("Sara"))   # True
    print("Is Ahmad in the queue?", queue.search_node("Ahmad")) # False

    # One student leaves the queue
    queue.delete_node("Omar")
    print("\nQueue after Omar left:")
    queue.print_list()

    # Another student leaves (first one)
    queue.delete_node("Ali")
    print("\nQueue after Ali left:")
    queue.print_list()
