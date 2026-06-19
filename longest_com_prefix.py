class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        
        for i in range(0,len(first)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != first[i]:
                    return first[:i]
        return first
