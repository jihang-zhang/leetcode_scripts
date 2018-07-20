# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Iterative solution
        head = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next

        # recursive solution
        # if not l1 or not l2:
        #     return l1 or l2
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

#         My own interpretation before looking at discussion
#         Use two loops
#         if l1 == None:
#             return l2
#         if l2 == None:
#             return l1
#         if l1 == None and l2 == None:
#             return None

#         nums = []
#         iteration = 0
#         while l1 != None or l2 != None:
#             if l1 == None:
#                 nums.insert(0, l2.val)
#                 l2 = l2.next
#             elif l2 == None:
#                 nums.insert(0, l1.val)
#                 l1 = l1.next
#             else:
#                 if l1.val < l2.val:
#                     nums.insert(0, l1.val)
#                     l1 = l1.next
#                 else:
#                     nums.insert(0, l2.val)
#                     l2 = l2.next
#         cand = ListNode(nums[0])
#         for n in nums[1:]:
#             result = ListNode(n)
#             result.next = cand
#             cand = result
#         return result
