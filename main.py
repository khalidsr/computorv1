import re


def parsUltraPlus(terms):
    coefficients = []
    exponents = []
    constants = []

    for term in terms:
        i =0
        parts = re.split(r'([+-])',term)
        while i < len(parts):
            if 'X' in  parts[i]:
                parts[i] = parts[i].split("*")
                coefficient = parts[i][0]
                exponent = parts[i][1]
                coefficients.append(coefficient if coefficient else 1.0)
                exponents.append(exponent)
            else:
                if parts[i].isdigit():
                    constants.append(parts[i])
                else:
                    # if i < len(parts) - 1:
                        parts[i] = parts[i+1].join(parts[i])
                        print(parts[i])
            i+=1

    return coefficients, exponents, constants


# def parsUltraPlus(terms):
#     coefficients = []
#     exponents = []
#     j = 1
#     for term in terms:
#         matches = re.findall(r'([-+]?\d*\.*\d*)\s?\*\s?X\^(-?\d+)', term)
#         for match in matches:
#             coefficient, exponent = match
#             if(j == 2):
#                 coefficients.append(-float(coefficient) if coefficient else 1.0)
#             else:
#                 coefficients.append(float(coefficient) if coefficient else 1.0)
#             exponents.append(int(exponent))
#         j+=1
#     return coefficients,exponents;

# def  parsUltraPlus(terms):
#     coefficients = []
#     exponents = []
#     j = 1
#     for term in terms:
#         matches = re.split(r'([-+])', term)
#         print(matches)
#     return coefficients, exponents

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
# def ParsUltra(arg):
#     right = arg.split("=")
#     return right
arg = input("./computer ")
arg = arg.replace(" ", "")
if pars(arg) == False:
        print("Please enter valid syntax for polynomials")
        exit(1)
# equat = ParsUltra(arg)

word = arg.split("=")


# print(word);
# word = parsUltraPlus(equat[0])
# print(word)
# print (w[0])
# i =0

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