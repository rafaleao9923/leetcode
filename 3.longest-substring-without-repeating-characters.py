def is_valid(s, mid):
    # Count the frequency of each character in the pattern
    count = [0] * 256
    found = False

    # Stores the number of distinct characters in a substring of size mid
    distinct = 0

    for i in range(len(s)):
        count[ord(s[i])] += 1
        if count[ord(s[i])] == 1:
            distinct += 1
        if i >= mid:
            count[ord(s[i - mid])] -= 1
            if count[ord(s[i - mid])] == 0:
                distinct -= 1
        if i >= mid - 1:
            # Substring of length mid found which contains all the unique characters
            if distinct == mid:
                found = True
    return found


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        ans = float('inf')

        # Lower bound and Upper Bound for Binary Search
        low_bound = 1
        high_bound = length

        # Applying Binary Search on answer
        while low_bound <= high_bound:
            mid = (low_bound + high_bound) // 2

            # If a substring of length mid is found which contains all unique characters
            # then update low_bound, otherwise update high_bound
            if is_valid(s, mid):
                ans = mid
                low_bound = mid + 1
            else:
                high_bound = mid - 1
        return ans


# Driver code
if __name__ == "__main__":
    solution = Solution()
    for input_str in ("abcabcbb", "bbbbb", "pwwkew"):
        print("The input string is", input_str)
        length = solution.lengthOfLongestSubstring(input_str)
        print("The length of the longest non-repeating character substring is", length)
        print("-------------------------------")