from .house_builder import House_Builder

class House_Director(House_Builder):

    def __init__(self):
        self.builder = House_Builder()

    def build_default_house(self):
        self.builder.setQtdeWalls(4).setWallType("Pedra").setFloorType("Cerâmica").setRoofType("Telha Normal")
        self.builder.setQtdeWalls(2).setWindowType("Vidro")
        return self.builder.build()

    def build_mansion(self):
        self.builder.setQtdeWalls("25").setWallType("Pedra Polida").setFloorType("Mármore").setGardemType("Rosas")
        self.builder.setPoolVolume("2.500.000L").setRoofType("Telha Especial").setQtdeWindow(10).setWindowType("Vidro")
        return self.builder.build()