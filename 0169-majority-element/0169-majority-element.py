class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for no in nums:
            if no in num_dict:
                num_dict[no]+=1
            else:
                num_dict[no]=1
        num_len = len(nums)
        for key, value in num_dict.items():
            if value > (num_len/2):
                return key
            
                
                
            
        