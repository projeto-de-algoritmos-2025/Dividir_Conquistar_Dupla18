class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       #Junta as listas
        def merge_two(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
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
        #Divide a lista em metades
        def split(head: Optional[ListNode]):
            mid = head
            ahead = head.next
            while ahead and ahead.next:
                mid = mid.next
                ahead = ahead.next.next
            right = mid.next
            mid.next = None
            return head, right
        #Chamada recursiva do dividir e conquistar
        def divide_and_conquer(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node or not node.next:
                return node
            #Divide as partes
            left, right = split(node)
            #Ordena 
            left = divide_and_conquer(left)
            right = divide_and_conquer(right)
            #Junta novamente
            return merge_two(left, right)

        return divide_and_conquer(head)
