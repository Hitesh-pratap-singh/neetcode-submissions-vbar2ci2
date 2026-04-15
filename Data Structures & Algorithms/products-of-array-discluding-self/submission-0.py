class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mult = {}
        right_mult = {}
        result = []

        for i in range(len(nums)):
            if i == 0:
                left_mult[i] = nums[i]
            else:
                left_mult[i] = nums[i]*left_mult[i-1]

        for i in range(len(nums), 0, -1):
            if i == len(nums):
                right_mult[i-1] = nums[i-1]
            else:
                right_mult[i-1] = nums[i-1]*right_mult[i]

        for i in range(len(nums)):
            if i == 0:
                result.append(right_mult[i+1])
            elif i == len(nums)-1:
                result.append(left_mult[i-1])
            else:
                prod = left_mult[i-1]*right_mult[i+1]
                result.append(prod)

        return result