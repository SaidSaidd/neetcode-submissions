class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()

        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        # Brute force method
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        nums.sort()
        if len(nums) == 0 or len(nums) == 1:
            return False
        n = nums[1]
        for n in range(1,len(nums)):
            if nums[n] == nums[n - 1]:
                return True
        return False
        