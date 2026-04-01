class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_set = set()
        max_count=0
        l = 0
        r = 0
        count = 0
        max_count = 0
        while l < len(s):
            while r < len(s) and s[r] not in new_set:
                new_set.add(s[r])
                count+=1
                r+=1
            max_count = max(max_count, count)
            new_set.discard(s[l])
            l+=1
            count-=1
        return max_count   
              