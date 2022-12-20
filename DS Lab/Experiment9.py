#double linked lists

print("""choiceoose an option:
1:Insert at beginning
2:Insert at position
3:Insert at end
4:Delete at beginning
5:Delete at position
6:Delete at end
7:Searchoice
8:Count Nodes
9:Display       
0:Exit  
            """)
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    
    def insert_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        i=1
        while i<pos-1 and temp.next!=None:
            temp=temp.next
            i+=1
        if i<pos-1:
            print("Invalid Position")
        elif i==pos-1:
            new_node.next=temp.next
            temp.next.prev=new_node
            temp.next=new_node
            new_node.prev=temp
    
    def delete_begin(self):
        if self.head==None:
            print("Empty List")
        else:
            self.head=self.head.next
            self.head.prev=None
    
    def delete_end(self):
        if self.head==None:
            print("Empty List")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.prev.next=None

    def delete_pos(self,pos):
        if self.head==None:
            print("Empty List")
        else:
            temp=self.head
            i=1
            while temp.next!=None and i<pos-1:
                i+=1
                temp=temp.next
            if i<pos-1:
                print("Invalid Position")
            elif i==pos-1:
                temp.next=temp.next.next
                temp.next.prev=temp

    def searchoice(self,pivot):
        temp=self.head
        if self.head==None:
            print("Empty List")
        else:
            while temp.next!=None:
                if temp.data!=pivot:
                    temp=temp.next
                else:
                    print("Found")
                    break
            if temp.data==pivot:
                print("Found")

    def count(self):
        i=1
        temp=self.head
        while temp.next!=None:
            temp=temp.next
            i=i+1
        print("No of Nodes: ", i)
    
    def display(self):
        pos=self.head
        while(pos):
            print(pos.data, end="-->")
            pos=pos.next


dll=DoubleLinkedList()

choice=1
while choice!=0:
    choice=int(input("choiceoose an option"))
    if choice==1:
        data=input()
        dll.insert_begin(data)
    if choice==2:
        data=input()
        pos=int(input())
        dll.insert_begin(pos,data)
    if choice==3:
        data=input()
        dll.insert_end(data)
    if choice==4:
        dll.delete_begin()
    if choice==5:
        pos=int(input())
        dll.delete_pos(pos)
    if choice==6:
        dll.delete_end()
    if choice==7:
        dll.display()
    if choice==8:
        dll.count()
    if choice==0:
        break      
        

            


        