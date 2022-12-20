#Single Circular Linked Lists

print("""Menu:
1:Insert Begin
2:Insert End
3:Delete Begin
4:Delete End
5:Display
0:Exit
""")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class csll:

    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode
            self.head = newnode

    def insertEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode

    def deleteEnd(self):
        if self.head is None:
            print('no elements present')
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            print(temp.next.data, 'deleted successfully')
            temp.next = self.head

    def deleteBegin(self):
        if self.head is None:
            print('no elements present')
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            print(self.head.data, 'deleted successfully')
            temp.next = self.head.next
            self.head = self.head.next

    def display(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data)



#driver code

csll = csll()
choice=1
while choice != 0:
    choice=int(input())
    if choice == 1:
        ele=int(input('enter element to insert:'))
        csll.insertBegin(ele)
    elif choice == 2:
        ele = int(input('enter element to insert:'))
        csll.insertEnd(ele)
    elif choice == 3:
        csll.deleteBegin()
    elif choice == 4:
        csll.deleteEnd()
    elif choice == 5:
        csll.display()



#double circular linked list
print("""Choose an option:
1:Insert at Beginning
2:Insert at End
3:Delete at Beginning
4:Delete at End
5:Display
0:Exit""")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class CDLL:
    def __init__(self):
        self.head=None
    
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            new_node.prev=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
            new_node.prev=temp

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            new_node.prev=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            new_node.prev=temp
            self.head=new_node
        
    def delete_begin(self):
        if self.head is None:
            print("No elements found")
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=self.head.next
            self.head=temp.next
            self.head.prev=temp
    
    def delete_end(self):
        if self.head is None:
            print("No elements found")
        else:
            temp=self.head
        while temp.next.next!=self.head:
            temp=temp.next
        temp.next=self.head
        self.head.prev=temp
    
    def display(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data)

cdll=CDLL()
choice=1
while choice!=0:
    choice=int(input())
    if choice == 1:
        ele=int(input('enter element to insert:'))
        cdll.insert_begin(ele)
    elif choice == 2:
        ele = int(input('enter element to insert:'))
        cdll.insert_end(ele)
    elif choice == 3:
        cdll.delete_begin()
    elif choice == 4:
        cdll.delete_end()
    elif choice == 5:
        cdll.display()
    elif choice == 0:
        break
    

    



