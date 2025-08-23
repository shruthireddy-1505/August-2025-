class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"
        a1=int(a,2)
        b1=int(b,2)
        add=a1+b1
        res=""
        while add!=0:
            r=add%2
            res+=str(r)
            add//=2
        return res[::-1]
                