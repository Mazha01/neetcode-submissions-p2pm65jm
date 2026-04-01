class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        # dict_anagram = {}

        # for str in strs:
        #     sortedStr = "".join(sorted(str))
        #     if sortedStr in dict_anagram:
        #         dict_anagram.get(sortedStr).append(str)
        #     else:
        #         new_group = [str]
        #         dict_anagram[sortedStr] = new_group


        # for v in dict_anagram.values():
        #     output.append(v)

        # return output

        hash_str = {}

        for str in strs:
            key  = [0] * 26
            for char in str:
              index = ord(char) - ord('a')
              key[index]+=1
            key = tuple(key)  
            if key in hash_str:
                hash_str[key].append(str)
            else:
                 arr = [str]
                 hash_str[key] = arr

        return list(hash_str.values())
