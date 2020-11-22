class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value > d:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insert(d)
        if self.value < d:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insert(d)
        if self.value == d:
            print("Þetta stak er nú þegar í listanum")

    def find(self,d):
        if self.value == d:
            print("true")
            return True

        elif self.value > d:
            if self.left is None:
                print("false")
                return False
            else:
                self.left.find(d)

        else:
            if self.right is None:
                print("false")
                return False
            else:
                self.right.find(d)


    def preOrderPrint(self):
        if self.left is not None:
            print(self.left.value)
            self.left.preOrderPrint()
        
        if self.right is not None:
            print(self.right.value)
            self.right.preOrderPrint()
        
            
    def postOrderPrint(self):
        if self.left is not None:
            self.left.postOrderPrint()
            print(self.left.value)
        
        if self.right is not None:
            self.right.postOrderPrint()
            print(self.right.value)

    def delete(self,d): 
        if self.value == d:
            print("404 Delete fall ekki fundið")

        elif self.value > d:
            if self.left is None:
                print("Talan er ekki í fallinu")
                return False
            else:
                self.left.delete(d)

        else:
            if self.right is None:
                print("Talan er ekki í fallinu")
                return False
            else:
                self.right.delete(d)

class Tree:  #-------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.root = None
    
    def insert(self,d):
        if self.root is None:
            self.root = Node(d)
        else:
            self.root.insert(d)

    def find(self,d):
        if self.root is None:
            print("tréið er tómt")
        else:
            self.root.find(d)

    def preOrderPrint(self):
        if self.root is None:
            print("Þetta tré er tómt")
        else:
            print(self.root.value)
            self.root.preOrderPrint()
        

    def postOrderPrint(self):
        if self.root is None:
            print("tréið er tómt")
        else:
            self.root.postOrderPrint()
            print(self.root.value)

    def delete(self,d):
        if self.root is None:
            print("Tréið er tómt")
        else:
            self.root.delete(d)

t = Tree()
t.insert(20)
t.insert(10)

t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)

t.preOrderPrint()
print()
t.delete(60)
t.postOrderPrint()
print()
print(t.find(1))
print(t.find(15))
