#Define some functions
#Represent binary number in one's complement
def ones_complement(binary_number):
    ones =""
    for digit in binary_number:
        if digit =="0":
            ones+="1"
        else:
            ones+="0"
    return ones
#Represent binary number in two's complement
def twos_complement(binary_number):
    twos=""
    #First:calculate ones complement
    ones = ones_complement(binary_number)
    #Second:add 1 to the one’s complement to get twos complement
    carry=1
    twos=""
    for value in reversed(ones):
        if value =="0"and carry==1:
            twos="1"+twos
            carry=0
        elif value =="1"and carry==1:
            twos="0"+twos
        else:
            twos=value+twos
    return twos
#Addition of two binary numbers
def binary_addition(binary_Num1, binary_Num2):
    add=""
    carry = 0
    #Ensure two binary numbers have the same len by padding with leading 0s
    if len(binary_Num1) > len(binary_Num2):
        max_len = len(binary_Num1)
    else:
        max_len = len(binary_Num2)
    binary_Num1 = binary_Num1.zfill(max_len)
    binary_Num2 = binary_Num2.zfill(max_len)
    for i in range(len(binary_Num1) - 1, -1, -1):
        bart_sum=int(binary_Num1[i])+int(binary_Num2[i]) + carry
        add=str(bart_sum % 2)+add
        carry=bart_sum // 2
    if carry != 0:
        add="1"+add
    return add
#Subtraction of two binary numbers
def binary_subtraction(binary_Num1, binary_Num2):
 #check that frist number bigger than second number
        while int(binary_Num2) > int(binary_Num1):
            binary_Num2 = input("please enter number less than the first: ")
  # Ensure two binary numbers have the same len by padding with leading 0s
        if len(binary_Num1) > len(binary_Num2):
           max_len = len(binary_Num1)
        else:
           max_len = len(binary_Num2)
        binary_Num1=binary_Num1.zfill(max_len)
        binary_Num2=binary_Num2.zfill(max_len)
        result=''
        borrow=0
        for digit1,digit2 in zip(binary_Num1[::-1], binary_Num2[::-1]):
            digit1=int(digit1)
            digit2=int(digit2)
            digit1-=borrow
            sub=digit1-digit2
            if sub <0:
                sub+=2
                borrow=1
            else:
                borrow=0
            result=str(sub)+ result
        if borrow==1:
          result="1"+result
        return result
#Start the program
#Binary calculator
while True:
    #Menu 1
    print("Binary Calculator")
    print("A) Insert new numbers \nB)Exit")
    # Ask the user what he wants to do in the program
    choice = input("please select an option (A/B): ").upper()
    #Check of menu1
    #A condition
    if choice.upper() =="A":
        #Get user input
        number1 = input("please insert the first binary number: ")
        #Define valid values
        valid_values = set("01")
        #Check if the input is valid
        while not all (value in valid_values for value in number1):
            print("please enter a valid binary number")
            number1 = input("Please insert the first binary number: ")
        #Menu 2
        print("please select the operation")
        print("A) Compute one's complement \nB) Compute two's complement \nC) Addition \nD) Subtraction")
        operation = input("Enter the operation: ").upper()
        #Check of menu2
        while operation not in ["A", "B", "C", "D","a","b","c","d"]:
            print("Please select a valid operation")
            print("please select the operation")
            print("A) Compute one's complement \nB) Compute two's complement \nC) Addition \nD) Subtraction")
            operation = input("Enter the operation: ").upper()
        #A condition menu2
        if operation.upper() == "A":
            ones_comp = ones_complement(number1)
            print(f"one's complement of {number1}: ",ones_comp)
        #B condition menu2
        elif operation.upper() == "B":
            twos_comp = twos_complement(number1)
            print(f"Two's complement of {number1}:",twos_comp)
        #C,D conditions menu2
        elif operation.upper() in ("C","D"):
            number2 = input("please insert the second binary number: ")
            while not all(value in valid_values for value in number2.upper()):
                print("please enter a valid binary number")
                number2 = input("Please insert the second binary number: ")
            #C condition menu2
            if operation.upper() == "C":
                addition = binary_addition(number1,number2)
                print(f"Addition of two binary numbers {number1} and {number2}:",addition)
            #D condition menu2
            if operation.upper() == "D":
                subtraction = binary_subtraction(number1,number2)
                print(f"Subtraction of two binary numbers {number1} and {number2}:",subtraction)
    #B condition menu1
    elif choice.upper() == "B":
        print("Exit program")
        break
    #Another choice condition menu1
    else:
        print("Please select a valid choice")

# 1) Noran Mohamed Mokhtar    ID:20230451
# 2) Salma Yasser Saied       ID:20230172
# 3) Sama Abd El-Naser Osman  ID:20230176
