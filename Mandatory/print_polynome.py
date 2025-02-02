from solve_equation import firstDegre


def ReprintPolynome(res, cst):
    print("Reduced form: " + str(cst) + " * X^0",end=' '),
    for i in res:
        if res[i] > 0:
            print("+ " + str(res[i]) + " * X^" + str(i),end=' '),
        else:
            print(str(res[i]) + " * X^" + str(i),end=' '),
    print(" = 0")


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
            