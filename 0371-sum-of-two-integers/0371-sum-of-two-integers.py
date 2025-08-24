class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a<0 or b<0:
            return a+b
        while b!=0:
            add=a^b
            carry=(a&b)<<1
            a=add
            b=carry
        return a
        