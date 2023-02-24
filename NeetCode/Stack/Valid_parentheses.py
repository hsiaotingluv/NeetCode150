class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # dict = {'(':')', '{':'}', '[': ']'}

        # for char in s:
        #     if char in dict:
        #         stack.append(char)
        #     elif not stack or dict[stack.pop()] != char:
        #         return False
            
        # return len(stack) == 0

        result = True
        stack = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in ['(', '{', '[']:
                print(c)
                stack.append(c)
            else:
                if (len(stack) == 0):
                    return False
                
                prev = stack.pop()
                if (c == ')' and prev != '('):
                    return False
                if (c == '}' and prev != '{'):
                    return False
                if (c == ']' and prev != '['):
                    return False
        
        return len(stack) == 0
    
print(Solution().isValid("()[]{}"))
