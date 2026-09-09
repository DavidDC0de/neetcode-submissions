class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        solution = []

        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] > target:
                end -= 1

            else:
                start += 1

        if start < end:
            return [start + 1, end + 1]

        else:
            return [end+1, start + 1]
