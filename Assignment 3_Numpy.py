import numpy as np

print('--------1------------')
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
print(np.where(arr % 2 == 1, -1, arr))


print('--------2------------')
arr = np.arange(10)
print(arr)
print(np.reshape(arr, (-1, 5)))


print('--------3------------')
arr = np.array([1,2,3])
print(np.r_[np.repeat(arr, 3), np.tile(arr, 3)])


print('--------4------------')
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))

print('--------5------------')
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a == b))


print('--------6------------')
rand_arr = np.random.uniform(5,10, size=(5,3))
print(rand_arr)


print('--------7------------')
np.set_printoptions(suppress=False)
arr = np.arange(15)
print(arr)
np.set_printoptions(threshold=6)
print(arr)


print('--------8------------')
import random
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
np.set_printoptions(suppress=True, precision=6)
print(rand_arr)


print('--------9------------')
arr = np.arange(9).reshape(3,3)
print(arr)
arr[:, [1,0,2]]


print('--------10------------')
arr = np.arange(9).reshape(3,3)
print(arr)
arr[[1,0,2],:]