import matplotlib as mpl
from BSplineBase import BSplineBase
import matplotlib.pyplot as plt
import numpy as np
import math
import plotly.graph_objects as go

def generate_random_P():
    P = []
    for i in range(-5,5):
        tmp = []
        for j in range(-5,5):
            tmp.append([i,j,10-math.floor((i*i+j*j)/20)+np.random.rand()])
        P.append(tmp)
    P=np.asarray(P)
    return P


def plotExampleBase(U,style="seaborn",n=3):
    GivenBase = BSplineBase(U)
    mpl.style.use(style)
    us = np.linspace(0,1,1000)
    TotalLen = len(U)-2*(n-1)
    print(TotalLen)
    for i in range(len(U)-2*(n-1)):
        plt.plot(us,[GivenBase.GetValue(u,i,n) for u in us],"C"+str(i))

        
def plot2DExample(U,V,style="seaborn",n=3,i=0,j=0):
    UBase = BSplineBase(U)
    VBase = BSplineBase(V)
    us = np.linspace(0,1,100)
    vs = np.linspace(0,1,100)
    zs = np.asarray([UBase.GetValue(u,i,n) for u in us]).reshape(1,100)*np.asarray([VBase.GetValue(v,j,n) for v in vs]).reshape(100,1)
    fig = go.Figure(data=[go.Surface(z=zs, x=us, y=vs)])
    fig.show()
    
def plotSurface(U,V,P,style="seaborn",n=3):
    UBase = BSplineBase(U)
    VBase = BSplineBase(V)
    us = np.linspace(0,1,100)
    vs = np.linspace(0,1,100)
    zs = []
    for i in range(len(U)-2*(n-1)):
        for j in range(len(V)-2*(n-1)):
            zs.append(
                (
                    np.asarray([UBase.GetValue(u,i,n) for u in us]).reshape(1,100)*np.asarray([VBase.GetValue(v,j,n) for v in vs]).reshape(100,1)
                ).reshape(100,100,1)*P[i,j].reshape(1,3)
            )

    Points = np.asarray(zs).sum(0).reshape(-1,3)
    x, y, z = Points.T

    fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z,color='cyan')])
    for i in range(P.shape[0]):
        
        x,y,z = P[i,:].T
    
        fig.add_scatter3d(
            x=x, y=y, z=z,
            marker=dict(
                size=4,
                color="red",
                colorscale='Viridis',
            ),
            line=dict(
                color='darkblue',
                width=10
            )
        )
    for i in range(P.shape[1]):
        
        x,y,z = P[:,i].T
    
        fig.add_scatter3d(
            x=x, y=y, z=z,
            marker=dict(
                size=4,
                color="red",
                colorscale='Viridis',
            ),
            line=dict(
                color='darkblue',
                width=10
            )
        )
    fig.show()
    
    
