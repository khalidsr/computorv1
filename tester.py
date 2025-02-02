import subprocess
from colorama import Fore, Style

class TestCase:
    def __init__(self, input_str, expected_output):
        self.input = input_str
        self.expected_output = expected_output

def run_test(executable, test_case):
    try:
        result = subprocess.run([executable, test_case.input], capture_output=True, text=True)
        return result
    except Exception as e:
        print(f"Failed to run test: {e}")
        return None

def main():
    tests = [
        TestCase(
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
            "Reduced form: - 9.3 * X^2 + 4 * X^1 + 4 * X^0 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\nx1 = (-1*4 - √164.8) / (2*-9.3)\n   = -16.837445228704972 / -18.6\n   = 0.905239\nx2 = (-1*4 + √164.8) / (2*-9.3)\n   = 8.83744522870497 / -18.6\n   = -0.475131"
        ),
        TestCase(
            "5 * X^0 + 4 * X^1 = 4 * X^0",
            "Reduced form: 4 * X^1 + 1 * X^0 = 0\nPolynomial degree: 1\nThe solution is:\nx = -1*1 / 4\n  = -1 / 4\n  = -0.250000"
        ),
    ]

    executable = "./computor"

    for index, test_case in enumerate(tests):
        result = run_test(executable, test_case)
        if result is not None:
            output_str = result.stdout.strip()
            if output_str == test_case.expected_output:
                print(f"{Fore.GREEN}Test {index + 1} passed{Style.RESET_ALL} \n{test_case.expected_output}\n\n{Fore.GREEN}.....{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}Test {index + 1} failed{Style.RESET_ALL}")
                print(f" Expected:\n{test_case.expected_output}")
                print(f" Got:\n{output_str}\n\n{Fore.RED}.....{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()