class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, number in enumerate(nums):
            key = target - number
            if key in seen:
                return [seen[key], index]
            seen[number] = index