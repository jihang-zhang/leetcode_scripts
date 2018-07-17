class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            rev = 0
            y = x
            while y != 0:
                y, pop = divmod(y, 10)
                rev = rev * 10 + pop
            return x == rev
