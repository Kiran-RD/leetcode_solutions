def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        m = len(nums)
        res = []
        for i in range(m-2):
            left = i+1
            right = m-1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                
                sum = nums[i]+nums[left]+nums[right]
                
                if sum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
