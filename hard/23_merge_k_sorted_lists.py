from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        if not lists:
            return None
        #Junta as listas
        def merge_two(a: Optional['ListNode'], b: Optional['ListNode']) -> Optional['ListNode']:
            dummy = ListNode(0)
            current = dummy
            while a and b:
                #Escolha do menor valorem busca da ordem crescente , movimentação do ponteiro no item da lista escolhido
                if a.val <= b.val:
                    current.next = a
                    a = a.next
                else:
                    current.next = b
                    b = b.next
                current = current.next
            current.next = a or b
            return dummy.next

        def divide_and_conquer(left: int, right: int) -> Optional['ListNode']:
            if left == right:
                return lists[left]
            #Calcula o meio
            mid = (left + right) // 2
            #Junta as partes esquerda e direita
            l = divide_and_conquer(left, mid)
            r = divide_and_conquer(mid + 1, right)
            return merge_two(l, r)
        #Chamada inicial dos limites
        return divide_and_conquer(0, len(lists) - 1)
