#Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.

class Dog:
    def __init__(self,name="",breed="",color="",gender=""):
        self.name=name
        self.breed=breed
        self.color=color
        self.gender=gender

    def printAll(self):
        print(self.name,self.breed,self.color,self.gender)

class Person:
    def __init__(self,weight="",height=""):
        self.weight=weight
        self.height=height

    def printBMI(self):
        print("The body mass is: "+ str(self.weight/(self.height *self.height)*703 ))



class Product:
    def __init__(self,name="",price=0,quanity):
        self.name=name
        self.price=price
        self.quanity=quanity


























def main():
     #problem1()
    #problem2()
    problem3()
    # problem4()

def problem1():
    myNewdog=Dog("Juicy","shitzu","brown","female")
    myNewdog.printAll()


# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
def problem2():
    userInput=""
    while (userInput!='='):
        userInput=input("Enter another string.")

#In your main file create three Person objects. Change the weight and height of each one. Afterwards, print the BMI (body mass index) of each Person.
# If you don’t know how to calculate BMI, look at the code I provided for you.
#<strong>Hint</strong>: BMI is (weight / (height * height)) x 703. Weight is in pounds and height is in inches.
#<strong>Extra</strong>:Put the three person objects in an array and use a loop to print out their BMIs.


# def problem3():
#     newPerson1=Person(150,50)
#     newPerson2=Person(175,65)
#     newPerson3=Person(150,75)
#     newPerson1.printBMI()
#     newPerson2.printBMI()
#     newPerson3.printBMI()


# Create a class Product that represents a product sold online.
# A product has a name, price, and quantity.
 def problem4():







if __name__ == '__main__':
    main()