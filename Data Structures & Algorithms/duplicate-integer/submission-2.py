class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq_table = {}
        # for num in nums:
        #     if num in freq_table:
        #         freq_table[num] = freq_table[num]+1
        #     else:
        #         freq_table[num] = 1
        #     # print(freq_table)

        
        # for key, value in freq_table.items():
        #     if value > 1:
        #         return True

        # updated_nums = sorted(nums)

        # itr = 1;

        # while itr < len(updated_nums):
        #     if updated_nums[itr] == updated_nums[itr-1]:
        #         return True
        #     itr+=1

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False