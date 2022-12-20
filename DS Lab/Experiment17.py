#binary search tree and searching
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binarysearchtree:
    def __init__(self):
        self.root=None
        
    def add(self,data):
        tree_node=Node(data)
        if self.root==None:
            self.root=tree_node
        else:
            if data>root.data:
                if root.right:
                    self.add(root.right)
                else:
                    root.right=tree_node
                    #traverse right
            else:
                if root.left:
                    self.add(root.left)
                else:
                        root.left=tree_node
                    #traverse left
        self.add(self.root)              
                    
    def search(self,pivot,root):
    
         if root==None:
             return "not found"
         if root.data==pivot:
             print(root.data)
             return "found"
         if pivot<root.data:
          
             return self.search(pivot,root.left)
         elif pivot>root.data:
         
             return self.search(pivot,root.right)
             
             
         
tree=binarysearchtree()
tree.add(3)
tree.add(8)
tree.add(6)
tree.add(7)
tree.add(14)
tree.add(9)
print(tree.search(14,tree.root))