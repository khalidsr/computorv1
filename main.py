import re
def printError():
    print("Please enter valid syntax for polynomials")
    exit(1)

def parsUltraPlus(terms):
    coefficients = []
    exponents = []
    constants = []
    j = 0

    for term in terms:
        i = 0
        parts = re.split(r'([+-])', term)
        
        while i < len(parts):
            if 'X' in parts[i]:
                parts[i] = parts[i].split("*")
                coefficient = parts[i][0]
                if len(parts[i]) != 2:
                    print(len(parts[i]))
                    printError()
                if len(parts[i][1]) > 2 and parts[i][1][2:].isdigit():
                    exponent = int(parts[i][1][2:])
                else:
                    printError()

                if coefficient:
                    sign = '+' if i == 0 or parts[i-1] == '+' else '-'
                    rslt = float(sign + coefficient)
                    if j == 1:
                        rslt *= -1
                    coefficients.append(rslt)
                else:
                    coefficients.append('+' if i == 0 or parts[i-1] == '+' else '-')
                exponents.append(exponent)
            elif parts[i].replace('.', '', 1).isdigit():
                sign = '+' if i == 0 or parts[i-1] == '+' else '-'
                rst = float(sign + parts[i])
                if j == 1:
                    rst *= -1
                constants.append(rst)
            i += 1
        j += 1

    return coefficients, exponents, constants

def ReduceEquationTwo(res):
    arr = []
    for i in res.keys():
        if res[i] == 0:
            del res[i] 
    maximum = max(res.keys())
    if res[maximum]:
        if maximum > 2:
            print('Polynomial degree:', maximum)
            print("The polynomial degree is strictly greater than 2, I can't solve.")
        elif maximum <= 2:
            print('Polynomial degree:', maximum)
        
        else:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            
def big_c(const):
    big_c = 0
    for i in const:
        big_c += int (i)
    return big_c

def  ReduceEquation(coefficients,exponents):
    hold_coeff = []
    
    res = {}
    for  key in exponents:
        for value in coefficients:
            if key in res:
                res[int (key)] += value
            else:
                res[int (key)] = value
            coefficients.remove(value)
            break
    return res
    # seen_elements = set()
    # repeated_elements = set()
    # for element in exponents:
    #     if element in seen_elements:
    #         repeated_elements.add(element)
    #         hold_coeff.append(exponents.index(element))
    #         print(hold_coeff)
    #     else:
    #         seen_elements.add(element)

    # if repeated_elements:
    #     print("Some elements are repeated in the list:", repeated_elements)
    # else:
    #     print("No elements are repeated in the list.")
    
def checkDelta(res,cst):
    delta = res
    for i in res.keys():
        if i == 0:
            cst+=res[i]
            del res[i]
            #
    delta = (res[1]*res[1]  - (4 * res[2] * cst))
    print(delta) 
    return delta
    
def pars(arg):

    count = arg.count('=')

    if not  count <= 1:
        return False
    if not arg.find("^-") == -1:
        return False
    for i in arg:
        if not  (i.isdigit() or i.isspace() or i == "X" or i == '*' or i == "+" or i == "-" or 
                 i == "^" or i == "/" or i == "." or i == "="):
            return False     
    return True

arg = input("./computer ")
arg = arg.replace(" ", "")
if pars(arg) == False:
    printError()

word = arg.split("=")
if len(word) == 2:
    if len(word[0]) == 0 or len(word[1]) == 0 :
        printError()

coefficients, exponents,const = parsUltraPlus(word)

res = ReduceEquation(coefficients,exponents)
ReduceEquationTwo(res)
bigC = big_c(const)
delta = checkDelta(res,bigC)

# print(bigC)



# print("Coefficients:", coefficients)
# print("Exponents:", exponents)
# print("Const:", const)

