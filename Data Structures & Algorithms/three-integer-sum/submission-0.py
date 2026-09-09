class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_2 = nums[::]
        nums_2.sort()

        return_list = []

        for i, a in enumerate(nums_2):
            if a > 0:
                break

            if i > 0 and a == nums_2[i-1]:
                continue

            l, r = i + 1, len(nums_2) -1 
            while l < r:
                t = a + nums_2[l] + nums_2[r]
                if t > 0:
                    r -= 1

                elif t < 0:
                    l += 1

                else:
                    return_list.append([a, nums_2[l], nums_2[r]])
                    l += 1
                    r -= 1
                    while nums_2[l] == nums_2[l-1] and l < r:
                        l += 1

        return return_list