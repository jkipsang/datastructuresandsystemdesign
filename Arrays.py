
# 2. Traversal of a Matrix Data Structure:
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for row in arr:
    for x in row:
        print(f"{x}", end=" ")
    print()

# 3. Searching in a Matrix Data Structure:

def search_in_matrix(arr, x):
    rows, cols = len(arr), len(arr[0])
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==x:
                return True
    return False


# Driver code to test the function
x = 8
arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]
# print(f" rows: {len(arr)} and columns {len(arr[0])}")

if search_in_matrix(arr, x):
    print("YES")
else:
    print("NO")



#Row wise sorting a 2D array
def sortRows(mat):
    for row in mat:
        print(row, end= " ")
        row.sort()

mat = [
    [77, 11, 22, 3],
    [11, 89, 1, 12],
    [32, 11, 56, 7],
    [11, 22, 44, 33]
]

# print(sortRows(mat))

sortRows(mat)

print('[\n', end='')
for row in mat:
    print('  [', end='')
    print(', '.join(map(str, row)), end='')
    print(']')
print(']')



# Search in a Matrix or 2D Array

def searchMartix(mat, x):
    n=len(mat)
    m= len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j]==x:
                return True
    return False

if __name__ == "__main__":
    mat = [
        [1, 5, 9, 11],
        [14, 20, 21, 26],
        [30, 34, 43, 50]
    ]
    if searchMartix(mat,14):
        print("Found")
    else:
        print("No Found")



# Row-wise vs column-wise traversal of matrix

from time import perf_counter

def row_major(arr):

    rows = len([arr])
    cols = len([arr[0]])

    # Accessing elements row-wise

    for i in range(rows):
        for j in range(cols):
            arr[i][j]+=1

def col_major(arr):

    rows = len([arr])
    cols = len([arr[0]])
    # Accessing elements col-wise
    for j in range(cols):
        for i in range(rows):
            arr[i][j]+=1

if __name__ == "__main__":
    n=1000 # Size of the matrix (n x n)
    arr = [[0] * n for _ in range(n)]
        # Time taken by row-major order
    t_start = perf_counter()
    row_major(arr)
    t_row = perf_counter() - t_start
    print("Row major access time: {:.10f} s".format(t_row))

    # Time taken by column-major order
    t_start = perf_counter()
    col_major(arr)
    t_col = perf_counter() - t_start
    print("Column major access time: {:.10f} s".format(t_col))


#adding two matrices 
def add(A,B):
    n = len(A)
    m = len(A[0])
    C= [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j]=A[i][j]+B[i][j]
    return C


A = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]
B = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]
C = add(A, B)
# print(C)
print("Result matrix is:")
for row in C:
    # print(f"row : {row}")
    print(' '.join(map(str,row)))


#Subtracting Matrices

def subtract(m1,m2):
    rows = len(m1)
    cols = len(m1[0])
    res = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            res[i][j]=m1[i][j]-m2[i][j]
    return res
# Driver code
if __name__ == '__main__':
  
    # Define two rectangular matrices
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[1, 1, 1], [1, 1, 1]]

    # Perform the subtraction
    res = subtract(m1, m2)

    # Print the result matrix
    print("Result matrix is:")
    for row in res:
        print(' '.join(map(str, row)))


# Multiple matrices
# The number of columns in Matrix-1 must be equal to the number of rows in Matrix-2.
# Output of multiplication of Matrix-1 and Matrix-2, results with equal to the number of rows of Matrix-1 and  the number of columns of Matrix-2 i.e. rslt[R1][C2]
def mulMat(m1,m2):
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])
    if c1 != r2:
        print("Invalid Input")
        return None
    # Initialize the result matrix with zeros
    res = [[0]*c2 for _ in range(r1)]
    # Perform matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] +=m1[i][k]*m2[j][k]
    return res
# Driver code
if __name__ == "__main__":
    m1 = [
        [1, 1],
        [2, 2]
    ]

    m2 = [
        [1, 1],
        [2, 2]
    ]

    result = mulMat(m1, m2)

    print("Multiplication of given two matrices is:")
    for row in result:
        print(" ".join(map(str, row)))
