''' Write a class “Calculator” 
capable of finding square, cube and square root of a number.'''



class calculator:

    def __init__(self, n):
        self.n = n

    def square(self): #This is for square
        print(f"The square is : {self.n*self.n}")


    def cube(self): #This is for cube
        print(f"The cube is : {self.n*self.n*self.n}") 

      
    def squareroot(self):# This is for square root 
        print(f"The root is: {self.n**1/2}") 

num = int(input("Enter your number: "))        

a = calculator(num)
a.square()
a.cube()
a.squareroot()     



    