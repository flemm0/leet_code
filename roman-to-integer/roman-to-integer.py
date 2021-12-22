class Solution:
    def romanToInt(self, s: str) -> int:
        my_list = []
        for i in range(len(s)):
            if s[i] == 'M':
                my_list.append(1000)
            elif s[i] == 'D':
                my_list.append(500)
            elif s[i] == 'C':
                my_list.append(100)
            elif s[i] == 'L':
                my_list.append(50)
            elif s[i] == 'X':
                my_list.append(10)
            elif s[i] == 'V':
                my_list.append(5)
            elif s[i] == 'I':
                my_list.append(1)

        for i in range(len(my_list)-1):
            if my_list[i] < my_list[i+1]:
                my_list[i] = -my_list[i]
        return(sum(my_list))