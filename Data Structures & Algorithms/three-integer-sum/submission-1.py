class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)):
            left = i+1
            right = len(nums_sorted)-1
            seen = set()
            while left < right:
                total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                seen_str = str(nums_sorted[i])+str(nums_sorted[left])+str(nums_sorted[right])
                # print(seen_str)
                if total == 0 and seen_str not in seen:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    seen.add(seen_str)
                left+=1
                right-=1
            print(seen)
        return result