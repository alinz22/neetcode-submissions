class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            key = target - value
            if key in seen:
                return [seen[key], index]
            seen[value] = index
