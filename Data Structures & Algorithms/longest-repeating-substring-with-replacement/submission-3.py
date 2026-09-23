class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hash_map = {}
        res = 0
        
        while r < len(s):
            

            if s[r] not in hash_map:
                hash_map[s[r]] = 1
                r+=1

            else:
                hash_map[s[r]] += 1
                r+=1

            if len(hash_map) > 0:
                if (r-l) - max(hash_map.values()) <= k:
                    res = max((r-l), res)
                    
                else:
                    hash_map[s[l]] -=1
                    l += 1
            
        return res

            
            