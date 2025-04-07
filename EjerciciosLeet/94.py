#Los aborles siempre se leen todoooos los que esten a la izquierda primero.
#quiere decir que los de la izquierda tiene mayor gerarquia.

#         8
#       /
#      3
#     / \
#    1   6
#        / \
#       4   7

#Recorrido:
#Izquierda de 8 → 3

#Izquierda de 3 → 1 ✅ [1]

#Regresamos a 3 ✅ [1, 3]

#Derecha de 3 → 6

#Izquierda de 6 → 4 ✅ [1, 3, 4]

#Regresamos a 6 ✅ [1, 3, 4, 6]

#Derecha de 6 → 7 ✅ [1, 3, 4, 6, 7]

#Regresamos a 8 ✅ [1, 3, 4, 6, 7, 8]

#👉 Resultado: [1, 3, 4, 6, 7, 8]

#Definition for a binary tree node. class TreeNode:


class TreeNode:
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        resultado = []

        def inorder(nodo):
            if nodo is None:
                return
            inorder(nodo.left)            
            resultado.append(nodo.val)    
            inorder(nodo.right)           

        inorder(root)
        return resultado
