#Single Linked List

#menu
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


#creation of node
class node :
    def __init__(self,val):
        self.val=val
        self.next=None

#creation of single linked list
class linkedlist:
    def __init__(self):
        self.head=None

    #inserting at the beginning of a list
    def insert_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    #inserting at the end of a list
    def insert_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head=new_node
        else:
            pos=self.head
            while pos.next!=None:
                pos=pos.next
            pos.next=new_node

    #inserting at position
    def insert_pos(self,pos,data):
        temp=self.head
        i=1
        if pos<1:
            print("Invalid Position")
        else:
            new_node=node(data)
            while i<pos-1 and temp.next!=None:
                i+=1
                temp=temp.next
            
            if i<pos-1:
                print("Invalid Position")
            else:
                new_node.next = temp.next
                temp.next = new_node

    #displaying the list
    def display(self):
        pos=self.head
        while(pos):
            print(pos.val, end="-->")
            pos=pos.next
    #deleting the first element
    def delete_begin(self):
        if self.head==None:
            print("Empty List")
        else:
            self.head=self.head.next
    def delete_end(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
    def delete_pos(self,pos):
        if self.head == None:
            print("Empty list")
        else:
            temp = self.head
            i = 1
            while temp.next!=None and i<pos-1:
                i+=1
                temp = temp.next
            if i==pos-1:
                temp.next = temp.next.next
            else:
                print("Given position is out of range")
    #counting nodes
    def count(self):
        i=1
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        i=i+1
        print("No of Nodes: ", i)
    #searchoiceing
    def searchoice(self,pivot):
        temp=self.head
        if self.head==None:
            print("Empty List")
        else:
            while temp.next!=None:
                if temp.val!=pivot:
                    temp=temp.next
                else:
                    print("Found")
                    break
            if temp.val==pivot:
                print("Found")




llist = linkedlist()
choice=1
while choice!=0:
    choice=int(input("choiceoose an option"))
    if choice==1:
        data=input()
        llist.insert_begin(data)
    if choice==2:
        data=input()
        pos=int(input())
        llist.insert_begin(pos,data)
    if choice==3:
        data=input()
        llist.insert_end(data)
    if choice==4:
        llist.delete_begin()
    if choice==5:
        pos=int(input())
        llist.delete_pos(pos)
    if choice==6:
        llist.delete_end()
    if choice==7:
        llist.display()
    if choice==8:
        llist.count()
    if choice==0:
        break




