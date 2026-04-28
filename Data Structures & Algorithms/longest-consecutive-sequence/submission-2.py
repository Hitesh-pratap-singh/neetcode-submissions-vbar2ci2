class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        s = set(nums)
        print(s)

        max_length = 1
        temp_length = 1
        for i in s:
            if i-1 in s:
                temp_length+=1
            else:
                max_length=max(max_length, temp_length)
                temp_length = 1

        return max(max_length, temp_length)