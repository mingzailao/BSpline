


from numpy import *
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import operator


class BsplneBase:
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
            # if U[i+p]!=U[i] and U[i+p+1]!=U[i+1]:
            #         return (u-U[i])/(U[i+p]-U[i])*self.GetValue(u,i,degree)+(U[i+p-1+1]-u)/(U[i+p+1]-U[i+1])*self.GetValue(u,i+1,degree)
            # elif U[i+p]!=U[i]:
            #         return (u-U[i])/(U[i+p]-U[i])*self.GetValue(u,i,degree)
            # elif U[i+p+1]!=U[i+1]:
            #         return (U[i+p-1+1]-u)/(U[i+p+1]-U[i+1])*self.GetValue(u,i+1,degree)
            # else:
            #         return 0
def getPoint():
    dim=input("please enter the dimention you want:\n")
    n=4
    Points=np.zeros([n,dim])
    for i in range(n):
        Points[i]=np.asarray(input("please enter the point\n"),float)
    return Points

def BsplineCurve(Points,B=BsplneBase(U=np.asarray([0,0,0,0,0.5,1,1,1,1]),n=5),T=r_[0:1:0.001]):
    ans=np.zeros([T.size,Points.shape[1]])
    for j in range(T.size):
        for i in range(Points.shape[0]):
            ans[j]=ans[j]+B.GetValue(T[j],i,degree=3)*Points[i]
    return ans.transpose()


Points=np.asarray([[0,0,0],[-1,2,-2],[5,6,-3],[2,-4,-4],[5,-6,8]])
print Points.shape[1]
PP=Points.transpose()
U=np.asarray([0,0,0,0,0.5,1,1,1,1])
B=BsplneBase()


#
T=r_[0:1:0.001]
ans=BsplineCurve(Points,B,T)

x=ans[0]
y=ans[1]
z=ans[2]



fig=plt.figure()
ax=p3.Axes3D(fig)
plt.plot(PP[0],PP[1],PP[2],'mo:')
ax.plot_wireframe(x,y,z,color='b')
plt.show()






