class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        else:
            current=2
            for next in range (2,len(nums)):
                if nums[next] != nums[current-2]:
                    nums[current]=nums[next]
                    current+=1
            return current