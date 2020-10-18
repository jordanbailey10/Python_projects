class Protected:
    def __init__(self):
        self.protectedVar = 0

obj = Protected()
obj._protectedVar = 84
print(obj._protectedVar)

class Protected2:
    def __init__(self):
        self.__protected2Var = 24

    def getProtected2(self):
        print(self.__protected2Var)

    def setProtected2(self,private):
        self.Protected2 = protected2

obj = Protected2()
obj.getProtected2()
obj.setProtected2(12)
obj.getProtected2


