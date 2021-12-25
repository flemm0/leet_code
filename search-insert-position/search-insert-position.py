class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        
        if target > nums[-1]:
            idx = len(nums)
        elif target in nums:
            while nums[idx] != target:
                idx += 1
        else:
            while nums[idx] < target:
                idx += 1
        
        return(idx)
            