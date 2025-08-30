class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        l=[2,3,5,7,11,13,17,19,23,29]
        ans=0
        for i in range(left,right+1):
            r_s=i
            count=0
            while r_s!=0:
                a=r_s&1
                if a==1:
                    count+=1
                r_s>>=1
            if count in l:
                ans+=1
        return ans
                