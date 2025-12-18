class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        return val == val[::-1]