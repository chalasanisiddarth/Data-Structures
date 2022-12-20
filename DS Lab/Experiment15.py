class Queue:
    def __init__(self,):
        self.max=5
        self.queue=[]
        self.front=0
        self.rear= -1
    
    def enqueue(self,data):
        if self.rear<self.max:
            self.rear+=1
            self.queue[self.rear]=data
        else:
            print("Queue is full")
    
    def dequeue(self):
        if self.front<=self.rear:
            self.queue[self.front]=None
        else:
            print("Queue is empty")

    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i])

    
queue1=Queue()

queue1.enqueue(3)
queue1.enqueue(5)
queue1.enqueue(6)
queue1.dequeue()
queue1.enqueue(0)
queue1.display()