class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs_2 = []
        str_dict = {}
        final_list = []

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)
            strs_2.append(sorted_word)

        for i in range(len(strs_2)):
            if strs_2[i] in str_dict:
                str_dict[strs_2[i]].append(i)

            else:
                str_dict[strs_2[i]] = [i]

        for word in str_dict:
            new_list = []
            for i in str_dict[word]:
                new_list.append(strs[i])
            final_list.append(new_list)
            new_list = []
            
        return final_list