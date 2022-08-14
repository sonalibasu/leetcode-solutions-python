"""
Link: https://leetcode.com/problems/maximum-subarray/

Time complexity - O(n) (optimized from brute force double for loop approach)
"""

class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        max_sum = current_sum = arr[0]
        for num in arr[1:]:
            current_sum = max((current_sum+num), num)
            max_sum = max(current_sum, max_sum)
        return max_sum