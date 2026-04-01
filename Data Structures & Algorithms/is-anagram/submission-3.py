class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict_s = {}
        # dict_t = {}

        # if len(s) != len(t):
        #     return False
        

        # for char in s:
        #     dict_s[char]=dict_s.get(char, 0)+1

        # for char in t:
        #     dict_t[char]=dict_t.get(char, 0)+1  
     
        # for char in t:
        #     if dict_t.get(char) != dict_s.get(char):
        #         return False
            
        # return True   

        dict_s = {}
        dict_t = {}

        if len(s)!=len(t):
            return False

        for i in range (len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1


        for i in range (len(s)):
            if dict_s.get(s[i]) != dict_t.get(s[i]):
                return False

        return True    