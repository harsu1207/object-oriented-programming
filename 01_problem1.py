'''Create a class “Programmer” for storing information of few programmers working at
Microsoft'''


class programmer:
    company = "Microsoft"

    def __init__(self,name, salary,pin):
        self.name= name
        self.salary= salary
        self.pin= pin

a = programmer("Harshit",120000000,245304)        
print(a.name , a.salary, a.pin, a.company)
    
