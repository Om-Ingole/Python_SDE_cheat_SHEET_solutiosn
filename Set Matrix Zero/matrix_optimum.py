# matrix = [[1, 2, 3], [1, 0, 4], [1, 3, 0]]
# # from threading import main_thread
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
#######only for printing in Matrix format
for line in matrix:
    print(*line)
print("\n")
###########
col0 = 1
for i, row in enumerate(matrix):
    if matrix[i][0] == 0:
        col0 = 0
    for j, col in enumerate(row, 1):

        if(j < len(row)):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
######## only for printing in Matrix format
for line in matrix:
    print(*line)
print("\n")
########
for i, row in reversed(list(enumerate(matrix))):
    if(i >= 0):#To avoid list out off bound err
        for j, col in reversed(list(enumerate(row))):
            if(j >= 1):  # To avoid list out off bound err
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    if col0 == 0:
        matrix[i][0] = 0

######## output
for line in matrix:
    print(*line)
print(col0)

