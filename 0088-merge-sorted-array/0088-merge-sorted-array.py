class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_len = m + n
        i, j = 0, 0
        result = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        result.extend(nums1[i:m])
        result.extend(nums2[j:n])

        nums1[:total_len] = result
        return nums1
                
        
            
        