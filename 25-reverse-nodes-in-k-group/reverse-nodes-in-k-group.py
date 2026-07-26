class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:

            # Find the kth node
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = prev_group.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp