class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_depth = 0
        for i in s:
            if i == '(':
                max_depth += 1 
                count = max(max_depth, count)
            elif i == ')':
                max_depth -= 1
        return count