from solve_equation import firstDegre


def format_number(n):
    """Format a number to remove trailing .0 if it's an integer."""
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

def ReprintPolynome(res, cst):

    terms = []
    
    if cst != 0:
        terms.append(f"{format_number(cst)} * X^0")
    
    for exp in sorted(res.keys()):
        coeff = res[exp]
        if coeff == 0:
            continue  

        coeff_str = format_number(coeff)
        
        if coeff > 0:
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


def ReduceEquationTwo(res,bigC):
    if len(res) == 0:
        print("Any real number is a solution")
        exit(0)
    maximum = max(res.keys())
    if res[maximum]:
        if maximum > 2:
            print('Polynomial degree: '+ str(maximum))
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            exit(1)
        elif maximum <= 2:
            ReprintPolynome(res, bigC)
            print('Polynomial degree: ' + str(maximum))
            if maximum == 1:
                print("The solution is:")
                print(firstDegre(res, bigC)) 
    return maximum
            