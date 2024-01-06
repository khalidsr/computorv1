import re

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
                exponent = parts[i][1][2:]
                if coefficient:
                    sign = '+' if i == 0 or parts[i-1] == '+' else '-'
                    rslt = float(sign + coefficient)
                    if j == 1:
                        rslt *= -1
                    coefficients.append(rslt)
                else:
                    coefficients.append('+' if i == 0 or parts[i-1] == '+' else '-')
                exponents.append(exponent)
            elif parts[i].isdigit():
                sign = '+' if i == 0 or parts[i-1] == '+' else '-'
                rst = float(sign + parts[i])
                if j == 1:
                    rst *= -1
                constants.append(rst)
            i +=1
        j+=1
    return coefficients, exponents, constants

def ReduceEquationTwo(res):
    arr = []
    for i in res.keys():
        arr.append(i)
    print(arr)
    maximum = max(arr)
    print(maximum)
    
    # index = exponents.index(maximum)
    # if coefficients[index]:
    #     if int (maximum) <= 2:
    #         print('Polynomial degree:', maximum)
    #     else:
    #         print("The polynomial degree is strictly greater than 2, I can't solve.")
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
                res[key] += value
            else:
                res[key] = value
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
        print("Please enter valid syntax for polynomials")
        exit(1)

word = arg.split("=")
if len(word) == 2:
    if len(word[0]) == 0 or len(word[1]) == 0 :
        print("Please enter valid syntax for polynomials")
        exit(1)

coefficients, exponents,const = parsUltraPlus(word)

res = ReduceEquation(coefficients,exponents)
ReduceEquationTwo(res)
# bigC = big_c(const)
# print(bigC)



# print("Coefficients:", coefficients)
# print("Exponents:", exponents)
# print("Const:", const)

