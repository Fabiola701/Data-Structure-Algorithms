queue = [] #global variable, semua fungsi mengenal variable tersebut

def enqueue():
    data = input("Enter data to enqueue: ")
    queue.append(data)
    print(f"'{data}' has been enqueued.")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty, cannot dequeue.")
        return None
    data = queue.pop(0)
    print(f"'{data}' has been dequeued.")
    return data

def peek():
    if len(queue) == 0:
        print("Queue is empty, nothing to peek.")
        return None
    data = queue[0]
    print(f"Front of the queue: '{data}'")
    return data

def size():
    print(f"Size of the queue: {len(queue)}")
    return len(queue)

def is_empty():
    empty = len(queue) == 0
    print(f"Is the queue empty? {'Yes' if empty else 'No'}")
    return empty

def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print(f"Queue contents: {queue}")

def main():
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Is Empty")
        print("6. Display")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            enqueue()
        elif choice == '2':
            dequeue()
        elif choice == '3':
            peek()
        elif choice == '4':
            size()
        elif choice == '5':
            is_empty()
        elif choice == '6':
            display()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


