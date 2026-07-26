class Solution:
    def isValid(self, s: str) -> bool:

        # For the string create a stack of each time an open parentheses is used
        # then popping the stack if the sibling parentheses is used
        # if the stack is empty it is true, else we return false

        pairs  = {'(': ')', '[': ']', '{': '}'}
        stack  = []

        for char in s:
            # if char is an opener
            if char in pairs:
                stack.append(char)
            # else the char is a closer
            else:
            # if we have something in the stack
                if stack:
                    if pairs[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack





        # stack = []

        # for char in s:
        #     if char == "(" or char == "[" or char == "{":
        #         stack.append(char)
        #     else:
        #         if not stack:
        #             return False
        #         if char == ")":
        #             if stack.pop() != "(":
        #                 return False
        #         if char == "]":
        #             if stack.pop() != "[":
        #                 return False
        #         if char == "}":
        #             if stack.pop() != "{":
        #                 return False
        # return not stack




