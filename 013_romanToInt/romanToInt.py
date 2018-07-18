class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref1 = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ref2 = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        pos = 0
        result = 0
        while pos < len(s) - 1:
            if s[pos:pos+2] in ref2:
                result += ref2[s[pos:pos+2]]
                pos += 2
            else:
                result += ref1[s[pos]]
                pos += 1
        if pos == len(s) - 1:
            result += ref1[s[pos]]
        return result