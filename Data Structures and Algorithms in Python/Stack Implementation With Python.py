stack = []
while True:
    print("Press 1 for PUSHING onto stack")
    print("Press 2 for POPPING form stack")
    print("Press 3 for EXITING the Program")
    print("Press 4 for REVERSING the string")

    options = input("What action do you want to perform?: ")
    if options == "3":
        print("Program has ENDED")
        break

    if options == "1":
        c = input("What do you want to INSERT?: ")
        stack.append(c)
        print(stack)

    if options == "2":
        if stack!=[]:
            stack.pop()
            print(stack)
        else:
            print("The Stack is empty!")

    if options == "4":
        if stack!=[]:
            d = stack.pop()[::-1]
            print(d)

    else:
        print("Please choose a CORRECT option")
