"""
Link: https://leetcode.com/problems/valid-parentheses/

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        complement = {'{':'}','[':']','(':')'}
        for bracket in s:
            if bracket in complement:
                stack.append(bracket)
            elif len(stack) == 0: #to prevent IndexError from empty list pop
                return False
            elif bracket != complement[stack.pop()]:
                return False
        if not stack:
            return True