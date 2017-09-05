from numpy import *
from matplotlib import *
from scipy import *
from pylab import figure, show, setp
from mpl_toolkits.mplot3d import Axes3D
from helpers import detect_peaks
def num_rossler(x_n,y_n,z_n,h,a,b,c):
    x_n1=x_n+h*(-y_n-z_n)
    y_n1=y_n+h*(x_n+a*y_n)
    z_n1=z_n+h*(b+z_n*(x_n-c))
    return x_n1,y_n1,z_n1


a=0.13
b=0.2
c=6.5
t_ini=0
t_fin=40*pi
h=0.0001
numsteps=int((t_fin-t_ini)/h)

t=linspace(t_ini,t_fin,numsteps)
x=zeros(numsteps)
y=zeros(numsteps)
z=zeros(numsteps)

x[0]=0
y[0]=0
z[0]=0

for k in range(x.size-1):
    [x[k+1],y[k+1],z[k+1]]=num_rossler(x[k],y[k],z[k],t[k+1]-t[k],a,b,c)

indexes = detect_peaks.detect_peaks(z, mph=1, mpd=2)
print('Peaks are: %s' % (indexes/10000))


fig = figure()

ax3 = fig.add_axes([1.1, 0.1, 0.4, 0.2])
ax4 = fig.add_axes([0.55, 0.25, 0.35, 0.5],projection='3d')

ax3.plot(t, z,color='blue',lw=1,label='z(t)')
ax3.set_xlabel('t')
ax3.set_ylabel('z(t)')
ax3.legend()
ax3.axis((t_ini,t_fin,min(z),max(z)))

ax4.plot(x, y,z,color='black',lw=1,label='Evolution(t)')
ax4.set_xlabel('x(t)')
ax4.set_ylabel('y(t)')
ax4.set_zlabel('z(t)')

show()

