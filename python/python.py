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
n=float(input("Enter the number."))
if n>0:
    print("You enterded positive number.")
elif n==0:
    print("you enterded zero.")
else:
    print("you enterded negative number.")
 