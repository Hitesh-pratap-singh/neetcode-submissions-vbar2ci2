class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)
        max_length = 1
        temp_length = 1
        print(sorted_nums)
        i=1
        while i < len(sorted_nums):
            print(sorted_nums[i], sorted_nums[i-1])
            print(temp_length, max_length)
            if sorted_nums[i] == sorted_nums[i-1]+1:
                temp_length+=1
            elif sorted_nums[i] == sorted_nums[i-1]:
                i+=1
                continue
            else:
                max_length = max(max_length, temp_length)
                temp_length = 1
            i+=1

        return max(max_length, temp_length)