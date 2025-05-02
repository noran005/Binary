#Define some functions
#Convert decimal to binary
def decimal_to_binary(decimal_number):
    i, bin_value = 0, 0
    dec_digits = "0123456789"
    for digit in str(decimal_number):
        if digit not in dec_digits:
            return
    decimal_number=int(decimal_number)
    while decimal_number != 0:
        remainder = decimal_number % 2
        bin_value += remainder * (10 ** i)
        decimal_number //= 2
        i += 1
    return bin_value
#Convert binary to decimal
def binary_to_decimal(binary_number):
   dec,i=0,0
   bin_digits="0,1"
   for digit in str(binary_number) :
       if digit not in bin_digits:
           return
   binary_number =int(binary_number)
   while binary_number >0:
          r= binary_number%10
          dec+=(r*(2**i))
          binary_number=binary_number//10
          i+=1
   return dec
#Convert decimal to octal
def decimal_to_octal(decimal_number):
    dec_digits = "0123456789"
    for digit in str(decimal_number):
        if digit not in dec_digits:
            return
    i, octal = 0, 0
    base = 8
    while decimal_number != 0:
        remainder = decimal_number % base
        octal += remainder * 10 ** i
        decimal_number //= base
        i += 1
    return octal
#Convert octal to decimal
def octal_to_decimal(octal_number):
    dec, i = 0, 0
    oct_digits = "01234567"
    for digit in octal_number:
        if digit not in oct_digits:
            return
    octal_number = int(octal_number)
    while octal_number > 0:
        r = octal_number % 10
        dec += (r * (8 ** i))
        octal_number = octal_number // 10
        i += 1
    return dec
#Convert hexadecimal to decimal
def hexadecimal_to_decimal(hex_value):
    decimal_value = 0
    hex_digits = "0123456789ABCDEF"
    hex_value = hex_value.upper()
    for digit in hex_value:
        decimal_value = decimal_value * 16 + hex_digits.index(digit)
    return decimal_value
#Convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal_value):
    hex_digits = "0123456789ABCDEF"
    hex_value = ""
    while decimal_value > 0:
        remainder = decimal_value % 16
        hex_value = hex_digits[remainder] + hex_value
        decimal_value = decimal_value // 16
    return hex_value
#Convert number
def convert_number(number, user_choice_from_base, user_choice_to_base):
    if user_choice_from_base == "A":
        decimal_value = (number)
    elif user_choice_from_base == "B":
        decimal_value = binary_to_decimal(number)
    elif user_choice_from_base == "C":
        decimal_value = octal_to_decimal(number)
    elif user_choice_from_base == "D":
        decimal_value = hexadecimal_to_decimal(number)

    if user_choice_to_base == "A":
        result = decimal_value
    elif user_choice_to_base == "B":
        result = decimal_to_binary(decimal_value)
    elif user_choice_to_base == "C":
        result = decimal_to_octal(int(decimal_value))
    elif user_choice_to_base == "D":
        result = decimal_to_hexadecimal(int(decimal_value))
    return result
#Number converter
#Starting program
while True:
    #Menu 1
    print("numbering system converter")
    # Ask the user what he wants to do in the program
    print("A) insert a new number \nB) Exit program")
    user_choice = input("Please enter your choice (A/B): ").upper()
    #Check of menu1
    #A condition
    if user_choice == "A":
        #Get user input
        number = input("Please insert a number: ")
        #Define valid characters
        valid_values = set("0123456789ABCDEFabcdef")
        #Check if the input is valid
        while not all (value in valid_values for value in number.upper()):
            print("please enter a valid number")
            number = input("Please insert a number: ")
        #Menu 2
        print("please enter the base you want to convert from :")
        print("A) Decimal \nB) Binary \nC) Octal \nD) Hexadecimal ")
        user_choice_from_base = input("please enter your choice A/B/C/D :").upper()
        #Check of menu2
        while user_choice_from_base not in ["A", "B", "C", "D","a","b","c","d"]:
            print("please select a valid choice.")
            print("please enter the base you want to convert from :")
            print("A) Decimal \nB) Binary \nC) Octal \nD) Hexadecimal ")
            user_choice_from_base = input("please enter your choice A/B/C/D : ")
        #Menu 3
        print("please select the base you want to convert to:")
        print("A) Decimal \nB) Binary \nC) Octal \nD) Hexadecimal")
        user_choice_to_base = input("please enter your choice A/B/C/D: ").upper()
        #Check of menu3
        while user_choice_to_base not in ["A", "B", "C", "D","a","b","c","d"]:
            print("please select a valid choice.")
            print("please enter the base you want to convert to :")
            print("A) Decimal \nB) Binary \nC) Octal \nD) Hexadecimal ")
            user_choice_to_base = input("please enter your choice A/B/C/D : ")
        result = convert_number(str(number), user_choice_from_base.upper(), user_choice_to_base.upper())
        print(f"Result: {result}\n")
    #B condition
    elif user_choice == "B":
        print("Exit program")
        break
    #Another choice condition
    else:
        print("Please select a valid choice")

# 1) Noran Mohamed Mokhtar    ID:20230451
# 2) Salma Yasser Saied       ID:20230172
# 3) Sama Abd El-Naser Osman  ID:20230176
