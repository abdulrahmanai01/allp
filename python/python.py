'''
a=int(input("Enter the Value:"))
b=input("Choose square or cube:")
b=(b.lower())
if "square" in b:
    c=a*a;
    print("The square Value is:",c)
elif "cube" in b:
    c=a*a*a;
    print("The cube Value of is:",c)
else:
    print("Please choose the correct option.")
'''
'''
a=input("enter the value you want")
a=int(a)
for b in range (1,11):
  print(a,"x",b,"=",a*b)
'''
'''
n=int(input("enter the number."))
if(n%2)==0:
    print("the given number is Even.")
else:
    print ("the given number is odd")
'''
'''
n=float(input("Enter the number."))
if n>0:
    print("You enterded positive number.")
elif n==0:
    print("you enterded zero.")
else:
    print("you enterded negative number.")
'''
'''
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Selkect operator.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if 
    '''

class gameofthrones() :
    name = " "
    house = " "
    def Targaryen (self):
        print("Daenerys enter the Dragon stone")
    def Stark(self):
        print("jon snow enjoy in the castle block")
    def Lanisters(self):
        print("Tiryan secon hand for kings landing")
    def Barathion(self):
        print("Robbert death in storm's end   ")
Daenerys =gameofthrones() 
jon = gameofthrones()
Tiryan = gameofthrones()
Robbert = gameofthrones()
Daenerys.name = input("Enter name")
Daenerys.Birthyear = "2001"
jon.name = input("Enter name")
jon.Birthyear = "2000"
Tiryan.name = input("Enter name")
Tiryan.Birthyear = "1987"
Robbert.name = input("Enter name")
Robbert.Birthyear = "1990"
print(Daenerys.name)
print("Birthyear:",Daenerys.Birthyear)
Daenerys.Targaryen()

print(jon.name)
print("Birthyear : ",jon.Birthyear)
jon.Stark()

print(Tiryan.name)
print("Birthyear: ",Tiryan.Birthyear)
Tiryan.Lanisters()

print (Robbert.name)
print("Birthyear: ",Robbert.Birthyear)
Robbert.Barathion()
    