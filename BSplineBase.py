import numpy as np

class BSplineBase:
    def __init__(self,U=np.asarray([0,0,0,0,0.5,1,1,1,1])):
        self.U=U
        # self.n=n
    def GetValue(self,u,i,degree=3):
        U=self.U
        p=degree
        if degree==0:
            if u>=U[i] and u<=U[i+1]:
                return 1
            else:
                return 0
        else:
            degree=degree-1
            if u>=U[i] and u <=U[i+p+1]:
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
