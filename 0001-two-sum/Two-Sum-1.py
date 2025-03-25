from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums) - 1):
            for idx2 in range(idx + 1, len(nums)):
                if nums[idx] + nums[idx2] == target:
                    return [idx, idx2]

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))