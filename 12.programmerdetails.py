class Programmer:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
    def getdetails(self):
        print(f"Employee name : {self.name}" )
        print(f"Employee id : {self.id}" )
        print(f"Employee salary : {self.salary}" )
    @staticmethod
    def greet():
        print('Thank you.')    

p = Programmer('Tanmoy' , 1158, 35450)
p.getdetails()
p.greet()



        

