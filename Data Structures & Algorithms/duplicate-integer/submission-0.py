class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for num in nums:
            if num in new_set:
                print(f"Duplicate found: {num}")
                return True
            new_set.add(num)
        print(f"Duplicate not found in {nums}: {new_set}")    
        return False