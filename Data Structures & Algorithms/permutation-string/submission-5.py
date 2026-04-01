class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1>n2:
            return False

        s1Count = Counter(s1)

        
        for i in range(n2-n1+1):
            if Counter(s2[i:i+n1]) == s1Count:
                return True
        return False        

    def Counter(s: str) -> tuple:
        arr_s1 = [0]*26
        for char in s:
            arr_s1[ord(char) - ord('a')]+=1

        return tuple(arr_s1)
