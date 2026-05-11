import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack to put the values 
        rpn_stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                operator = token
                
                # Check for previous two values
                

                if rpn_stack:
                    second_num = rpn_stack.pop()
                else:
                    continue
                if rpn_stack:
                    first_num = rpn_stack.pop()
                else:
                    continue

                result = 0
                if operator == '+':
                    result = int(first_num) + int(second_num)
                if operator == '-':
                    result = int(first_num) - int(second_num)
                if operator == '*':
                    result = int(first_num) * int(second_num)
                if operator == '/':
                    result = math.trunc(int(first_num) / int(second_num))
                
                rpn_stack.append(result)
                
            else:
                rpn_stack.append(int(token))
        
        return rpn_stack[0]