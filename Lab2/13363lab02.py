import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def func(value):
    f = 3*(value**3) -3*(value) + 3
    #f = (9 * (value ** 2) - 3)
    return f

def get_y(current_x,t,n):
    #t = input('enter T :')
    #n = input('enter n :')
    #current_x = input('enter current x :')
    #current_x = 3
    #t=0.002
    #n=0.001
    previous_step_size = current_x
    x_values = []
    y_values = []

    while (previous_step_size > t):
        previous_x = current_x
        temp = func(previous_x)
        current_x = current_x - (n*temp)
        x_values.append(current_x)
        y_values.append(func(current_x))
        previous_step_size = abs(current_x - previous_x)


    return (x_values,y_values)

def local_minima(current_x,t,n):
    x_values = []
    y_values = []
    x_values , y_values = get_y(current_x,t,n)
    #print x_values
    i = len(y_values)
    plt.plot(x_values,y_values)
    return y_values[i-1]
#print ("Local minima is :  " , y_values[i-1])

x_values1 = []
y_values1 = []
i1=-2
while(i1<2):
    temp = func(i1)
    x_values1.append(i1)
    y_values1.append(temp)
    i1=i1+0.1

plt.plot(x_values1,y_values1)
plt.show()

import unittest

class Test(unittest.TestCase):
    def test_null(self):
        self.assertEqual(local_minima(3,0.002,0.001),1.9953391650431995)

    def test_one_ele(self):
        self.assertEqual(local_minima(5,0.002,0.001),1.9953391650431995)

    def test_two_ele(self):
        self.assertEqual(local_minima(3,0.2,0.1),1.9953391650431995)

    def test_three_ele(self):
        self.assertEqual(local_minima(3,2,1),1.9953391650431995)

    if __name__ == '__main__':
        unittest.main()



# 2.  initial x value is very big when compare with presision. then it can get many values for x and y coordinates
# to draw clear and smooth graph.

# 3. when gives big value for learning rate(n), code is infinitly running.

# 4. result is a curve. it's curve is change acording to the current_x value.
# when the value is decreased, curve also decrease
