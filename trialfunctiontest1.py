import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

trialfunction='sinc function'

xm=0
deltax=1
xm1=xm+deltax
n_discretise=100
n_leftpoints=7
dFD=deltax/float(n_discretise)

phim=[0 for i in range(-n_leftpoints*n_discretise-1,n_leftpoints*n_discretise+1)]
phimderiv=[0 for i in range(-n_leftpoints*n_discretise-1,n_leftpoints*n_discretise+1)]
xaxis=[0 for i in range(-n_leftpoints*n_discretise-1,n_leftpoints*n_discretise+1)]

phimcarre=[0 for i in range(0,n_leftpoints*n_discretise+1)]

if trialfunction in ['sinc function']:
    for i in range (-n_leftpoints*n_discretise,n_leftpoints*n_discretise+1):
   
        x=xm+(float(i)/n_discretise)*deltax
        xaxis[i]=x
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

 

phimcarre[0]=np.square(phim[0])*dFD
for i in range(1,n_leftpoints*n_discretise+1):
    phimcarre[i]=phimcarre[i-1]+2.*np.square(phim[i])*dFD


tmm_3=0
hmm_3=0
 
for i in range (-n_discretise,n_discretise+1):
    tmm_3=tmm_3+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_3=hmm_3+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)

tmm_5=0
hmm_5=0

for i in range (-2*n_discretise,2*n_discretise+1):
    tmm_5=tmm_5+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_5=hmm_5+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)

tmm_7=0
hmm_7=0

for i in range (-3*n_discretise,3*n_discretise+1):
    tmm_7=tmm_7+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_7=hmm_7+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)

tmm_9=0
hmm_9=0

for i in range (-4*n_discretise,4*n_discretise+1):
    tmm_9=tmm_9+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_9=hmm_9+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)

tmm_11=0
hmm_11=0
for i in range (-5*n_discretise,5*n_discretise+1):
    tmm_11=tmm_11+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_11=hmm_11+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)


tmm_13=0
hmm_13=0
for i in range (-6*n_discretise,6*n_discretise+1):
    tmm_13=tmm_13+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_13=hmm_13+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)

tmm_15=0
hmm_15=0
for i in range (-7*n_discretise,7*n_discretise+1):
    tmm_15=tmm_15+phim[i]*phim[i]*deltax/float(n_discretise)
    hmm_15=hmm_15+phimderiv[i]*phimderiv[i]*deltax/float(n_discretise)




tmm1=0
hmm1=0 

for i in range (0,n_discretise+1):

    tmm1=tmm1+phim[i]*phim[i-n_discretise]*deltax/float(n_discretise);
    hmm1=hmm1+phimderiv[i]*phimderiv[i-n_discretise]*deltax/float(n_discretise);
#print (tmm,tmm1)
#print (hmm,hmm1)
