# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 時間計算量 O(n^2)、空間計算量 O(n)
class Step1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        appeared = set()
        while headA:
            appeared.add(headA)
            headA = headA.next
        while headB:
            if headB in appeared:
                return headB
            headB = headB.next
        return None