class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        i=0
        j=i+1
        k=j+1
        while i<n:
            if j>=n:
                break
            if nums[i]!=nums[j] and nums[i]!=nums[k]:
                break
            i=k+1
            j=i+1
            k=j+1
        return nums[i]
                