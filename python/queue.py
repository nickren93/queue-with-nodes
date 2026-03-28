class Node:
    def __init__(self, data = None, next = None):
        self.data = data;
        self.next = next;
  


class Queue:
    def __init__(self, front = None):
        self.front = front;
        self.rear = front;
    

    # ADD NODE TO BACK OF QUEUE
    # USE DATA TO CREATE A NEW NODE AND ADD IT TO THE QUEUE
    def enqueue(self, data):
        new_node = Node(data)

        if self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    

    # REMOVE NODE FROM FRONT OF QUEUE AND RETURN IT
    def dequeue(self):
        if self.front is None:
            return None
        
        removed = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        removed.next = None
        return removed
    

    # RETURN NODE AT FRONT WITHOUT REMOVING IT
    def peek(self):
        return self.front


    # RETURN TRUE IF QUEUE IS EMPTY, OTHERWISE FALSE
    def isEmpty(self):
        if self.front:
            return False
        return True
            

    # RETURN NUMBER OF NODES IN QUEUE, E.G. 10
    def size(self):

        num = 0
        node = self.front
        while node != None:   
            num += 1
            node = node.next

        return num

    # RETURN INTEGER REPRESENTING HOW FAR TARGET IS FROM FRONT OF QUEUE
    # IF TARGET ISN'T IN QUEUE, RETURN -1
    def search(self, target):

        num = 0
        node = self.front

        while node is  not None:
            if node.data == target:
                return num
            node = node.next
            num += 1

        return -1
       

    







# if (require.main === module) {
#   // add your own tests in here
 
# }

# module.exports = {
#   Node,
#   Queue
# };

# // Write your Big O findings here

# // Optional: Please add your pseudocode to this file
# // Optional: And a written explanation of your solution
