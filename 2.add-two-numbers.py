from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0   # memory values
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            print(dummyHead.next)
        return dummyHead.next
    # def addTwoNumbers(self, l1, l2):
    #     str_l1, str_l2 = '', ''
    #     while l1:            
    #         str_l1 += str(l1.val)
    #         l1 = l1.next
    #     while l2:            
    #         str_l2 += str(l2.val)
    #         l2 = l2.next
    #     int_l1 = int(str_l1[::-1])
    #     int_l2 = int(str_l2[::-1])       
    #     return list(map(int, str(int_l1 + int_l2)[::-1]))


if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    solution = Solution()
    print(solution.addTwoNumbers(node1, node4).val)