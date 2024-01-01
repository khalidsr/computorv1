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
            i += 1
        j+=1
    return coefficients, exponents, constants

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

coefficients, exponents,const = parsUltraPlus(word)
print("Coefficients:", coefficients)
print("Exponents:", exponents)
print("Const:", const)

# for coeff, exp in zip(coefficients, exponents):
#     print( coeff )
#     print("----------")
#     print(exp)
#     print("----------")


# while i < len(word):
#     print (parsUltraPlus(word[i]))
#     i+=1

    
    
    
    
# print(pars(arg))

# print("Reduced form: " + name)
# print("Polynomial degree: 2 " + name)
# print("Discriminant is strictly positive, the two solutions are: " + name)