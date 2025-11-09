class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

# Busca binária para equilibrar duas metades entre os arrays ordenados
# ajusta partições até que os elementos da esquerda sejam menores que os da direita
# retorna a mediana combinando corretamente as duas metades.

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  

        m, n = len(nums1), len(nums2)
        total = m + n
        meio = total // 2

        esquerda, direita = 0, m

        while esquerda <= direita:
            i = (esquerda + direita) // 2
            j = meio - i

            # limites da partição infinitos para arrays vazios
            esquerdaA = nums1[i - 1] if i > 0 else float("-inf")
            direitaA = nums1[i] if i < m else float("inf")
            esquerdaB = nums2[j - 1] if j > 0 else float("-inf")
            direitaB = nums2[j] if j < n else float("inf")

            # condição de partição 
            if esquerdaA <= direitaB and esquerdaB <= direitaA:

                # mediana impar
                if total % 2 == 1:
                    return float(min(direitaA, direitaB))

                # mediana par
                return (max(esquerdaA, esquerdaB) + min(direitaA, direitaB)) / 2.0

            elif esquerdaA > direitaB:
                direita = i - 1
            else:
                esquerda = i + 1

        return 0