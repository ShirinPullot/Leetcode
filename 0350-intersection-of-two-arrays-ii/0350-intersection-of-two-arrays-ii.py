class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =[]
        len_num1= len(nums1)
        len_num2= len(nums2)  
        if len_num2<=len_num1:
            for  element in nums2:
                if element in nums1:
                    result.append(element)
                    nums1.remove(element)
        if len_num2>len_num1:
            for  element in nums1:
                if element in nums2:
                    result.append(element)
                    nums2.remove(element)
        return result

        
                    
        