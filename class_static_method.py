


class planet:
    exo    = False  # class variables
    gasous = True  # 

    def __init__(self, name, matter_status ):        
        self.name   = name    # instance variable
        self.gasous = matter_status

    def display(self):
         print("Hi I am an 'instance' method, I can acces both class and instance variables")
         print(self.name, self.gasous, planet.gasous)   

    @classmethod
    def print_class_vars(cls):
         print("Hi I am a class method, I can  acces class variables only") 
         print("Exo planet: {}, Gasous: {}".format(cls.exo, cls.gasous))

    @staticmethod 
    def greet():
         print("Hi I am a static method, can't acces class nor instance variables")   


earth = planet('earth',False)

earth.display()
print()
planet.print_class_vars()
print()
planet.greet()    
print("\n--------------------------------------------------------------")
# can also call class/static methods from instance 
earth.print_class_vars()
print()
earth.greet()




