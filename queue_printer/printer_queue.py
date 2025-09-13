from collections import deque
import time

def printer_queue():
    """
    Simulates a printer queue using Python's deque.
    Files are printed in the order they are added (FIFO).
    """
    
    # Initialize an empty queue
    queue = deque()

    # Add files to the queue
    queue.append("Document1.pdf")
    queue.append("photo.png")
    queue.append("Report.docx")

    # Show the initial state of the queue
    print(f"Initial Queue: {queue}")

    # Process the queue
    while queue:
        current_file = queue.popleft()  # Remove the first file in the queue
        print(f"Printing {current_file}...")
        time.sleep(1)  # Simulate printing time

    # All files are printed
    print("All files have been printed successfully!")

# Run the printer queue simulation
if __name__ == "__main__":
    printer_queue()
