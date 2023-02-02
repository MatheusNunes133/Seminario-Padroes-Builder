from .house_interface import Home_Interface
from .house import House

class House_Builder(Home_Interface):
    
    def __init__(self) -> None:
        self.house_builder = House()

    def setQtdeWalls(self, qtde_paredes):
        self.house_builder.home["qtde_paredes"] = qtde_paredes
        return self
    
    def setWallType(self, tipo_parede):
        self.house_builder.home["tipo_parede"] = tipo_parede
        return self

    def setFloorType(self, tipo_piso):
        self.house_builder.home["tipo_piso"] = tipo_piso
        return self

    def setPoolVolume(self, volume_piscina):
        self.house_builder.home["volume_piscina"] = volume_piscina
        return self

    def setGardemType(self, tipo_jardim):
        self.house_builder.home["tipo_jardim"] = tipo_jardim
        return self

    def setRoofType(self, tipo_teto):
        self.house_builder.home["tipo_teto"] = tipo_teto
        return self

    def setWindowType(self, tipo_janela):
        self.house_builder.home["tipo_janela"] = tipo_janela
        return self

    def setQtdeWindow(self, qtde_janela):
        self.house_builder.home["qtde_janela"] = qtde_janela
        return self

    def build(self):
        return self.house_builder