import re

def msqrt(y):
    
    i = 1
    while 1:
        i += 1
        if i * i >= y:
            break

    x = (i + y / i) / 2
    return x


def ReprintPolynome(res, cst):
    for i in res:
        print(str(i.values()) + " * X^" + str(i.keys()), end=" ")
    print(str(cst))



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
    maximum = max(res.keys())
    if res[maximum]:
        if maximum > 2:
            print('Polynomial degree: '+ str(maximum))
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            exit(0)
        elif maximum <= 2:
            print('Polynomial degree: ' + str(maximum))
            if maximum == 1:
                print("The solution is:")
                print(firstDegre(res,bigC))
                
    return maximum
            
def big_c(const, res):
    big_c = 0
    for i in const:
        big_c += float (i)
    for i in res.keys():
      if i == 0:
          big_c+=res[i]
          del res[i]
    return big_c

def  ReduceEquation(coefficients,exponents):
    
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
    
def checkDelta(res,cst):
    
    delta = res
    for i in res.keys():
        if i == 0:
            cst+=res[i]
            del res[i]
    if res.get(1):
        b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    else:
        a = 0
    delta = (b*b  - (4 * a * cst))
    return delta

def twoSolution(res,delta):
    if res.get(1):
      b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    x1 = (-b - msqrt(delta))/(2*a)
    x2 = (-b + msqrt(delta))/(2*a)
    return x1,x2

def oneSolution(res):
    if res.get(1):
      b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    x = -b/(2*a)
    return x,None

def complexSolution(res,delta):
    if res.get(1):
     b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    alpha = str(-b/(2*a))
    betha = str(- msqrt(abs(delta))/(2*a))
    gamma = str(msqrt(abs(delta))/(2*a))
    if betha[0] == '-':
        x1 = alpha + " " + betha + "i"
    else:
        x1 = alpha  + " + " + betha + "i"
    if gamma[0] == '-':
        x2 = alpha + " " + gamma + "i"
    else:
        x2 = alpha + " + " + gamma + "i"

    return x1,x2
    
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

def firstDegre(res,bigC):

    x = - (bigC/res[1])
    return x


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
bigC = big_c(const,res)
maximum = ReduceEquationTwo(res)

ReprintPolynome(res,bigC)

delta = checkDelta(res,bigC)
if maximum == 2:
    if delta > 0:
        x1,x2 = twoSolution(res,delta)
        print("Discriminant is strictly positive, the two solutions are:")
        print(round(x1,6))
        print(round(x2,6))
    elif delta == 0:
        x = oneSolution(res)
        print("Discriminant is 0 , the solution is :")
        print(x)
    else:
       x1, x2 = complexSolution(res,delta)
       print("Discriminant is strictly negative, the two imaginary solutions are:")
       print(x1)
       print(x2)

# print(bigC)




