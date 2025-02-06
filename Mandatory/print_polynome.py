from solve_equation import firstDegre


def format_number(n):
    """Format a number to remove trailing .0 if it's an integer."""
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

def ReprintPolynome(res, cst):

    terms = []
    
    # if cst != 0:
    terms.append(f"{format_number(cst)} * X^0")
    for exp in sorted(res.keys()):
        coeff = res[exp]
        # if coeff == 0:
        #     continue  

        coeff_str = format_number(coeff)
        
        if coeff >= 0:
            sign = "+"
        else:
            sign = "-"
            coeff_str = format_number(abs(coeff))
        
        if exp == 0:
            term = f"{sign} {coeff_str}"
        elif exp == 1:
            term = f"{sign} {coeff_str} * X^1"
        else:
            term = f"{sign} {coeff_str} * X^{exp}"
        
        terms.append(term)

    if not terms:
        terms.append("0")
    polynome = " ".join(terms)
    
    print(f"Reduced form: {polynome} = 0")


def printError():
    print("Please enter valid syntax for polynomials")
    exit(1)


def ReduceEquationTwo(res, bigC):

    nonzero_terms = {k: v for k, v in res.items() if v != 0}


    maximum = max(nonzero_terms.keys(), default=0)

    ReprintPolynome(res, bigC)
    print(f'Polynomial degree: {maximum}')


    if maximum == 0:
        if bigC != 0:
            print("No solution.")
        else:
            print("Any real number is a solution.")
        exit(1)

    if maximum > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        exit(1)

    if maximum == 1:
        print("The solution is:")
        print(round(firstDegre(res, bigC), 6))

    return maximum
