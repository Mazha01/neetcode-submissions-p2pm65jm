class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. считаем частоты
        f_hash = {}
        for num in nums:
            f_hash[num] = f_hash.get(num, 0) + 1 

        # 2. создаем buckets
        matrix = [[] for _ in range(len(nums) + 1)]
        for key, value in f_hash.items():
            matrix[value].append(key)

        # 3. идем с конца (макс частоты)
        res = []
        for i in range(len(matrix) - 1, 0, -1):
            for num in matrix[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res