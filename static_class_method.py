import math

class complex:
    cnt = 0 # static variable 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        complex.cnt+=1
      
    @property
    def real(self):
        return self.x

    @real.setter
    def real(self,x):
        self.x=x 

    @property
    def imag(self):
        return self.y

    @real.setter
    def imag(self,y):
        self.y=y 

    def __add__(self,z):
        return complex(self.x+z.x, self.y+z.y)

    @staticmethod
    def mod(z):
        return math.sqrt(z.x**2+z.y**2)

    @classmethod 
    def from_tuple(cls,tup):
        return cls(tup[0],tup[1])

    def __str__(self):
        sign = '+' if self.y>=0 else '-'
        return "{} {} i{}".format(math.fabs(self.x),sign,math.fabs(self.y))



# use of @property set get
z = complex(1,2)
t = complex(3,4)
print(z)
z.real=10
print(z)


# use of @classmethod
v = complex.from_tuple((3,5))
print(v)
print("number of instances:",v.cnt)

# use of __add__
print(z+v)

# use of static method
print(complex.mod(z))
    
