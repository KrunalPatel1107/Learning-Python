print("Welcome to the Greatest Calculator Ever!!!")

operation = str(input("What would you like to do? "
                  "Type sum or sub? : "))

if operation == "sum":
    firstnum = input("First number: ")
    secondnum = input("Second number: ")
    sum = float(firstnum) + float(secondnum)
    print("Sum: " + str(sum))
elif operation == "sub":
    firstnum = input("First number: ")
    secondnum = input("Second number: ")
    sub = float(firstnum) - float(secondnum)
    print("Sub: " + str(sub))
else:
    print("You jerk!")
