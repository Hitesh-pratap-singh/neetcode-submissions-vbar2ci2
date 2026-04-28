class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        s = set(nums)
        # print(s)

        max_length = 1

        for i in s:
            if i-1 in s:
                max_length+=1

        return max_length