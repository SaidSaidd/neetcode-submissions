class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArray = [0] * (2 * n)

        for i in range(n):
            newArray[i] = nums[i]
            newArray[i + n] = nums[i]

        return newArray
