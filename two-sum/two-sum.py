class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            val = target - nums[i]
            for j in range(i + 1, len(nums)):
                if val == nums[j]:
                    return([i, j])
