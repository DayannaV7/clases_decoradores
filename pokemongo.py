from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class pokemones(BaseModel):
    id: int
    name: str 
    attack: int 
    life: int
    type: str

p1 = pokemones(id=1, name="bulbasaur", life=100, attack=15, type="grass")
p2 = pokemones(id=2, name="ivysaur", life=100, attack=16, type="grass")
p3 = pokemones(id=3, name="venusaur", life=100, attack=17, type="grass")
p4 = pokemones(id=4, name="charmander", life=100, attack=18, type="fire")
p5 = pokemones(id=5, name="charmeleon", life=100, attack=19, type="fire")
p6 = pokemones(id=6, name="charizard", life=100, attack=20, type="fire")
p7 = pokemones(id=7, name="squirtle", life=100, attack=15, type="water")
p8 = pokemones(id=8, name="wartortle", life=100, attack=16, type="water")
p9 = pokemones(id=9, name="blastoise", life=100, attack=17, type="water")
p10 = pokemones(id=10, name="caterpie", life=100, attack=10, type="bug")
p11 = pokemones(id=11, name="metapod", life=100, attack=11, type="bug")
p12 = pokemones(id=12, name="butterfree", life=100, attack=12, type="bug")
p13 = pokemones(id=13, name="weedle", life=100, attack=10, type="bug")
p14 = pokemones(id=14, name="kakuna", life=100, attack=11, type="bug")
p15 = pokemones(id=15, name="beedrill", life=100, attack=12, type="bug")
p16 = pokemones(id=16, name="pidgey", life=100, attack=13, type="normal")
p17 = pokemones(id=17, name="pidgeotto", life=100, attack=14, type="normal")
p18 = pokemones(id=18, name="pidgeot", life=100, attack=15, type="normal")
p19 = pokemones(id=19, name="rattata", life=100, attack=13, type="normal")
p20 = pokemones(id=20, name="raticate", life=100, attack=14, type="normal")
p21 = pokemones(id=21, name="spearow", life=100, attack=13, type="normal")
p22 = pokemones(id=22, name="fearow", life=100, attack=14, type="normal")
p23 = pokemones(id=23, name="ekans", life=100, attack=15, type="poison")
p24 = pokemones(id=24, name="arbok", life=100, attack=16, type="poison")
p25 = pokemones(id=25, name="pikachu", life=100, attack=16, type="electric")
p26 = pokemones(id=26, name="raichu", life=100, attack=17, type="electric")
p27 = pokemones(id=27, name="sandshrew", life=100, attack=15, type="ground")
p28 = pokemones(id=28, name="sandslash", life=100, attack=16, type="ground")
p29 = pokemones(id=29, name="nidoran-f", life=100, attack=14, type="poison")
p30 = pokemones(id=30, name="nidorina", life=100, attack=15, type="poison")
p31 = pokemones(id=31, name="nidoqueen", life=100, attack=16, type="poison")
p32 = pokemones(id=32, name="nidoran-m", life=100, attack=14, type="poison")
p33 = pokemones(id=33, name="nidorino", life=100, attack=15, type="poison")
p34 = pokemones(id=34, name="nidoking", life=100, attack=16, type="poison")
p35 = pokemones(id=35, name="clefairy", life=100, attack=12, type="fairy")
p36 = pokemones(id=36, name="clefable", life=100, attack=13, type="fairy")
p37 = pokemones(id=37, name="vulpix", life=100, attack=14, type="fire")
p38 = pokemones(id=38, name="ninetales", life=100, attack=15, type="fire")
p39 = pokemones(id=39, name="jigglypuff", life=100, attack=11, type="normal")
p40 = pokemones(id=40, name="wigglytuff", life=100, attack=12, type="normal")
p41 = pokemones(id=41, name="zubat", life=100, attack=13, type="poison")
p42 = pokemones(id=42, name="golbat", life=100, attack=14, type="poison")
p43 = pokemones(id=43, name="oddish", life=100, attack=13, type="grass")
p44 = pokemones(id=44, name="gloom", life=100, attack=14, type="grass")
p45 = pokemones(id=45, name="vileplume", life=100, attack=15, type="grass")
p46 = pokemones(id=46, name="paras", life=100, attack=13, type="bug")
p47 = pokemones(id=47, name="parasect", life=100, attack=14, type="bug")
p48 = pokemones(id=48, name="venonat", life=100, attack=13, type="bug")
p49 = pokemones(id=49, name="venomoth", life=100, attack=14, type="bug")
p50 = pokemones(id=104, name="cubone", life=100, attack=17, type="ground")


lista_pok: list[pokemones] = [p1, p2, p3, p4, p5, p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50]

@app.get("/showallpokemon/")
def all_pokemon():
    return lista_pok



   