class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {')':'(', ']':'[', '}':'{'}

        for par in s:
            if par not in my_dict:
                stack.append(par)
            else:
                if not stack or my_dict[par] != stack[-1]:
                    stack.append('*')
                    break
                if my_dict[par] == stack[-1]:
                    stack.pop()

        return(not stack)