class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        out = []

        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for j in range(len(pos)):
            out.append(pos[j])
            out.append(neg[j])

        return out