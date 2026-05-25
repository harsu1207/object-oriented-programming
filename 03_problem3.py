'''Add a static method in problem 2, to greet the user with hello'''





class calculator:

    def __init__(self, n):
        self.n = n

    def square(self): #This is for square
        print(f"The square is : {self.n*self.n}")


    def cube(self): #This is for cube
        print(f"The cube is : {self.n*self.n*self.n}") 

      
    def squareroot(self):# This is for square root 
        print(f"The root is: {self.n**1/2}") 

    @staticmethod
    def hello():
        print("Hello user") 

num = int(input("Enter your number: "))        

a = calculator(num)
a.hello()
a.square()
a.cube()
a.squareroot() 