class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute Force
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Two-pass Hash Table
        # lookup = {}
        # for i in range(len(nums)):
        #     lookup[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in lookup and lookup[complement] != i:
        #         return [i, lookup[complement]]

        # One-pass Hash Table
        lookup = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup:
                return [i, lookup[complement]]
            lookup[nums[i]] = i
