class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1, 1]
        i = 2
        while i < n+1:
            fib.append(fib[i-2] + fib[i-1])
            i += 1
        
        return(fib[-1])