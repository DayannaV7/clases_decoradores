from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class pokemon(BaseModel):
    id: int
    nombre: str
    vida: int
    ataque: int
    vivo: bool

p1 = pokemon(id=1, nombre="bulbasaur", vida=100, ataque=15,vivo=True)
p2 = pokemon(id=25,nombre="pikachu",vida=100,ataque=16,vivo=True)
p3 = pokemon(id=50,nombre="cubone",vida=100,ataque=17,vivo=True)

new_pokemon: list[pokemon] = [p1,p2,p3]   

pokemon_db = [
    {"name":"bulbasaur"},
    {"name":"cubone"},
    {"name":"pikachu"},
    {"name":"gengar"},
    {"name":"charizard"},
]

@app.get("/allpokemon/")
def show_all_pokemon():
    return new_pokemon

@app.get("/onepokemon/")
def show_one_pokemon(pos:int):
    for pokemon in new_pokemon:
        if(pokemon.id==pos):
            return pokemon
        else:
            return {"pokemon no encontrado"}
    
@app.get("/pokemon/")
def show_pokemon(skip: int=0, limit: int=3):
    return pokemon_db[skip:skip+limit]

@app.get("/Dayanna")
def dayanna():
    return {"dayanna": 1+2}

@app.get("/suma/{a}/{b}")
def sumar(a, b):
    res = int(a)+int(b)
    return {"la suma da: ": res}

@app.get("/edad/{n}/{yo}")
def edad(n,yo):
    anio_actual = date.today().year
    anio_nacimiento = int(n)
    edad1 = int(anio_actual) - int(anio_nacimiento)
    nombre = str(yo)
    return {"mi nombre es:": nombre}
#datos estaticos datos tipados estaticamente