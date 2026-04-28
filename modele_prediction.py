import numpy as np


def prediction(**kwargs):
    B=np.load('matrice_B.npy')
    Y=np.load('matrice_Y.npy')
    X=np.load('matrice_X.npy')
    Y_predi=np.load('matrice_Y_predi.npy')
    x=np.array([1,kwargs['categorie'],kwargs['viabilite'],kwargs['position']])
    y=x@B
    #coefficient de determination
    Y_moyenne=np.mean(Y)
    SCR=np.sum((Y-Y_predi)**2)
    SCT=np.sum((Y-Y_moyenne)**2)
    R2=1-(SCR/SCT)
    return {'prediction':float(y[0]),'coef_determination':R2}