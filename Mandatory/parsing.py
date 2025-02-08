import re
from print_polynome import printError

def pars(arg):
    
    if arg.find('X') == -1:
        return False
    if re.search(r'[\+\-\*/\^]=', arg):
        return False
    if re.search(r'[\+\-\*/\^]{2,}', arg):
        return False
    count = arg.count('=')
    if count != 1:
        return False
    if not arg.find("^-") == -1:
        return False
    for i in arg:
        if not  (i.isdigit() or i.isspace() or i == "X" or i == '*' or i == "+" or i == "-" or 
                 i == "^" or i == "/" or i == "." or i == "="):
            return False     
    return True

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