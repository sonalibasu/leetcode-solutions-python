"""
https://leetcode.com/problems/two-sum/
Complexity - O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            xb = target - nums[i]
            if xb in ref:
                return [i, ref[xb]]
            ref[nums[i]] = i
            
        