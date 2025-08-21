class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        while x or y:
            x1=x&1
            y1=y&1
            if x1!=y1:
                count+=1
            x>>=1
            y>>=1
        return count
                