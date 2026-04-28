import numpy as np
# la premiere colonne contient les un pour la valeur de terrain si toute les variables 
# sont a wero la deuxieme colonne pour les categories sachant que les valeur des cagtegories sont les 
# centres les prix moyenne de chaque categorie en millier
# la troisieme pour la proximite par rapport a la route <=50 vaut 3, >50 et <=100 vaut 2 et >100 vaut
# la quatrieme pour la viabilite quit peut avoir les valeurs(0,1,2,3)

# X=np.array([[1,20,550,5],
#          [1,20,350,7],
#          [1,20,300,9],
#          [1,40,270,10],
#          [1,40,278,14],
#          [1,40,190,12],
#          [1,60,200,13],
#          [1,60,222,10],
#          [1,60,220,11],
#          [1,150,200,12],
#          [1,150,160,14],
#          [1,150,120,16],
#          [1,380,90,16],
#          [1,380,80,18],
#          [1,380,40,19],])

# Y=np.array([[15000],
#            [23000],
#            [30000],
#            [35000],
#            [40000],
#            [50000],
#            [55000],
#            [80000],
#            [100000],
#            [120000],
#            [170000],
#            [200000],
#            [320000],
#            [400000],
#            [500000],])

# B=np.linalg.inv((X.T)@X)@(X.T@(Y))
# print(B)
# print(np.linalg.det(X.T @ X)) 

X=np.array([[1,4,6,6],
           [1,4,5,6],
           [1,4,5,5],
           [1,4,5,4],
           [1,3,4,5],
           [1,3,4,4],
           [1,3,3,4],
           [1,3,3,3],
           [1,2,2,4],
           [1,2,2,3],
           [1,2,1,3],
           [1,2,2,1],
           [1,2,1,2],
           [1,1,0,1],
           [1,1,1,1],
           [1,1,0,2],])

Y=np.array([[110000],
           [100000],
           [95000],
           [90000],
           [75000],
           [70000],
           [65000],
           [60000],
           [45000],
           [42000],
           [40000],
           [38000],
           [35000],
           [22000],
           [25000],
           [20000],])

B=np.linalg.inv((X.T)@X)@((X.T)@Y)
Y_predi=X@B
#coefficient de determination
Y_moyenne=np.mean(Y)
SCR=np.sum((Y-Y_predi)**2)
SCT=np.sum((Y-Y_moyenne)**2)
R2=1-(SCR/SCT)

def prediction():
    pass

# print(B)
# print(X@B)

if __name__=="__main__":
    # cat,viabilite,position=input('entrer  respectivement le score(en entier) de :categorie , viabilite, position par rapport a l axe principal.Puis le status titre(=1) ou non titre(=0)').split()
    # y=np.array([1,int(cat),int(viabilite),int(position)])
    # Valeur=y@B
    # print(f"la valeur de votre terrain est d'environ{Valeur}")
    # print(f"R^2={R2} {SCR} {SCT}")
    np.save('matrice_B.npy',B)
    np.save('matrice_Y.npy',Y)
    np.save('matrice_X.npy',X)
    np.save('matrice_Y_predi.npy',Y_predi)