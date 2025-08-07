'''
Create a NumPy array with values from 10 to 50.
Extract elements greater than 30


Multiply the array by 2


Find mean and standard deviation of the array'''

import numpy as np
arr=np.arange(10,51 )
print(arr)
print("values greater than 30 :",arr>30)
print(arr*2)
print(np.mean(arr))
print(np.std(arr))

print("-------------------------------")
'''
Task:
 Create a 3x3 matrix with numbers from 1 to 9.
Reshape it to a 1D array


Access the middle row from the original matrix


Replace the last element of reshaped array with 100'''
arr1=np.arange(1,10).reshape(3,3)
print(arr1)
arr2=arr1.flatten()
print(arr2)
arr1[-1]=100
print(arr1)

print('------------------------------------')







'''arr = np.array([5, 12, 17, 23, 45, 50, 66])
Find all even numbers

Replace all values less than 20 with 0'''


arr3= np.array([5, 12, 17, 23, 45, 50, 66])
for i in arr3:
    if i%2==0:
        print(i,end=" ")

print(arr3[arr3<20])


for i in arr3:
    if i>20:
        i=0
        print(i)

print('---------------------------------')


'''Generate a 5x5 matrix with random integers between 1 and 100.
Find the maximum and minimum value in the matrix


Find the sum of each row


Replace all values greater than 50 with -1'''
arr4=np.random.randint(1,101,size=(5,5))
print(arr4)
max=arr4.max()
print(max)
min=arr4.min()
print(min)
sum=arr4.sum()
print(sum)
arr[arr>50]=-1
print(arr4)







