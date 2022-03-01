# Simple Calculator

while True:
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))

    print("Choose an operation: " )
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choose = int(input("Enter your operation: "))

    while choose < 1:
        print ("Please choose an operation!")
        choose = int(input("Enter your operation: "))

    while choose > 4:
        print ("Please choose an operation!")
        choose = int(input("Enter your operation: "))

    if (choose == 1):
        print ("Result:", first_number + second_number)

    elif (choose == 2):
        print ("Result:", first_number - second_number)

    elif (choose ==3):
        print ("Result:", first_number * second_number)

    else:
        print ("Result:", first_number / second_number)

    use_calc = input("Use this calculator again [Y/N]? ")

    if (use_calc == "Y"):
        continue

    elif (use_calc == "N"):
        print("Thank you for using this calculator!") 
        exit()

