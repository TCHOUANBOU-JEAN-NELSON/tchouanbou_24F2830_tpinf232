from fastapi import FastAPI,Query
from typing import Annotated
from modele_prediction import prediction 
from modifier_matrices import modifier
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Autorise tout pour le test local
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/prediction")
def get_prediction(categorie:int=2,viabilite:int=5,position:int=5):
    donnee={
        'categorie':categorie,
        'viabilite':viabilite,
        'position':position
    }
    predi=prediction(**donnee)
    return predi

@app.get("/entrener")
def entrener(categorie:int=2,viabilite:int=5,position:int=5,valeur:int=5000):
    donnee={
        'categorie':categorie,
        'viabilite':viabilite,
        'position':position,
        'valeur':valeur
    }
    modif=modifier([1,categorie,viabilite,position],[valeur])
    return modif
