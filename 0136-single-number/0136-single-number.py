class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        elem_dict = {}
        for element in nums:
            if element in elem_dict:
                elem_dict[element]+=1
            else:
                elem_dict[element]=1
        for key, value in elem_dict.items():
            if value ==1:
                return key
                
            