class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)< 3:
            return []
        else:
            nums.sort()
            triplet =[]
            for i in range(len(nums)-2):
                l=i+1
                r = len(nums)-1
                while l<r:
                    sum = nums[i]+nums[l]+ nums[r] 
                    if sum ==0:
                        triplet.append((nums[i], nums[l], nums[r]))
                        l+=1
                    elif sum >0:
                        r-=1
                    else:
                        l+=1
  
        return list(set(triplet))

                    