from house.house_director import House_Director

# Exemplo casa normal

casa_normal = House_Director().build_default_house()
casa_normal.print()

# Exemplo Mansão

mansao = House_Director().build_mansion()
mansao.print()