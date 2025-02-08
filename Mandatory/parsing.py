import re
from print_polynome import printError

def pars(arg):
    
    if arg.find('X') == -1:
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

import re

def parsUltraPlus(terms):
    coefficients = []
    exponents = []
    constants = []
    is_right_side = False  # Tracks which side of the equation we're on

    # Regex to match polynomial terms
    term_pattern = re.compile(r"([+-]?\s*\d*\.?\d*)\*?X(\^(\d+))?|([+-]?\s*\d+\.?\d*)")

    for term in terms:
        for match in term_pattern.finditer(term):
            coef, _, exp, constant = match.groups()

            if coef is not None:  # Term contains 'X'
                coef = coef.replace(" ", "")  # Remove spaces
                coef = float(coef) if coef not in ["", "+", "-"] else float(coef + "1")
                exp = int(exp) if exp else 1  # Default exponent is 1
                if is_right_side:
                    coef *= -1  # Invert sign if on the right side of '='
                coefficients.append(coef)
                exponents.append(exp)
            elif constant is not None:  # Standalone constant term
                constant = float(constant.replace(" ", ""))
                if is_right_side:
                    constant *= -1  # Invert sign if on the right side of '='
                constants.append(constant)

        is_right_side = True  # Switch to right side after first pass

    return coefficients, exponents, constants
