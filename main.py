import re



def parsUltraPlus(word):
    # hold = []
    # for i in word:
    #     if i.find("X") == 0:
    #         hold = word.split("X")
    #         hold.append(word)


    coefficients = []
    exponents = []
    matches = re.findall('\d+', word)
    for match in matches:

        coefficient, exponent = match
        coefficients.append(coefficient if coefficient else 1.0)
        exponents.append(exponent)
    return coefficients, exponents
    # return hold
    
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
def ParsUltra(arg):
    right = arg.split("=")
    return right
arg = input("./computer ")
arg = arg.replace(" ", "")
if pars(arg) == False:
        print("Please enter valid syntax for polynomials")
        exit(1)
equat = ParsUltra(arg)
word = equat[0].split("+")
# print (word)
i =0
coefficients, exponents = parsUltraPlus(word)
for coeff, exp in zip(coefficients, exponents):
    print("Coefficient: "+ coeff + ", Exponent: " + exp )
# while i < len(word):
#     print (parsUltraPlus(word[i]))
#     i+=1

    
    
    
    
# print(pars(arg))

# print("Reduced form: " + name)
# print("Polynomial degree: 2 " + name)
# print("Discriminant is strictly positive, the two solutions are: " + name)