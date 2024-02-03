queue = []

def enqueue(item):
    queue.append(item)
    print(f"{item} has been enqueued.")

    def dequeue():
        if not queue:
            print("Queue is empty.Cannot dequeue.")
            return None
        else:
            item = queue.pop(0)
            print(f"{item} has been dequeued.")
            return item
        
        enqueue(1)
        enqueue(2)
        enqueue(3)
        dequeue_result = dequeue()
        print("Dequeued item:", dequeue_result)


        enqueue(4)

        print("Current queue:", queue)
