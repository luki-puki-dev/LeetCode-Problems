# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = []
        l4 = []
        while l1:
            l3.append(l1.val)
            l1 = l1.next
        
        while l2:
            l4.append(l2.val)
            l2 = l2.next
        number1 = 0
        for i in reversed(l3):
            number1 = (number1*10) + i
        number2 = 0
        for j in reversed(l4):
            number2 = (number2*10) + j
        
        added_numbers = number1 + number2

        final_list = list(map(int,str(added_numbers)))

        l5 = ListNode()
        current = l5
        for num in reversed(final_list):
            current.next = ListNode(num)
            current = current.next
        return l5.next
