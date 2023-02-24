class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        # import re
        # result = re.sub(r'[\W_]', '', s).lower()
        for c in s:
            if (c.isalnum()):
                result += c.lower()
        
        i = 0
        j = len(result) - 1
        isPalindrome = True

        while (i < j):
            if (result[i] != result[j]):
                return False
            else:
                i += 1
                j -= 1
        
        return isPalindrome
    
s = "A man, a plan, a canal: Panama"
solution = Solution()
result = solution.isPalindrome(s)
print(result)



