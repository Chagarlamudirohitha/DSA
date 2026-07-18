class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        nums[i]=nums[0]
        for j in range(n):
            if nums[i]==nums[j]:
                continue
            else:
                i+=1
                nums[i]=nums[j]
        return i+1        

