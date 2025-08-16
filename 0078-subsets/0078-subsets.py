class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        tot_set=1<<n
        res=[]
        for i in range(tot_set):
            ans=[]
            for j in range(n):
                lf_shift=1<<j
                if i&lf_shift!=0:
                    ans.append(nums[j])
            res.append(ans)
        return res
        