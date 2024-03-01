# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 時間計算量 O(n)、空間計算量 O(n)
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

# 時間計算量 O(n)、空間計算量 O(1)
class Step2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA, hB = headA, headB
        lenA, lenB = 0, 0
        while hA:
            lenA += 1
            hA = hA.next
        while hB:
            lenB += 1
            hB = hB.next
        
        diff = abs(lenA-lenB)
        for i in range(diff):
            if lenA > lenB:
                headA = headA.next
            else:
                headB = headB.next

        while headA or headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None