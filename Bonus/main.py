import re

from parsing import pars, parsUltraPlus
from print_polynome import printError, ReduceEquationTwo
from reduce_polynome import  ReduceEquation, big_c
from solve_equation import checkDelta, twoSolution, oneSolution, complexSolution
# import sys 

def main():
    arg = input("./computer ")
    # arg = sys.argv[1]
    arg = arg.replace(" ","")
    arg = arg.strip('\"')
    if pars(arg) == False:
        printError()

    word = arg.split("=")
    if len(word) == 2:
        if len(word[0]) == 0 or len(word[1]) == 0 :
            printError()

    coefficients, exponents,const = parsUltraPlus(word)

    res = ReduceEquation(coefficients, exponents)

    bigC = big_c(const, res)
    maximum = ReduceEquationTwo(res, bigC)
    delta = checkDelta(res, bigC)
    if maximum == 2:
        if delta > 0:
            if res[2] != 0:
                x1,x2 = twoSolution(res, delta)
                print("Discriminant is strictly positive, the two solutions are:")
                print(round(x1, 6))
                print(round(x2, 6))
            elif res.get(1):
                x = oneSolution(res, bigC)
                print("Discriminant is 0, the solution is:")
                print(x)
        elif delta == 0:
            x = oneSolution(res, bigC)
            print("Discriminant is 0, the solution is:")
            print(x)
        else:
            x1, x2 = complexSolution(res, delta)
            print("Discriminant is strictly negative, the two complex solutions are:")
            print(x1)
            print(x2)

if __name__=="__main__":
    main()
