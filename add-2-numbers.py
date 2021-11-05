# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = []
        
        l3 = ListNode()
        start_node = l3
        is_first = True
        
        while l1 != None and l2 != None:
            dig_sum = l1.val + l2.val + carry
            if is_first:
                l3.val = dig_sum % 10
                is_first = False
            else:
                next_node = ListNode(val=dig_sum % 10)
                l3.next = next_node
                l3 = next_node
            carry = dig_sum // 10
            l1 = l1.next
            l2 = l2.next
        
        larger_list = l1 if l2 == None else l2
        
        while larger_list != None:
            dig_sum = larger_list.val + carry
            l3.next = ListNode(val=dig_sum % 10)
            l3 = l3.next
            carry = dig_sum // 10
            larger_list = larger_list.next
            
        if carry > 0:
            l3. next = ListNode(val=carry)
            l3 = l3.next
        
        return start_node
        
