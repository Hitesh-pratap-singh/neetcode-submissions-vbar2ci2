class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_table = {}
        # for num in nums:
        #     freq_table[num] = freq_table[num]+1

        
        # for key, value in freq_table:
        #     if value > 1:
        #         return True

        updated_nums = sorted(nums)

        itr = 1;

        while itr < len(updated_nums):
            if updated_nums[itr] == updated_nums[itr-1]:
                return True
            itr+=1

        return False