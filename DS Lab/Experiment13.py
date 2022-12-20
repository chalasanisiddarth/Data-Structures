#stack implementation
print("""Choose an option:
    1:Insert at end
    2:Delete at end
    3:To check if stack is empty
    4:To check if stack is full
    5:To display
    0:TO Exit""")
class Stack:
    def __init__(self):
        self.stack=[]
        self.length=0
        self.mai=10
        self.top=-1
    
    def push(self,data):
        if self.length<self.mai:
            self.stack.append(data)
            self.length+=1
            self.top+=1
        elif self.length>=self.mai:
            print("STACK OVERFLOW")
            choice=0
        
    def pop(self):
        if self.length==0:
            print("STACK UNDERFLOW")
        else:   
            self.length-=1
            self.top-=1
            return self.stack.pop()
            
            
        
    def isEmpty(self):
        if self.length==0:
           print("Stack is empty")
        else:
            print("Stack is not empty")

    def isFull(self):
        if self.length==self.mai:
            print("Stack is Full")
        else:
            print("Stack is not Full")
    
    def display(self):
        for items in self.stack[::-1]:
            print(items)
    
    def peak(self):
        return self.stack[-1]
    
    def reverse(self,string):
        stack=Stack()
        n=len(string)

        for i in range(0,n):
            stack.push(string[i])

        string=""
        for i in range(0,n):
            string+=stack.pop()
        print(string)
    
    def eval_postfii(self,string):
        stack1=Stack()
        for i in range(0,len(string)):
            if string[i].isdigit():
                stack1.push((int(string[i])))
            else:
                val2 = stack1.pop()
                val1 = stack1.pop()
                if string[i]=='*':
                    stack1.push(val1*val2)
                if string[i]=='+':
                    stack1.push(val1+val2)
                if string[i]=='-':
                    stack1.push(val1-val2)
                if string[i]=='/':
                    stack1.push(val1/val2)
        print("Postfii Eipression :", string)
        print("Answer :",stack1.pop())
         
        
    def infix_to_postfix(self,data):
        priority={"^":0,
        "*":1,
        "/":1,
        "+":2,
        "-":2,
        }
        result=""
        for i in data:
            if i=="+" or i=="-" or i=="*" or i=="/" or i=="^":
                if len(stack.stack)>=1:
                    last=stack.stack[-1]
                    
                    if last!="(" and priority[last]<=priority[i]:
                        result+=last
                        stack.pop()
                        stack.push(i)
                    else:
                        stack.push(i)
                else:
                    stack.push(i)
            elif i=="(":
                stack.push(i)
            elif i==")":
                while len(stack.stack)>=1:

                    i=stack.stack[-1]
                    stack.pop()
                    if i=="(":
                        break
                    result+=i
            else:
                result+=i
        while len(stack.stack)>=1:

            i=stack.stack[-1]
            stack.pop()
            
            result+=i
        print("Infix Expression :",data)
        print("Postfix Expression :",result)
        
        

 





stack=Stack()
choice=1
while choice!=0:
    
    choice=int(input())
    
    if choice==1:
        data=int(input())
        stack.push(data)
    elif choice==2:
        stack.pop()
    elif choice==3:
        stack.isEmpty()
    elif choice==4:
        stack.isFull()
    elif choice==5:
        stack.display()
    elif choice==7:
        string=input("Enter postfix expression")
        stack.eval_postfii(string)
    elif choice==8:
        string=input("Enter infix expression")
        stack.infix_to_postfix(string)
    elif choice==0:
        break
    else:
        print("Wrong Input")