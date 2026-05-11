class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)

        # Start adding each character into a stack one by one
        stack = []
        
        for c in chars:
            if stack != []:
                if stack != [] and (c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '[') or (c == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if stack == []:
            return True
        return False
