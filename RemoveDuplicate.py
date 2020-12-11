
class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        curr = head.next
        prev = head
  
        while curr != None:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
    
        return head
