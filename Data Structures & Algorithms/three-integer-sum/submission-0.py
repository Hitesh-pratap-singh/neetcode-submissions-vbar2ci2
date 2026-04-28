class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)):
            left = i+1
            right = len(nums_sorted)-1

            while left < right:
                total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]

                if total == 0:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                
                left+=1
                right-=1

        return result