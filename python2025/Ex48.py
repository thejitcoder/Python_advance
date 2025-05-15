# Inheritence 
class A:
    def x1(self):
        print(1)

class B(A):
    def x2(self):
        print(2)

class C(B):
    def x3(self):
        print(3)

ob = C()
ob.x1()  # From class A
ob.x2()  # From class B
ob.x3()  # From class C

