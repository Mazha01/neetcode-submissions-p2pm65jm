class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dict_anagram = {}

        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr in dict_anagram:
                dict_anagram.get(sortedStr).append(str)
            else:
                new_group = [str]
                dict_anagram[sortedStr] = new_group


        for v in dict_anagram.values():
            output.append(v)

        return output