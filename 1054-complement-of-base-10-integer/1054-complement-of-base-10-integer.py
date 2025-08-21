class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        temp=n
        count=0
        while n:
            count+=1
            n>>=1
        ones_c="1"*count
        dup=int(ones_c,2)
        res=temp^dup
        return res
                