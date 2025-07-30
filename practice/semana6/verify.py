# This small program help to create and verify a password that into the user
import sys # this library is for exit to program
# verifyNumber::This function help verify to string content one digit, in the variable passed how param, this function return a bool
def verifyNumber(text): 
    number_exist = False # number_exist is a variable type bool
    for word in text: # Iterate text for found the digit
        if word.isdigit(): # if word is a digit number to variable number_exist change value to True
            number_exist = True
    return number_exist # return the value of number_exist
# verifyPassword::This function request two params and help to determinated if this params is equals, this function return a bool. 
def verifyPassword(password, password_confirm):
    if password_confirm == password:
        return True
    return False

count = 0 # this variable help to count to error
sesson = False # this variable is bool for status task
password = "" # this variable is type string
text_input = "" # this variable is type string
    
while sesson == False and count < 2: # this while execute the main instruccion
    text_input = input("Ingresa la contraseña:\n") # Request to user into a password
    res = verifyNumber(text_input) # res storage the answer to call to function verifyNumber and pass how param the value in text_input.
    while res == False and count < 2: # this while be execute if the variable res is false and it counter is minus to two
        count += 1 # add one to counter
        text_input = input("La contraseña debe tener almenos 1 numero.\nIngresa una contraseña:\n") # remmember to user that is necesary one number in the password
        res = verifyNumber(text_input) # recall to function verifyNumber
    if res == True: # if variable res is true then program request into the password again for verify that this is equals
        password = text_input
        text_input = input("Ingresa nuevamente la contraseña:\n")
        res = verifyPassword(password, text_input) # call to the function verifyPassword and storage the answer in res
    while res == False and count < 2: # while res is equal to false and counter is minus to two, execute the next code
        count += 1 # add one to counter
        text_input = input("Las contraseñas no coinciden.\nPorfavor ingresa la misma contraseña:\n") # notify to user that your password is diferente
        res = verifyPassword(password, text_input) # call to function verifyPassword and storage the answer in res
    if res == True: # if res is true then sesson change your value to true
        sesson = True

if sesson == True: # if sesson is true, notify to user that all right, and your password succesfull
    print("Contraseñas coinciden con éxito.")
elif count > 1: # if count is major to one, notifye to user that him had three wrong
    print("Fallaste en 3 intentos, por seguridad intentelo de nuevo más tarde.")
sys.exit()