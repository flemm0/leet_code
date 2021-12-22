class Solution:
    def reverse(self, x: int) -> int:
        reverse_x = str(x)[::-1].replace('-','')
        if (int(reverse_x) < -(2**31)) | (int(reverse_x) > ((2**31) - 1)):
            return(0)
        else:
            if x < 0:
                return(-int(reverse_x))
            else:
                return(int(reverse_x))