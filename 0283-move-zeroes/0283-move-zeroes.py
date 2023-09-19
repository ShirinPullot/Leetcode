class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_list = []
        while 0 in nums:
            zeros_list.append(0)
            nums.remove(0)
        nums[len(nums):] =zeros_list[:]
                
            
        