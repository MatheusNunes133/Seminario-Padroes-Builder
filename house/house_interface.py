from abc import ABC, abstractmethod

class Home_Interface(ABC):

    @abstractmethod
    def setQtdeWalls(qtde_paredes):
        pass

    @abstractmethod
    def setWallType(tipo_parede):
        pass

    @abstractmethod
    def setFloorType(tipo_piso):
        pass

    @abstractmethod
    def setPoolVolume(volume_piscina):
        pass

    @abstractmethod
    def setGardemType(tipo_jardim):
        pass

    @abstractmethod
    def setRoofType(tipo_teto):
        pass

    @abstractmethod
    def setWindowType(tipo_janela):
        pass

    @abstractmethod
    def setQtdeWindow(qtde_janela):
        pass
