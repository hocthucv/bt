import numpy as np
n=int(input("n="))
a=np.arange(n)
for i in range(n):
    a[i]=input("Nhập phần tử =")
print("Vector:", a)
for m in range(len(a)-1):
    for n in range(m+1,len(a)):
        if a[m]<a[n]:
            a[m],a[n]=a[n],a[m]
print("Vector giảm dần:", a)
