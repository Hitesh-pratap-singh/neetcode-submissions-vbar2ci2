class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxA = 0

        while(left < right):
            minHeight = min(heights[left], heights[right])
            tempArea = minHeight*(right - left)
            maxA = max(maxA, tempArea)
            print(minHeight, tempArea, maxA, left, right)
            if heights[left] < heights[right]:
                left += 1
            elif heights [left] > heights[right]:
                right-=1
            else:
                left+=1

        return maxA
