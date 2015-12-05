


from numpy import *
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import operator


class BsplineBase:
    def __init__(self,U=np.asarray([0,0,0,0,0.5,1,1,1,1]),n=5):
        self.U=U
        self.n=n
    def GetValue(self,u,i,degree=3):
        U=self.U
        p=degree
        if degree==0:
            if u>=U[i] and u<U[i+1]:
                return 1
            else:
                return 0
        else:
            degree=degree-1
            if u>=U[i] and u <U[i+p+1]:
                if U[i+p]!=U[i] and U[i+p+1]!=U[i+1]:
                    return (u-U[i])/(U[i+p]-U[i])*self.GetValue(u,i,degree)+(U[i+p+1]-u)/(U[i+p+1]-U[i+1])*self.GetValue(u,i+1,degree)
                elif U[i+p]!=U[i]:
                    return (u-U[i])/(U[i+p]-U[i])*self.GetValue(u,i,degree)
                elif U[i+p+1]!=U[i+1]:
                    return (U[i+p+1]-u)/(U[i+p+1]-U[i+1])*self.GetValue(u,i+1,degree)
                else:
                    return 0
            else:
                return 0

def getPoint():
    dim=input("please enter the dimention you want:\n")
    n=4
    Points=np.zeros([n,dim])
    for i in range(n):
        Points[i]=np.asarray(input("please enter the point\n"),float)
    return Points
def GetPlace(U=np.asarray([0,0,0,0,0.5,1,1,1,1]),u=0.5):
    for i in range(U.shape[0]):
        if u<=U[i+1] and u>=U[i]:
            return i
    return "out of the boundary!"
#add 0.5 to U to compute new Points2
def GetnewPoints(U=np.asarray([0,0,0,0,0.5,1,1,1,1]),Points=np.asarray([[0,0,0],[-1,2,-2],[5,6,-3],[2,-4,-4],[5,-6,8]]),u=0.5,degree=3):
    Points2=np.zeros([Points.shape[0]+1,3])
    i=GetPlace(U,u);
    Points2[:(i-degree)]=Points[:(i-degree)]
    for j in range(i-degree+1,i+1):
        alpha=(u-U[j])/(U[j+degree]-U[j])
        Points2[j]=(1-alpha)*Points[j-1]+alpha*Points[j]
    Points2[(i+1):]=Points[i:]
    return Points2
def BsplineCurve(Points,B,T=r_[0:1:0.001]):
    ans=np.zeros([T.size,Points.shape[1]])
    for j in range(T.size):
        for i in range(Points.shape[0]):
            ans[j]=ans[j]+B.GetValue(T[j],i,degree=3)*Points[i]
    return ans.transpose()


Points1=np.asarray([[0,0,0],[-1,2,-2],[5,6,-3],[2,-4,-4],[5,-6,8]])
P1=Points1.transpose()
U1=np.asarray([0,0,0,0,0.5,1,1,1,1])
B1=BsplineBase(U1,n=5)


Points2=GetnewPoints(U1,Points1,u=0.5,degree=3)
P2=Points2.transpose()
U2=[0,0,0,0,.5,.5,1,1,1,1]
B2=BsplineBase(U2,n=6)

T=r_[0:1:0.001]
C1=BsplineCurve(Points1,B1,T)

x1=C1[0]
y1=C1[1]
z1=C1[2]

C2=BsplineCurve(Points2,B2,T)
x2=C2[0]
y2=C2[1]
z2=C2[2]


fig=plt.figure()
ax=p3.Axes3D(fig)
plt.plot(P1[0],P1[1],P1[2],'mo:')
plt.plot(P2[0],P2[1],P2[2],'ro:')
ax.plot_wireframe(x1,y1,z1,color='b')
ax.plot_wireframe(x2,y2,z2,color='g')
plt.show()







