class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = True
        string = str(x)
        reverse_str = string [::-1]
        for i in range(len(string)):
            if string[i] == reverse_str[i]:
                pass
            else:
                flag = False
        return(flag)
            