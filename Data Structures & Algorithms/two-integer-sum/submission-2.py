class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # result = []
        # while i < len(nums):
        #     j = i + 1;
        #     while j < len(nums):
        #         if nums[i]+nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        #             break
        #         j+=1
        #     i+=1

        idx_table = {}
        result = []
        for index, num in enumerate(nums):
            idx_table[num] = index

        print(idx_table)

        i = 0
        while i < len(nums):
            
            if target-nums[i] in idx_table:
                return [i, idx_table[target-nums[i]]]

            i+=1

        return []