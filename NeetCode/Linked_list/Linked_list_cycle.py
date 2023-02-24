class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        '''
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        '''
        
        small = head
        fat = head

        if (not head):
            return False

        while (fat and small):
            if (not fat.next or not small.next):
                return False
            small, fat = small.next.next, fat.next
            if (small == fat):
                return True
        
        return False
    