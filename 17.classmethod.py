
# Python program to understand the classmethod
  
class Student:
      
    # create a variable
    name = "Geeksforgeeks"
      
    # create a function
    def print_name(self):
        print("The name is : ", self.name)
          
# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
# Student.print_name = classmethod(Student.print_name)
  
# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()
classmethod