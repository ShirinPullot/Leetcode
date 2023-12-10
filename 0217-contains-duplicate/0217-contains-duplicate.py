class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums)==0 or len(nums)==1:
        #     return False
        # else:
            num_dict = {}
            for num in nums:
                if num in num_dict:
                    return True
                else:
                    num_dict[num]=1
        