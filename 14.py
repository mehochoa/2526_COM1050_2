class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for i in range(len(strs[0])):
            cur = strs[0][i]
            for j in range(1, len(strs)): 
                if i >= len(strs[j]) or strs[j][i] != cur:
                    return result
            result += cur
        return result
