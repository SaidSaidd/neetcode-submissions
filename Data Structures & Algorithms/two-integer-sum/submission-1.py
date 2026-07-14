class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res_index = []
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res_index.append(i)
        #             res_index.append(j)
        # return res_index
        
        seen_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff  in seen_dict:
                return [seen_dict[diff], i]
            seen_dict[nums[i]] = i


            
