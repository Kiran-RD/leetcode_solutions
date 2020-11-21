class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach 1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]
        
        # approach 2
        # we can improve the performance by using set which reduces look up times
#         nums_set = set(nums)
        
#         for i in nums_set:
#             if target - i in nums_set:
#                 index1 = nums.index(i)
#                 nums[index1] = None
#                 index2 = nums.index(target-i)
#                 return [index1, index2]
            
        # approach 2 using dictionary
        nums_dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                return [i, nums_dict[target - nums[i]]]
            nums_dict[nums[i]] = i
        
        
