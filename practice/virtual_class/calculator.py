import sys
# This program help to user for calculate basic operationts aritmetics
# This progran is conformated for 8 functions.
def text_explain(params, operation_sign): # text_explain is a function dedicated to show in screen the operation pass to pass
        text="" # text is a variable for concatenate the result of operation
        sign="" # sign is a variable for storage the sign in the param received
        match operation_sign: # whit match i can use varius options how switch in c++ or js, operation_sign is the chosen operation
                # asign the sign to operation to sign
                case 1:
                    sign = "+"
                case 2:
                    sign="-"
                case 3:
                    sign="*"
                case 4:
                    sign="/"
        for value in params: # whit this bucle iterate the list params received how param
                if value.startswith("-"): # if value in params init whit the sign - then wrap the value between parentheses and add to sign respect to chosen operation
                        text += "(" + value + ")" + sign
                elif value.startswith("+"): # if value in params init whit the sign + then wrap the value between parentheses and add to sign respect to chosen operation 
                        text += "(" + value + ")" + sign
                else: # only add to sign respecto to chosen operation
                        text += value + sign
        text = text.strip(sign) # remove the last sign in the string
        text += " = " # add the sign equal to end string
        return text # return the string completed

def add(value_one, value_two): # this function only make the operation add, request to params value one and value two
        return value_one + value_two

def rest(value_one, value_two):# this function only make the operation rest, request to params value one and value two
        return value_one - value_two

def multiplication(value_one, value_two):# this function only make the operation multiplication, request to params value one and value two
        return value_one * value_two

def division(params):# this function only make the operation division, request to params value one and value two
        return int(params[0]) / int(params[1])

def calc(params, operation): # this function select the action to execute and return to string whit the result to chosen operation
        res = 0 # this variable storage result of operation
        count = 0 # this counter is for determinate if is the first param 
        for value in params: # whit this bucle i iterate in the list params 
                value = int(value) # change value to type int
                if count == 0: # if count is equal to 0 then res value now is the value of the first param
                    res = value
                else: # if count not is 0 then with match select to chosen operation
                    match operation:
                            case 1: # the user chosen add operation then recall to function add and pass params, res that is the first value and value that is the second value
                                print("SUMANDO...")
                                res = add(res, value)
                            case 2: # the user chosen add operation then recall to function rest and pass params, res that is the first value and value that is the second value
                                print("RESTANDO...")
                                res = rest(res, value)
                            case 3: # the user chosen add operation then recall to function multiplication and pass params, res that is the first value and value that is the second value
                                print("MULTIPLICANDO...")
                                res = multiplication(res, value)
                            case 4: # the user chosen add operation then recall to function division and pass params.
                                print("DIVIDIENDO...")
                                res = division(params)
                count += 1 # increment count on one
        return  text_explain(params, operation) + str(res) # recall to function text_explain and concatenated the result to calc

def verify_number(count): # verify_number is a function for determinated if the param into is or not one number
        value = input(f"Ingresa el parametro {count}:\n")
        try: # try change the type of variable of string to int
            int(value)
        except ValueError: # if is try failed then recall to recursive mode to own function
            value = False
            while value == False:
                print("Porfavor ingresa numeros.")
                value = verify_number(count)
        return value
        
def use(): # use is my function init this function show the option to user and help to user for your simple use
        option = 0 # this variable is for storage to chosen operation select for the user
        values = [] # this list storage the diferents params into the user 
        count = len(values) # count variable storage the number of elements in the list values
        count = count + 1 # add one to count because values to init is 0
        value = 0 # value variable storage the input of users
        menu = "1.suma\n2.resta\n3.multiplicacion\n4.division" # menu storage the options to check
        while option > 4 or option < 1: # this bucle execute if option is major to four and minor to one.
                status_warning = False # the variable status_warning is alert for show in screen the message warning
                warning = "Elige una opcion valida del menu."
                try: # try storage in option the input to user and try change the input in type int
                    print(menu)
                    option = int(input("Bienvenido a tu calculadora, seleccione la operacion que desea realizar:\n"))
                except ValueError: # if try, failed then show the message warning and change the status_warning to True
                        print(f"{warning}")
                        status_warning = True
                if option > 4 or option < 1 and status_warning != True: # if try is success and status_warning is diferent to True show in the screen the message warning and the menu
                            print(f"{warning}\n{menu}")
        value = verify_number(count) # storage the result of verify_number in value
        values.append(value) # add a new element to list values
        count = count + 1 # add one to count
        value = verify_number(count) #repeat the last pass
        values.append(value)
        if option < 4 and option > 0: # if option is minor to 4 and major to 0, program ask to user if wish add a new element to the list
                while input("Desea agregar otro parametro.\ny:SI\nn:NO\n") == "y":
                        count = count + 1 # if answer is y then add one to count
                        value = verify_number(count) # storage the return in value
                        values.append(value) # add a new element to list values
        print(calc(values, int(option))) # show on the screen the operation.

if __name__ == "__main__": 
        use() # recall to the function use
        while input("¿Desea realizar otra operación?:\ny:SI\nn:NO\n") == "y": # if the input is diferent to y then the bucle end
                use() # recall to the function use
        print("Hasta pronto.") # end to program message
        sys.exit() # use sys for end the program