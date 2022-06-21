# matrix = [[1, 2, 3], [1, 0, 4], [1, 3, 0]]
matrix = [[1, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
col_dum = [None]*len(matrix[0])
row_dum = [None]*len(matrix)

# row_dum[0]=0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if(matrix[i][j] == 0):
            print(i)
            row_dum[i] = 0
            col_dum[j] = 0


for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if row_dum[i] == 0 or col_dum[j] == 0:
            matrix[i][j] = 0


print(matrix)
# print(row_dum)
# print(col_dum)
