def get_Sum(coordinate,matrix2D):
  #Funcion para obtener los numeros de la suma Maxima
  listSumOutput =[]
  for i in range(coordinate[1],coordinate[0]+1,1):
      listSumOutput.append(matrix2D[i][i])
      print(matrix2D[i][i])
  return listSumOutput

def set_all_sum (matrix):
   #Funcion para obtener las sumas
   sumMax=0
   coordinate =[0,0]
   for i in range(1,len(matrix),1):
       for j in range(i):
          matrix[i][j]=matrix[i-1][j]+matrix[i][i]
          if sumMax<matrix[i][j]:
             sumMax = matrix[i][j]
             coordinate [0] = i
             coordinate [1] = j
   return coordinate

def get_integer_input(prompt):
    #Función para obtener un número entero del usuario con validación.
    n = input(prompt)
    if n.isdigit():
        return int(n)
    else:
        print("La entrada no es un número válido.")
        return None

def get_numbers_list(n):
    #Función para obtener una lista de números del usuario.
    lista = []
    for _ in range(n):
        digit = input("Escribe un número para la lista: ")
        if digit.isdigit():
            lista.append(int(digit))  # Convertir digit a entero y agregar a la lista
        else:
            print("No ingresaste un número")
            lista.append(0)  # Usar 0 como valor predeterminado
    return lista

def create_matrix(n):
    #Función para crear una matriz bidimensional n x n inicializada con ceros.
    return [[0] * n for _ in range(n)]

def fill_diagonal(matrix, values):
    #Función para llenar la diagonal principal de la matriz con los valores dados.
    for i in range(len(matrix)):
        matrix[i][i] = values[i]

def print_matrix(matrix):
    #Función para imprimir la matriz.
    for row in matrix:
        print(row)

def main():
    n = get_integer_input("Escribe un número: ")
    if n is not None:
        lista = get_numbers_list(n)
        matrix2D = create_matrix(n)
        fill_diagonal(matrix2D, lista)
        coordinate= set_all_sum(matrix2D)
        print_matrix(matrix2D)
        listSum=get_Sum(coordinate,matrix2D)
        print(listSum)
if __name__ == "__main__":
    main()
