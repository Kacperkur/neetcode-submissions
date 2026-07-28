import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        num_stack = []
        operators = {"+", "-", "*", "/"}

        for item in tokens:
            if item not in operators:
                num_stack.append(int(item))
            else:
                
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                if item == "+":
                    result = num1 + num2
                elif item == "-":
                    result = num1 - num2
                elif item == "*":
                    result = num1 * num2
                else:
                    result = int(num1 / num2)

                num_stack.append(result)
        return num_stack[0]




            

