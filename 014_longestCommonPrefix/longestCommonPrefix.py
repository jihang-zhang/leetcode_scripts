class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        pos = 0
        while True:
            try:
                candidate = strs[0][pos]
                for i in range(1, len(strs)):
                    if strs[i][pos] != candidate:
                        return result
                result += candidate
                pos += 1
            except IndexError:
                return result