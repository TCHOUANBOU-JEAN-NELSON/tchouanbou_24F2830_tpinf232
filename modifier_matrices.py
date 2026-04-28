import numpy as np



def modifier(list1,list2):
    Y=np.load('matrice_Y.npy')
    X=np.load('matrice_X.npy')
    x=np.array(list1)
    y=np.array(list2)
    X_maj=np.vstack((X,x))
    Y_maj=np.vstack((Y,y))
    B=np.linalg.inv((X_maj.T)@X_maj)@((X_maj.T)@Y_maj)
    Y_predi=X_maj@B
    #coefficient de determination
    Y_moyenne=np.mean(Y_maj)
    SCR=np.sum((Y_maj-Y_predi)**2)
    SCT=np.sum((Y_maj-Y_moyenne)**2)
    R2=1-(SCR/SCT)
    if (R2<1 and R2>0):
        np.save('matrice_B.npy',B)
        np.save('matrice_Y.npy',Y_maj)
        np.save('matrice_X.npy',X_maj)
        np.save('matrice_Y_predi.npy',Y_predi)
        return {'message':"modele entrainee","coef_determination":R2}
    else:
        return{"message":"l'ajout de ces valeurs fausse notre regression"}