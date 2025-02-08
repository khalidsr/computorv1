from solve_equation import firstDegre

def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return f"{int(n)}" 
    else:
        return f"{n}"
    
def ReprintPolynome(res, cst):
    terms = []

    if cst != 0:
        terms.append((cst, f"{format_number(abs(cst))}"))

    for exp in sorted(res.keys(), reverse=True):
        coeff = res[exp]
        if coeff == 0:
            continue 

        coeff_str = format_number(abs(coeff))
        sign = "+" if coeff > 0 else "-"

        if exp == 0:
            term = f"{coeff_str}"
        elif exp == 1:
            term = f"{coeff_str} * X" if coeff_str != "1" else "X"
        else:
            term = f"{coeff_str} * X^{exp}" if coeff_str != "1" else f"X^{exp}"

        terms.append((sign, term)) 

    if not terms:
        print("Reduced form: 0 = 0")
        return  

    polynome = terms[0][1] 
    for sign, term in terms[1:]:
        polynome += f" {sign} {term}"

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

            