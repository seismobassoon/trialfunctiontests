import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

trialfunction='sinc function'

xm=0
deltax=1
xm1=xm+deltax
n_discretise=100

phim=[0 for i in range(-n_discretise-1,n_discretise+1)]
phimderiv=[0 for i in range(-n_discretise,n_discretise+1)]

if trialfunction in ['sinc function']:
    for i in range (-n_discretise,n_discretise+1):
   
        x=xm+(float(i)/n_discretise)*deltax

        xx=(x-xm)/deltax
        phim[i] = np.sinc(xx)
        if i == 0:
            phimderiv[i]=0
        else:
            phimderiv[i]=(phim[i]-phim[i-1])/(deltax/n_discretise)
            #phimderiv[i]=np.pi/deltax*(xx*np.cos(np.pi*xx)-np.sin(np.pi*xx))/(xx*xx)

elif trialfunction in ['linear spline']:
    for i in range (-n_discretise,0):
        x=xm+(float(i)/n_discretise)*deltax
        phim[i]=(x+deltax)/deltax
        phimderiv[i]=1./deltax
    for i in range (0,n_discretise+1):
        x=xm+(float(i)/n_discretise)*deltax
        phim[i]=(-x+deltax)/deltax
        phimderiv[i]=-1./deltax

 

tmm=0
hmm=0
 
for i in range (-n_discretise,n_discretise+1):
    tmm=tmm+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm=hmm+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)

tmm1=0
hmm1=0 

for i in range (0,n_discretise+1):

    tmm1=tmm1+phim[i]*phim[i-n_discretise]*deltax/float(n_discretise);
    hmm1=hmm1+phimderiv[i]*phimderiv[i-n_discretise]*deltax/float(n_discretise);
print (tmm,tmm1)
print (hmm,hmm1)
