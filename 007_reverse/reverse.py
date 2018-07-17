class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        flag = x < 0
        if flag:
            x = -x
        while x != 0:
            x, pop = divmod(x, 10)
            if flag:
                if rev > 2147483648 // 10 or (rev == 2147483648 and pop > 8):
                    return 0
            else:
                if rev > 2147483647 // 10 or (rev == 2147483647 and pop > 7):
                    return 0
            rev = rev * 10 + pop
        if flag:
            rev = -rev
        return rev
