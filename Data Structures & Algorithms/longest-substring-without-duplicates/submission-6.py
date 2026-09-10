class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        max_list = []

        for letter in s:
            if letter not in stack:
                stack.append(letter)
            else:
                max_list.append(len(stack))

                index = stack.index(letter)
                stack = stack[index + 1:]
                stack.append(letter)

        max_list.append(len(stack))

        return max(max_list) if max_list else 0