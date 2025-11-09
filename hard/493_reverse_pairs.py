class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# Divide e Conquista feito com mergesort
# divide o array depois conta pares entre as metades e depois mescla ordenado.
# retorna o total de pares i e j

        def mesclar_contar(esquerda, direita):
            i = j = cont = 0
            while i < len(esquerda) and j < len(direita):
            # ve esquerda é maior que o dobro de direita para validar os da esquerda
                if esquerda[i] > 2 * direita[j]:
                    cont += len(esquerda) - i
                    j += 1
                else:
                    i += 1
            return cont, sorted(esquerda + direita)

        def dividir(lista):
            if len(lista) <= 1:
                return 0, lista
            meio = len(lista) // 2
            cont_esq, esquerda = dividir(lista[:meio])
            cont_dir, direita = dividir(lista[meio:])
            # conta pares cruzando esquerda e direita
            cont_merge, ordenado = mesclar_contar(esquerda, direita)
            # soma todos os pares encontrados
            return cont_esq + cont_dir + cont_merge, ordenado

        total, _ = dividir(nums)
        return total