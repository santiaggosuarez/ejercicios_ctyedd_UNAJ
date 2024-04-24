# SITIO PARA EJECUTAR CÓDIGO PYTHON ONLINE: https://www.mycompiler.io/es/new/python

# CONSIGNA:

# Escribir un método que devuelve un camino desde la raíz hasta una hoja en donde la longitud del mismo debe ser igual al parámetro. Puede retornar cualquier camino que encuentre y en caso de no encontrar ninguno retornar la lista vacía.

# CONSTRUCCIÓN DEL ÁRBOL

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(22)
root.right.left = TreeNode(6, TreeNode(7))
root.right.right = TreeNode(18)

# MÉTODO REQUERIDO

def solve(root, edge_count):
    # Verifica si la raíz del árbol está vacía, en cuyo caso retorna una lista vacía.
    if not root:
        return []
    
    # Usa una pila para almacenar los pares de nodos y el camino hasta ese nodo.
    # Inicializa la pila con la raíz del árbol y un camino que comienza con la raíz.
    stack = [(root, [])]
    
    while stack:
        # Saca el último nodo y el camino correspondiente de la pila.
        node, path = stack.pop()
        
        # Si se encuentra una hoja y la longitud del camino es igual al parámetro 'edge_count', retorna el camino actual más el nodo hoja.
        if not node.left and not node.right and len(path) == edge_count:
            return path + [node.value]
        
        # Si hay un hijo derecho, lo agrega a la pila con el camino actualizado.
        if node.right:
            stack.append((node.right, path + [node.value]))
        # Si hay un hijo izquierdo, lo agrega a la pila con el camino actualizado.
        if node.left:
            stack.append((node.left, path + [node.value]))

    return []


# EJERCICIO:

# Si longitud= 1 retorna: 8-5 
long = 1
print(f"Longitud = {long}:", solve(root, long))

# Si longitud= 2 retorna: 8-22-18
long = 2
print(f"Longitud = {long}:", solve(root, long))

# Si longitud= 5 retorna lista vacía
long = 5
print(f"Longitud = {long}:", solve(root, long))
