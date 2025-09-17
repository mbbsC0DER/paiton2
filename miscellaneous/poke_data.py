import requests 

base_url ="https://pokeapi.co/api/v2"
def get_pokemon_data(name):
    final_url = f"{base_url}/pokemon/{name}"
    response = requests.get(final_url)
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else :
        print (f"Failed to retrieve data : {response.status_code}")

poke_name = input("Enter pokemon : ")
poke_info = get_pokemon_data(poke_name)
if poke_info :
    print ("\tPokemon data")
    # print (poke_info)
    print (f'Name : {poke_info["name"]}\nHeight : {poke_info["height"]}\nID : {poke_info["id"]}')
else :
    pass
