# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        '''
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
        '''

        head = None
        next1 = list1
        next2 = list2

        if (next1 == None):
            return next2
        if (next2 == None):
            return next1

        if (next1.val <= next2.val):
            head = list1
        else:
            head = list2
        
        while (next1 != None and next2 != None):
            if (next1.val <= next2.val):
                temp = next1.next
                next1.next = next2
                next1 = temp
            else:
                temp = next2.next
                next2.next = next1
                next2 = temp
        
        if (next1 == None):
            next1 = next2
        else:
            next2 = next1

        return head
    
        '''
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
        '''

list1 = ListNode()
list1.val = 1
list1.next = None
list2 = ListNode()
list2.val = 2
list2.next = None

print(Solution().mergeTwoLists(list1, list2))