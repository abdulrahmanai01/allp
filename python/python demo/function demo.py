def myfunction():
    a=1+2
    print(a) 
    if a==3:
        print("a is 3")
        x="welcome"
        for x1 in x:
            print(x1)
        for x2 in x.split(" "):
            print(x2)
    y= input("enter the value.").split()
    print(y)
myfunction()