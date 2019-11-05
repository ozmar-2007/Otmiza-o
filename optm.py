from mpl_toolkits.mplot3d import Axes3D as a3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt



def plot_a_box(l, x, a = 0, g = 60):
    # height of box base from polig5
    Z = np.sin(np.radians(g))*x+a #box walls height from box base
    prj = np.cos(np.radians(g))*x #ground projection
    bb  = l-2*x
    
    if 2*x >= l:
        x = l/2
    
    bet = [x,      x+bb,   a]
    bdt = [bet[1], bet[1], a]
    bdf = [bet[1], x,      a]
    bef = [x,      x,      a]
    
    ute = [bet[0],     bet[1]+prj, Z]
    utd = [bdt[0],     ute[1],     Z]
    udt = [bdt[0]+prj, bdt[1],     Z]
    udf = [udt[0],     bdf[1],     Z]
    ufd = [bdf[0],     bdf[1]-prj, Z]
    ufe = [bet[0],     ufd[1],     Z]
    uef = [bef[0]-prj, bef[1],     Z]
    uet = [uef[0],     bet[1],     Z]
    
    polgn0 = [bet, bdt, bdf, bef]
    polgn1 = [ute, utd, bdt, bet]
    polgn2 = [bdt, udt, udf, bdf]
    polgn3 = [bef, bdf, ufd, ufe]
    polgn4 = [uet, bet, bef, uef]
    
    polgn5 = [[0,0,0],[0, l, 0], [l, l, 0], [l, 0, 0]]
    
    poligons=[polgn0, polgn1, polgn2, polgn3, polgn4, polgn5]
    
    ax = a3(plt.figure())

    for poligon in poligons:
        tri = Poly3DCollection([poligon])
        tri.set_edgecolor('k')
        tri.set_alpha(0.9)
        tri.set_facecolor('brown')
        ax.add_collection3d(tri)
    
    ax.plot([x,x],        [0, l],       zs=[0, 0], color='k', linestyle='dashed')
    ax.plot([bb+x, bb+x], [0, l],       zs=[0, 0], color='k', linestyle='dashed')
    ax.plot([0, l],       [bb+x, bb+x], zs=[0, 0], color='k', linestyle='dashed')
    ax.plot([0, l],       [x, x],       zs=[0, 0], color='k', linestyle='dashed')

    ax.set_zlim3d(0, Z)
    ax.set_ylim3d(0, l)
    ax.set_xlim3d(0, l)
    # Hide grid lines
    ax.grid(False)

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    
    plt.axis('off')

    plt.show()


    
def bhaskara(a, b, c):
    delta = (b * b) - (4 * a * c)
    if delta < 0:
        # Delta menor que 0, a função não tem raízes
        return None
    delta = sqrt(delta)
    r1 = (-b + delta) / (2 * a)
    r2 = (-b - delta) / (2 * a)
    return r1, r2
    
if __name__ == "main" :
    plot_a_box(15, 3, a = 0, g = 90)