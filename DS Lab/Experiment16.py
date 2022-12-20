print("""Choose an option:
1:Insert
2:Preorder traversal
3:Inorder traversal
4:Postorder traversal
0:Exit
""")

class Node:
    def __init__(self,d):
        self.data=d
        self.right=None
        self.left=None
class BinaryTree:
    def Insert():
        d=int(input("Enter data (press -99 for None): "))
        if d == -99:
            return None
        else:
            Newnode=Node(d)
            print("Enter left of:",Newnode.data)
            Newnode.left=B.Insert()
            print("Enter right of: ",Newnode.data)
            Newnode.right=B.Insert()
            return Newnode
    def Preorder(root):
        
        if root is not None:
            print(root.data,end="->")
            B.Preorder(root.left)
            B.Preorder(root.right)
            

        

    def Inorder(root):
        if root is not None:
            B.Inorder(root.left)
            print(root.data,end="->")
            B.Inorder(root.right)

    
    def Postorder(root):
        
        if root is not None:
            B.Postorder(root.left)
            B.Postorder(root.right)
            print(root.data,end="->")



B=BinaryTree
choice=1
while choice!=0:
    choice=int(input("Choose an option"))

    if choice==1:
        B.Insert()
    elif choice==2:
        print("Preorder traversal: \n")
        B.Preorder(root)
        print("\n")
    elif choice==3:
        print("Inorder Traversal: \n")
        B.Inorder(root)
        print("\n")
    elif choice==4:
        print("Postorder traversal:")
        B.Postorder(root)
        print("\n")
    elif choice==0:
        break
    else:
        print("Invalid input")