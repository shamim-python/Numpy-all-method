#make array
import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("a=",a)
print("b=",b)
print("c=",c)

#scan shape
print("shape:",a.shape)

#scan Dimension
print("Dimension",c.ndim)

#scan datatype
print("Datatype:",b.dtype)

#Array indexing/slicing:
print(b[0,1])
print(b[:,1])
print(c[2,-1])
print(c[-1,-1])
print(a[1])

    #array math
#array sumation       
print("sumation=",np.sum(b))
#array average
print("mean=",np.mean(c))
# array standard deviation(std)
print("std=",np.std(c))

arr=np.array([100,102,98,101,99])
ar=np.array([2,4,8,16,32])
a=np.array([100,101,100,99,100,99,100])
print(np.mean(arr))
print(np.std(arr))
print(np.mean(ar))
print(np.std(ar))
print(np.mean(a))
print(np.std(a))

d=np.array([1,2,3])
print(d)
e=np.zeros((3,3))
print(e)
f=np.arange(1,21,)
f=np.arange(1,21,3)
print(f)
g=np.linspace(2,10,5)
print(g)


#chalange
G=np.array([[10,20,30],[40,50,60]])
#1 shape and dimension
print(np.shape(G))
print(np.ndim(G))

#2 eliment of second row third collum
print(G[1,1])
#sumation of every collum
print(np.sum(G,axis=0))

#average
print(np.mean(G))
#5 print 2nd collum
print(G[:,2])
print(sum(G[:,2]))


#subarray
h=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(h [0:2,1:3])

i=np.array([1,2,3])
j=np.array([[1],[2],[3]])
print(i+j)

k=np.arange(6)
print(k)
l=k.reshape((2,3))
print(l)
print(l.T)
print(b.flatten())
m=np.array([[1,2,3],[4,5,6]])
print(m)
print(m.flatten())
n=np.arange(1,10)
o=n.reshape((3,3))
print(o)
print(n.flatten())
p=np.arange(12)
q=p.reshape(3,4)

z=np.arange(1,10).reshape(3,3)
print(z)
print("sum=",np.sum(z))
print("Mean=",np.mean(z))
print("std=",np.std(z))
print("max=",np.max(z))
print("min=",np.min(z))
print("0st cullam",z[:,0])
print("2nd row=",z[1,:])

y=np.arange(10,26).reshape(4,4)
print(y)

print(y.diagonal())
print(y.flatten())
print(y[y%2==0])
print(y*2)





