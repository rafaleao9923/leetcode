class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

if __name__ == "__main__":
    print(Solution.isPalindrome(121))  # True
    print(Solution.isPalindrome(-121))  # False (negative numbers are not palindromes)
    print(Solution.isPalindrome(10))    # False

"""
Imagine you have a number, like 121. A palindrome is a special kind of number that reads the same forward and backward, like the word "level" or the number 121. So, the function is checking if a given number is a palindrome or not.

Here's a simple explanation of the function:

1. **Handle special cases:**
   - If the number is negative, it's not a palindrome because palindromes are always positive.
   - If the number ends with a zero (except for zero itself), it's also not a palindrome because numbers like 120 or 30 are not the same backward.

2. **Reverse the number:**
   - Create a new number by reading the original number backward. For example, if the original number is 121, the reversed number would be 121 in this case.

3. **Compare the original and reversed numbers:**
   - Check if the original number is the same as the reversed number. If they are the same, it means the number is a palindrome!
"""