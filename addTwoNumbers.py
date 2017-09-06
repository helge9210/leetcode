# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next_node_1 = l1
        next_node_2 = l2
        sum_node = ListNode(0)
        next_sum_node = sum_node
        overflow = 0

        while True:

            if next_node_1 is not None:
                value_1 = next_node_1.val
                next_node_1 = next_node_1.next
            else:
                value_1 = 0

            if next_node_2 is not None:
                value_2 = next_node_2.val
                next_node_2 = next_node_2.next
            else:
                value_2 = 0

            next_overflow, value_sum = divmod(value_1 + value_2 + overflow, 10)
            print(value_1, value_2, value_sum, overflow)

            next_sum_node.val += (value_sum)
            overflow = next_overflow


            if next_node_1 is None and next_node_2 is None:
                if overflow > 0:
                    next_sum_node.next = ListNode(overflow)
                break

            next_sum_node.next = ListNode(0)
            next_sum_node = next_sum_node.next

        return sum_node

if __name__ == '__main__':
    il1 = ListNode(1)
    #il1.next = ListNode(4)
    il2 = ListNode(9)
    il2.next = ListNode(9)
    #il2.next.next = ListNode(4)

    c = Solution()
    l = c.addTwoNumbers(il1, il2)
    print(l.val, l.next.val, l.next.next.val)

