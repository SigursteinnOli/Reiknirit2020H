class Node: 
    # Smiður, frumstillir d og núllstillir bendana prv og nxt
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bÃ¦tir aftast Ã¡ listann.   
    def append(self,d):
        if self.nxt is None:
            n = Node(d)
            self.nxt = n
            self.nxt.prv = self
        else:
            return self.nxt.append(d)

    # EndurkvÃ¦mt fall sem prentar listann.
    def printList(self):
        if self.nxt is None:
            print(self.data, end=" ")
        else:
            print(self.data, end=" ")
            self.nxt.printList()
                
    # EndurkvÃ¦mt fall sem athuga hvort stak d er Ã­ listanum.
    def find(self, d):
        #print(self.nxt)

        if self.data == d:
            print("True")
        elif self.nxt is None:
            print("False")
        else:
            self.nxt.find(d)

    # EndurkvÃ¦mt fall sem eyÃ°ir staki d Ãºr listanum.
    def delete(self, d):
        #Miðju
        if (self.data == d) and (self.nxt is not None) and (self.prv is not None): 
            self.prv.nxt = self.nxt
            self.nxt.priv = self.prv
        
        #Enda
        elif (self.data == d) and (self.nxt is None) and (self.prv is not None):
            self.priv.next = None
            self.priv = None

        #Byrjun
        elif (self.data == d) and (self.nxt is not None) and (self.prv is None):
            self.nxt.prv = None
            self.nxt = None

        elif self.data != d and self.nxt is None:
            print("Stak ekki í listanum")

        else:
            self.nxt.delete(d)

class DLL:
    # SmiÃ°ur, nÃºllstillir Haus listans
    def __init__(self):
        self.head = None

    # BÃ¦tir viÃ° fremst Ã¡ listann, hnÃºturinn verÃ°ur Head -> fÃ¶rum ekki Ã­ Node klasann.
    def push(self,d):
        if self.head is None:
            self.head = Node(d)
        else:
            n = Node(d)
            n.nxt = self.head
            self.head.prv = n
            self.head = n
    
    # BÃ¦tir viÃ° aftast Ã¡ listann -> kallar Ã¡ endurkvÃ¦mnt fall Ã­ Node.
    def append(self, d):
        if self.head is None:
            self.head = Node(d)
        else:
            self.head.append(d)

    # Prentar listann allan Ã¡ skjÃ¡ -> kallar Ã¡ endurkvÃ¦mt fall Ã­ Node.
    def printList(self):
        if self.head is None:
            print("Þessi listi er tómur")
        else:
            self.head.printList()
    
    # Finnur stak d Ã­ ef til -> kallar Ã¡ endurkvÃ¦mnt fall Ã­ Node.
    def find(self, d):
        if self.head is None:
            print("Listinn er tómur")
        else:
            self.head.find(d)

    # EyÃ°ir staki d Ãºr lista ef til -> kallar Ã¡ endurkvÃ¦mnt fall Ã­ Node.
    def delete(self, d):
        if self.head is None:
            print("Listinn er tómur")
        
        if self.head.data == d:
            self.head = self.head.nxt
            self.head.prv.nxt = None
            self.head.prv = None
        
        elif self.head.data == d and self.head.nxt is None:
            self.head = None
        else:
            self.head.delete(d)

# KeyrslurÃºtÃ­na
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7         
dbl.push(1)             # 1 5 7 
dbl.push(0)             # 0 1 5 7 
dbl.append(10)          # 0 1 5 7 10
dbl.printList()         
print()
print(dbl.delete(5))   # 0 1 7 10
dbl.printList() 
print()
print(dbl.find(9))    # False
print(dbl.find(7))      # True