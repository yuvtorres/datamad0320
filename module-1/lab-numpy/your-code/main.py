#1. Import the NUMPY package under the name np.
import numpy as np

#2. Print the NUMPY version and the configuration.
print(f" Mi versión de numpy es: {np.version.version}")

"""
 Mi versión de numpy es: 1.17.4
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a=np.asarray([[[np.random.standard_normal() for i in range(2)] for k in range(3)] for l in range(5)])
a=np.random.random_sample((3,2,5))
a=np.random.random((3,2,5))

#4. Print a.
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.ones((5,2,3))

#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
# Yes they have it
print(a.size==b.size)

#8. Are you able to add a and b? Why or why not?
"""
# No, because the shape are different
# Indeed the c=a+b gives the following error:

ValueError: operands could not be broadcast together with shapes (3,2,5) (5,2,3)
"""

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c=b.T
print(f'a shape--> {a.shape} | b shape -->  {b.shape} | c shape --> {c.shape}')

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
"""
It works now because the have the same shape.
"""
d=a+c

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
"""
The values of d are the values of a plus one. And both have the same shape.
"""
print(f'This is a:\n{a} \n\n and this is d:\n{d}')


#12. Multiply a and c. Assign the result to e.
e=a*c
print(f'\n\n e:\n\n{e}\n')

#13. Does e equal to a? Why or why not?
"""
Yes there are similar because we are multiplying by ones
"""
print(e==a)

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=d.max()
d_min=d.min()
d_mean=d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.empty((d.shape))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for i_a,e_a in enumerate(d):
    for i_b,e_b in enumerate(e_a):
        for i_c,e_c in enumerate(e_b):
            if e_c==d_min:
                f[i_a,i_b,i_c]=0
            elif e_c<d_mean:
                f[i_a,i_b,i_c]=25
            elif e_c==d_mean:
                f[i_a,i_b,i_c]=50
            elif e_c<d_max:
                f[i_a,i_b,i_c]=75
            elif e_c==d_max:
                f[i_a,i_b,i_c]=100

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(f'what I have in d\n{d}')
print(f'\n\nwhat I have in f\n{f}')

# Yes, I have what I expected in f one 100, one zero and no 50's

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
claves={0:"A",25:"B",50:"C",75:"D",100:"E"}

f_l=[[[claves[e_a]  for e_a in e_b ]  for e_b in e_c]  for e_c in f]

print(f_l)

f_l

