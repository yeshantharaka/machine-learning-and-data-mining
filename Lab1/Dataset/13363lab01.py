import numpy as np
import csv
		
def second_power(matrix):                           # get element wise square
	matrix = np.power(matrix,2)
	return matrix
		
def cal(matrix,mean_matrix,num_rows):               # substitiute matrix element with means
	# matrix[:,0] = matrix[:,0]-mean_matrix[0]
	# matrix[:,1] = matrix[:,1]-mean_matrix[1]
	# matrix[:,2] = matrix[:,2]-mean_matrix[2]
	# matrix[:,3] = matrix[:,3]-mean_matrix[3]
	# matrix[:,4] = matrix[:,4]-mean_matrix[4]
	B = [list(mean_matrix) for i in range(num_rows)]
	sub = np.array(matrix)-np.array(B)
	
	return sub

with open('labExercise01.csv','rb') as f:         # read csv file
    reader=csv.reader(f)
    list1=list(reader)
    matrix = np.array(list1).astype("float")

#matrix = np.array(list(csv.reader(open("labExercise01.csv", "rb"), delimiter=","))).astype("float")

num_rows, num_cols = matrix.shape

mean_matrix = np.mean(matrix,axis=0)     # get mean matrix colom wise

matrix = cal(matrix,mean_matrix,num_rows)
matrix = second_power(matrix)
sum_matrix = np. sum (matrix,axis = 0)

sum_matrix1 = sum_matrix/(num_rows-1)
sum_matrix1 = np.sqrt(sum_matrix1)        # get squareroot elementwise
print('Sn value : ')
print(sum_matrix1)
print('\n')

# ---------------------- BONUS ----------------------------------------------#

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

print('------- end of local minimas ----------')
#--------------------------------------------------------------------------#