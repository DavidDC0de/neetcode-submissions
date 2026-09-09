class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        volume_dict = []

        while l < r:
            max_area = (r-l) * min(heights[l], heights[r])
            volume_dict.append([max_area, r,l])
            if heights[l] < heights[r]:
                l += 1
                
            elif heights[l] > heights[r]:
                r -= 1

            else:
                l += 1
                r -= 1

        volume_dict.sort()
        max_area, l, r = volume_dict[-1]

        return max_area