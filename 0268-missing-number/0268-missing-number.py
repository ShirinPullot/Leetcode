class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mini = 0
        maxi =  max(nums)
        new_list = []
        if mini not in nums:
            return mini
        else:
            for i in range(mini, maxi+2):
                new_list.append(i)
            for elem in new_list:
                if elem not in nums:
                    return elem
            
        