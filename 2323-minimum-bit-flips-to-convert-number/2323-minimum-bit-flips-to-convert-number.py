class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res=start^goal
        ans=""
        while res!=0:
            r=res%2
            ans+=str(r)
            res//=2
        count=0
        for i in ans:
            if i=="1":
                count+=1
        return count
                