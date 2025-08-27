class Solution:
    def reverseBits(self, n: int) -> int:
        if n==0:
            return 0
        s=""
        while n!=0:
            and_op=n&1
            s+=str(and_op)
            n>>=1

        temp=s
        temp=s[::-1]
        res=int(temp,2)
        l=res.bit_length()
        sub=32-l
        add=s+"0"*sub
        ans=int(add,2)
        return ans
        