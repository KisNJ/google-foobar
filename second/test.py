superheroes=["Spiderman","Superman"]
universe=["Marvel","DC"]
interat=list(zip(superheroes,universe))
print(list(interat))
listoftuples=[('Spiderman', 'Marvel'), ('Superman', 'DC')]
for hero,universe in interat:
    print(hero,universe)
