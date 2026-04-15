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
        # for index, num in enumerate(nums):
        #     idx_table[num] = index


        i = 0
        while i < len(nums):
            print(idx_table)
            if target-nums[i] in idx_table and i != idx_table[target-nums[i]]:
                return [idx_table[target-nums[i]], i]
            else:
                idx_table[nums[i]] = i

            i+=1
        
        print(idx_table)

        return []