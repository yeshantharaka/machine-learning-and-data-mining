import pandas as pd
import numpy as np
import sys
import unittest
from pandas.util.testing import assert_frame_equal


class Lab03Cov_Corr:

    def cov(self,Xvalue,Yvalue):
        xmean = Xvalue.mean()
        ymean = Yvalue.mean()
        N=Xvalue.size

        return_value=0
        for x in xrange(0, N):
            xi=Xvalue[x]
            yi = Yvalue[x]
            return_value +=(((xi-xmean)*(yi-ymean))/(N-1))

        return  return_value

    def corr(self,Xvalue,Yvalue):

        sdx=Xvalue.std()
        sdy=Yvalue.std()

        covval=self.cov(Xvalue,Yvalue)
        return ((covval) / (sdx*sdy))


df=pd.read_csv('lab03Exercise.csv',names=['a','b','c','d','e'])
df.shape
df=df.fillna(0)
co = Lab03Cov_Corr()

names=['a','b','c','d','e']
matrix=np.zeros(shape=(5,5),dtype=float)
print "Find the covariance matrix..."
for i in range(0, 5):
    for j in range(0,5):
        if i==j:
            val=df.loc[:,names[i]].var()
        else:
            val=co.cov((df.loc[:,names[i]]),(df.loc[:,names[j]]))

        matrix[i][j]=val

print '\n '
print matrix
print "\n ..................\n"
print df.cov()



matrix=np.zeros(shape=(5,5),dtype=float)
print "Find the correlation matrix..."
for i in range(0, 5):
    for j in range(0,5):
        matrix[i][j]=co.corr((df.loc[:,names[i]]),(df.loc[:,names[j]]))


print '\n '
print matrix
print "\n..................\n"
print df.corr()


class calculationTesting(unittest.TestCase):
    def setUp(self):
        print("=============================================")
        print("caculationTesting: SetUp : Begin")



    def testCovariance(self):

        df = pd.read_csv('lab03Exercise.csv', names=['a', 'b', 'c', 'd', 'e'])
        df.shape
        df = df.fillna(0)
        co = Lab03Cov_Corr()

        names = ['a', 'b', 'c', 'd', 'e']
        matrix = np.zeros(shape=(5, 5), dtype=float)
        print "Find the covariance matrix..."
        for i in range(0, 5):
            for j in range(0, 5):
                if i == j:
                    val = df.loc[:, names[i]].var()
                else:
                    val = co.cov((df.loc[:, names[i]]), (df.loc[:, names[j]]))

                matrix[i][j] = val
        actual=pd.DataFrame(matrix,names,names)
        correct=df.cov()
        assert_frame_equal(actual,correct)

    def testCorrelation(self):
        df = pd.read_csv('lab03Exercise.csv', names=['a', 'b', 'c', 'd', 'e'])
        df.shape
        df = df.fillna(0)
        co = Lab03Cov_Corr()

        names = ['a', 'b', 'c', 'd', 'e']
        matrix = np.zeros(shape=(5, 5), dtype=float)
        print "Find the correlation matrix..."
        for i in range(0, 5):
            for j in range(0, 5):
                matrix[i][j] = co.corr((df.loc[:, names[i]]), (df.loc[:, names[j]]))
        actual = pd.DataFrame(matrix, names, names)
        correct = df.corr()
        assert_frame_equal(actual, correct)

    def tearDown(self):
        print("calculationTesting: tearDown : Begin")
        print("=============================================")


if __name__ == '__main__':
    unittest.main()
	
	
	
	
	
	
	
# 2. since there is no zeros in the covariance matrix, we can conclude all the metrix are corelated.