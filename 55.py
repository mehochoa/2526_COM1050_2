class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_val=0
        for i in range (len(nums)):
            if i>max_val:
                return False
            max_val=max(max_val, i+nums[i])
        return True