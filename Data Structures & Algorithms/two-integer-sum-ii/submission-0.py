class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        left = 0
        right = len(numbers)-1

        while left<right:
            data = numbers[left]+numbers[right]
            if data == target:
                return[left+1, right+1]
            if data > target:
                right-=1
                continue
            if data < target:
                left+=1
                continue

        return result