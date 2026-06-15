class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first : strs[0]
        
        for i in range(0,lena(first)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != first[i]:
                    return first[:i]
        return first
