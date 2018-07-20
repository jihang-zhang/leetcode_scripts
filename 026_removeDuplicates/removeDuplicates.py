class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My interpretation
        if nums == []:
            return 0
        curr = nums[0]
        i = 1
        try:
            while True:
                if nums[i] > curr:
                    curr = nums[i]
                    i += 1
                else:
                    del nums[i]
        except IndexError:
            return i