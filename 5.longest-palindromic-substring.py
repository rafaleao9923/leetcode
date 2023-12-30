class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s)==0:
        #     return 0
        # maxLen=1
        # start=0
        # for i in range(len(s)):
        #     if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        #         start=i-maxLen-1
        #         maxLen+=2
        #         continue
        #     if s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        #         start=i-maxLen
        #         maxLen+=1
        # return s[start:start+maxLen]
    
        # if len(s)==0:
        #     return ""
        # maxLen=1
        # start=0
        # for i in range(len(s)):
        #     if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        #         start=i-maxLen-1
        #         maxLen+=2
        #         continue
        #     if s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        #         start=i-maxLen
        #         maxLen+=1
        # return s[start:start+maxLen]

        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            temp = expandAroundCenter(s, i, i)
            if len(temp) > len(longest):
                longest = temp

            # Even length palindrome
            temp = expandAroundCenter(s, i, i + 1)
            if len(temp) > len(longest):
                longest = temp

        return longest


if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))
    s = "cbbd"
    print(sol.longestPalindrome(s))
    s = "a"
    print(sol.longestPalindrome(s))
    s = "ac"
    print(sol.longestPalindrome(s))
    s = "bb"
    print(sol.longestPalindrome(s))