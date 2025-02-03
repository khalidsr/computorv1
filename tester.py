import subprocess
import sys
from colorama import Fore, Style
import difflib

class TestCase:
    def __init__(self, input_str, expected_output):
        self.input = input_str
        self.expected_output = expected_output

def run_test(executable, test_case):
    try:
        result = subprocess.run(["python3", executable, test_case.input], capture_output=True, text=True)
        return result
    except Exception as e:
        print(f"Failed to run test: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tester.py [mandatory|bonus]")
        sys.exit(1)

    directory = sys.argv[1]
    executable = f"./{directory}/main.py"

    tests = [
        TestCase(
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
            "Reduced form: - 9.3 * X^2 + 4 * X^1 + 4 * X^0 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\nx1 = (-1*4 - √164.8) / (2*-9.3)\n   = -16.837445228704972 / -18.6\n   = 0.905239\nx2 = (-1*4 + √164.8) / (2*-9.3)\n   = 8.83744522870497 / -18.6\n   = -0.475131"
        ),
        TestCase(
            "5 * X^0 + 4 * X^1 = 4 * X^0",
            "Reduced form: 4 * X^1 + 1 * X^0 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*1 / 4\n  = -1 / 4\n  = -0.250000"
        ),

        TestCase (
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
             "Reduced form: - 9.3 * X^2 + 4 * X^1 + 4 * X^0 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\nx1 = (-1*4 - √164.8) / (2*-9.3)\n   = -16.837445228704972 / -18.6\n   = 0.905239\nx2 = (-1*4 + √164.8) / (2*-9.3)\n   = 8.83744522870497 / -18.6\n   = -0.475131"
       ),
        TestCase (
            "5 * X^0 + 4 * X^1 = 4 * X^0",
             "Reduced form: 4 * X^1 + 1 * X^0 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*1 / 4\n  = -1 / 4\n  = -0.250000"
       ),
        TestCase (
            "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
             "Reduced form: - 5.6 * X^3 + 0 * X^2 - 6 * X^1 + 5 * X^0 = 0\nPolynomial degree: 3\nThe polynomial degree is strictly greater than 2, I can't solve."
       ),
        TestCase (
            "42 * X^0 = 42 * X^0",
             "Reduced form: 0 * X^0 = 0\nPolynomial degree: 0\nAny real number is a solution."
       ),
        TestCase (
            "5 * X^0 = 5 * X^0",
             "Reduced form: 0 * X^0 = 0\nPolynomial degree: 0\nAny real number is a solution."
       ),
        TestCase (
            "4 * X^0 = 8 * X^0",
             "Reduced form: - 4 * X^0 = 0\nPolynomial degree: 0\nNo solution."
       ),
        TestCase (
            "5 * X^0 = 4 * X^0 +7 * X^1",
             "Reduced form: - 7 * X^1 + 1 * X^0 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*1 / -7\n  = -1 / -7\n  = 0.142857"
       ),
        TestCase (
            "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0+ 1 * X^1",
             "Reduced form: 3 * X^2 + 12 * X^1 + 4 * X^0 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\nx1 = (-1*12 - √96) / (2*3)\n   = -21.79795897113271 / 6\n   = -3.632993\nx2 = (-1*12 + √96) / (2*3)\n   = -2.2020410288672885 / 6\n   = -0.367007"
       ),
        TestCase (
            "6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0+ 1 * X^1",
             "Reduced form: 5 * X^2 + 10 * X^1 + 5 * X^0 = 0\nPolynomial degree: 2\nDiscriminant is 0, the solution is:\nx = -1*10 / (2*5)\n  = -10 / 10\n  = -1.000000"
       ),
        TestCase (
            "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0+ 0 * X^1",
             "Reduced form: 3 * X^2 + 3 * X^1 + 4 * X^0 = 0\nPolynomial degree: 2\nDiscriminant is strictly negative, the two complex solutions are:\nx1 = -1*3/(2*3) + √abs(-39)/2*3\n   = -0.500000 - 1.040833𝒊\nx2 = -1*3/(2*3) - √abs(-39)/2*3\n   = -0.500000 + 1.040833𝒊"
       ),

        TestCase (
            "2 * X^2 + 3 * X^1 + 1 = 0",
             "Reduced form: 2 * X^2 + 3 * X^1 + 1 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\nx1 = (-1*3 - √1) / (2*2)\n   = -4 / 4\n   = -1.000000\nx2 = (-1*3 + √1) / (2*2)\n   = -2 / 4\n   = -0.500000"
       ),
        TestCase (
            "4 * X + 5 = 0",
             "Reduced form: 4 * X + 5 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*5 / 4\n  = -5 / 4\n  = -1.250000"
       ),
        TestCase ( 
            "5 = 5",
             "Reduced form: 0 * X^0 = 0\nPolynomial degree: 0\nAny real number is a solution."
       ),
        TestCase ( 
            "0 * X^2 + 3 * X^1 + 4 = 0",
             "Reduced form: 0 * X^2 + 3 * X^1 + 4 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*4 / 3\n  = -4 / 3\n  = -1.333333"
       ),
        TestCase (
            "3 * X^2 + 2 * X^1 + 1 = 3 * X^2 + 2 * X^1 + 1",
             "Reduced form: 0 * X^0 = 0\nPolynomial degree: 0\nAny real number is a solution."
       ),
        TestCase ( 
            "-2 * X^2 - 4 * X^1 - 6 = 0",
             "Reduced form: - 2 * X^2 - 4 * X^1 - 6 = 0\nPolynomial degree: 2\nDiscriminant is strictly negative, the two complex solutions are:\nx1 = -1*-4/(2*-2) + √abs(-32)/2*-2\n   = -1.000000 - 1.414214𝒊\nx2 = -1*-4/(2*-2) - √abs(-32)/2*-2\n   = -1.000000 + 1.414214𝒊"
       ),
        TestCase ( 
            "3 * X^2 - 2 * X^1 + 5 = 2 * X^2 + 3 * X^1 - 4",
             "Reduced form: 1 * X^2 - 5 * X^1 + 9 = 0\nPolynomial degree: 2\nDiscriminant is strictly negative, the two complex solutions are:\nx1 = -1*-5/(2*1) + √abs(-11)/2*1\n   = 2.500000 - 1.658312𝒊\nx2 = -1*-5/(2*1) - √abs(-11)/2*1\n   = 2.500000 + 1.658312𝒊"
       ),

        TestCase ( 
    
            "5 = 3",
             "Reduced form: 2 = 0\nPolynomial degree: 0\nNo solution."
       ),

        TestCase ( 

            "X^3 + X^2 + X + 1 = 0",
             "Reduced form: 1 * X^3 + 1 * X^2 + 1 * X + 1 = 0\nPolynomial degree: 3\nThe polynomial degree is strictly greater than 2, I can't solve."
       ),

        TestCase ( 

            "0.5 * X^2 + 1.5 * X^1 + 0.75 = 0",
             "Reduced form: 0.5 * X^2 + 1.5 * X^1 + 0.75 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\nx1 = (-1*1.5 - √0.75) / (2*0.5)\n   = -2.3660254037844384 / 1\n   = -2.366025\nx2 = (-1*1.5 + √0.75) / (2*0.5)\n   = -0.6339745962155614 / 1\n   = -0.633975"
       ),
        TestCase (
            "5 + 4 * X + 1 * X^2= 1 * X^2",
             "Reduced form: 4 * X + 5 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*5 / 4\n  = -5 / 4\n  = -1.250000"
       ),
        TestCase (
            "5 + X + 1 * X = 3 * X",
             "Reduced form: - 1 * X + 5 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*5 / -1\n  = -5 / -1\n  = 5.000000"
       )
    ]

    for index, test_case in enumerate(tests):
        result = run_test(executable, test_case)
        if result is not None:
            output_str = result.stdout.strip()
            if output_str.strip() == test_case.expected_output.strip():
                print(f"{Fore.GREEN}Test {index + 1} passed{Style.RESET_ALL} \n{test_case.expected_output}\n")
            else:
                print(f"{Fore.RED}Test {index + 1} failed{Style.RESET_ALL}")
                print(f" Expected:\n{test_case.expected_output}")
                print(f" Got:\n{output_str}\n")

                # Show detailed differences
                diff = difflib.ndiff(test_case.expected_output.splitlines(), output_str.splitlines())
                print("\n".join(diff))
            # if output_str == test_case.expected_output:
            #     print(f"{Fore.GREEN}Test {index + 1} passed{Style.RESET_ALL} \n{test_case.expected_output}\n")
            # else:
            #     print(f"{Fore.RED}Test {index + 1} failed{Style.RESET_ALL}")
            #     print(f" Expected:\n{test_case.expected_output}")
            #     print(f" Got:\n{output_str}\n")

if __name__ == "__main__":
    main()

