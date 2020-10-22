import math
from copy import deepcopy
class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y): 
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):       
        print("x:",self.x," y:",self.y)
   
    # Fall sem skilar lengd
    def lengd(self):        
        summa = (self.x**2)+(self.y**2)
        return round(math.sqrt(summa), 2)
        
    
    # Fall sem skilar hallatölu
    def halli(self):        
        return self.y / self.x
    
    # Fall sem skilar Þvervigri
    def þvervigur(self):     
        tempx = self.x
        tempy = self.y
        self.x = -tempy
        self.y = tempx
        
    '''
    
    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):   
        
    '''
    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v1):     
        top = (self.x * v1.x)+(self.y * v1.y)
        bottom = math.sqrt((self.x**2) * (v1.x**2)) + math.sqrt((self.y**2) * (v1.y**2))
        return math.degrees(math.acos(top/bottom))
        
    
    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v): 
        self.x += v.x
        self.y += v.y     
        return self.x , self.y

# Keyrsluforrit
v1 = Vigur(1,3)
v3 = v1
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = deepcopy(v1)
vþ.þvervigur()
print("Þvervigur: " , end=" ")
vþ.prenta()
'''
print("Stefnuhorn: ", v1.stefnuhorn())    
'''
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3.summa(v2)
print("Summa: " , end=" ")
v3.prenta()
