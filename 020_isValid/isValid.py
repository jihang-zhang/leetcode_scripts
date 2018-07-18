class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Linear scan after popping each pair
        # pair = ["()", "[]", "{}"]
        # length = len(s)
        # while s != "":
        #     for i in range(len(s) - 1):
        #         if s[i:i+2] in pair:
        #             s = s[:i] + s[i+2:]
        #             break
        #     if len(s) != length - 2:
        #         return False
        #     else:
        #         length -= 2
        # return True
        
        # Single linear scan
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p not in pair:
                stack.append(p)
            elif not stack or pair[p] != stack.pop():
                return False
        return not stack