# Python code to create a new file and write the solution to it

def create_file_with_solution():
    solution_code = """
def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10
    return x == reverted_number or x == reverted_number // 10
    """

    with open('6.palindrome-number.py', 'w') as f:
        f.write(solution_code)

create_file_with_solution()