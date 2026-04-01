class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_hash = {}
        for num in nums:
            f_hash[num] = f_hash.get(num, 0) + 1 

        res = []
        count = 0
        for key, value in sorted(f_hash.items(), key=lambda x: x[1], reverse=True):
            if len(res) == k:
              return res
            res.append(key) 
        return res