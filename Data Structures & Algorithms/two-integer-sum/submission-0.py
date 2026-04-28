class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums)-1
        
        while(left < right):
            add = nums[left] + nums[right]
            if add == target:
                break
            elif add > target:
                right -= 1
            else:
                left += 1


        return[left, right]
