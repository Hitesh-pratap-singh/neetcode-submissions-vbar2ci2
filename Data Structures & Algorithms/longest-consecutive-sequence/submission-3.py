class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        s = set(nums)
        print(s)
        max_length = 1
        for i in s:
            temp_length = 1
            if i-1 not in s:
                j = i
                flag = True
                while flag:
                    if j+1 in s:
                        temp_length += 1
                    else:
                        flag = False
                    j+=1
                max_length = max(max_length, temp_length) 

        return max_length