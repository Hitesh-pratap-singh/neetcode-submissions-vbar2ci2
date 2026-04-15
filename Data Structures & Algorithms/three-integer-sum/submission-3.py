class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sorted = sorted(nums)
        seen = set()
        # print(nums_sorted)
        for i in range(len(nums_sorted)):
            left = i+1
            right = len(nums_sorted)-1
            while left < right:
                total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                seen_str = str(nums_sorted[i])+str(nums_sorted[left])+str(nums_sorted[right])
                # print(seen_str, i, left, right)
                if total == 0:
                    if  seen_str not in seen:
                        result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                        seen.add(seen_str)
                    left+=1
                    right-=1
                if total < 0:
                    left+=1
                if total > 0:
                    right-=1
            # print(seen)
        return result