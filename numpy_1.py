



 import random
w = np.array(random.sample(range(1000), 12)) # одномерный массив из 12 случайных чисел от 1 до 1000
w = w.reshape((2,2,3)) # превратим w в трёхмерную матрицу
print(w)

print(w.transpose(0,2,1))
