# matrix = [[1, 2, 3], [1, 0, 4], [1, 3, 0]]
matrix = [[1,1,2,0],[3,4,5,2],[1,3,1,5]]

print(matrix)
# final = []
l= len(matrix[0])
print ("l=",l)
for row_idx, row in enumerate(matrix):
    for jdx, col in enumerate(row):
        if(matrix[row_idx][jdx]==0):
            # print("row-",row_idx,jdx)
            matrix[row_idx][jdx]=0
            # print("true")
            for k in range(len(matrix[row_idx])):
                matrix[row_idx][k] = -1
            for v in range(len(matrix)):

                matrix[v][jdx]=-1
for idx,row in  enumerate(matrix):
    for jdx,el in enumerate(row):
        if matrix[idx][jdx]==-1:
            matrix[idx][jdx] =0
           
print("\n")
print(matrix)
