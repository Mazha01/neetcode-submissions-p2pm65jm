class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # If the current subarray is already sorted, the min is nums[l]
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = l + (r - l) // 2
            res = min(res, nums[m])

            # Determine which half to discard
            if nums[m] >= nums[l]:
                # Left half is sorted; the rotation point is to the right
                l = m + 1
            else:
                # Right half is sorted; the rotation point is to the left (or is m)
                r = m - 1
                
        return res

        [2, 1]

        