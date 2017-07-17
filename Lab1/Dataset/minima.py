import numpy as np
import csv

with open('bonusExercise.csv','rb') as f:         # read csv file
    reader=csv.reader(f)
    list1=list(reader)
    matrix = np.array(list1).astype("float")

num_rows, num_cols = matrix.shape
print('LOCAL MINIMAS : \n')
for i in range(1,num_rows-2):
	if (matrix[i][0] < matrix[i-1][0]) & (matrix[i][0] < matrix[i+1][0] ):
		print(matrix[i][0])," , ",(matrix[i][1])
		print('\n')

