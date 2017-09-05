from pylab import *

A = rand(3,3)
A[0:2,1] = 4

I = A @ inv(A)
I = A.dot(inv(A))

t = linspace(0,4,num=1e3)
y1= cos(t/2) * exp(-t)
y2 = cos(t/2) * exp(-5*t)

figure()
plot(t, y1, label = 'Slow decay')
plot(t, y2, label = 'Fast decay')

legend(loc='best')
show()