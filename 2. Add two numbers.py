"""
Task: You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example_1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example_2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example_3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag=False
        l=t=ListNode()
        while(True):
            if flag:
                t.val+=1
                flag=False
            if l1!=None:
                t.val+=l1.val
                l1=l1.next
            if l2!=None:
                t.val+=l2.val
                l2=l2.next
            if t.val>9:
                flag=True
                t.val-=10
            if l2==l1 and l2==None and not flag:
                break
            t.next=ListNode()
            t=t.next
        return(l)