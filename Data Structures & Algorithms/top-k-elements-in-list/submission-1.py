class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        
        return_list = []

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        while k > 0:
            highest_frequency = (0,0)
            for num in hash:
                if hash[num] > highest_frequency[1] and num not in return_list:
                    highest_frequency = (num, hash[num])

            return_list.append(highest_frequency[0])
            k -= 1

        return return_list

        
        