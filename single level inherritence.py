#example-1
class one:
    a=10
    b=20
    def add(self):
        x=self.a+self.b
        print(x)
class two(one):
    def mul(self):
        y=self.a*self.b
        print(y)  


k=two()
k.add()
k.mul()
#example-2
class apple13:
    color="black"
    camera="50mp"
    storage=128
    bettery="4000mah"
    def show(self):
        print("mobile color is",self.color)
        print("moble camera is",self.camera)
        print("moble storage is",self.storage)
        print("mobile bettery is",self.bettery)

class apple14(apple13):
    storage=256
    color="sky blue"
    bettery="5000mah"
    facelock="yes"
    def show(self):
        print("mobile color is",self.color)
        print("moble camera is",self.camera)
        print("moble storage is",self.storage)
        print("mobile bettery is",self.bettery)
        print("mobile facelock is",self.facelock) 


k=apple14()
k.show()           
