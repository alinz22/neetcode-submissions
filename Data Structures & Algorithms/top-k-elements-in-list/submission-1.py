class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creates the bucket for every freq it could be up until the max
        freq = [[] for i in range(len(nums) + 1)]

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, c in count.items():
            freq[c].append(num)

        output = []
        #start at end of freq until begin decrement by 1
        for i in range(len(freq) - 1, 0, -1):
            #go through each number in the bucket
            for num in freq[i]:
                output.append(num)
            # once K return
            if len(output) == k:
                return output

            