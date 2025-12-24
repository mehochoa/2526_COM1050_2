class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        left, right =0, n-1
        while left<=right:
            if nums[right]==val:
                right-=1
            elif nums[left]==val:
                nums[left], nums[right] = nums[right], nums[left]
                right-=1
            else:
                left +=1
        return left