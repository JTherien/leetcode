from math import log10

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        
        sol = Solution()

        n1 = sol.list_reverse_int(l1)
        n2 = sol.list_reverse_int(l2)
        n3 = n1 + n2
        
        l3 = []

        if n3 == 0:

            return 0

        for m in range(int(log10(n3)), -1, -1):

            magnitude = 10 ** m

            n3_mod = n3 % magnitude

            digit = n3 - n3_mod

            l3[:0] = [int(digit / magnitude)]

            n3 -= digit        
        
        return l3

    def list_reverse_int(self, l: list) -> int:

        num = 0

        for n, i in enumerate(l):

            num += i * (10 ** n)

        return num

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.addTwoNumbers([2,4,3], [5,6,4]))