'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get
fare information of train running under Indian Railways.'''
import random
class train:
    def __init__(self,TrainNo,):
        self.TrainNo = TrainNo
    
    def book(self):
        print(f"Your Train is book, Train number is {self.TrainNo}")

    def getstatus(self,fro,to):
        print(f"Your train {self.TrainNo} from{fro} to {to} is on time")

    def fair(self,fro,to):
        print(f"Your train no {self.TrainNo} from {fro} to {to} fair is :{random.randint(222,5555)}") 


a = train(256395) 
a.book()   
a.getstatus("Hapur","Meerut") 
a.fair("Hapur", "Meerut")       
        
        