class Solution:
    def isValid(self, s: str) -> bool:

        # For the string create a stack of each time an open parentheses is used
        # then popping the stack check if 

        stack = []
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')':
                    if stack.pop() != '(':
                        return False   
                if char == ']':
                    if stack.pop() != '[':
                        return False
                if char == '}':
                    if stack.pop() != '{':
                        return False
        return not stack