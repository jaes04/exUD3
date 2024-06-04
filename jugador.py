MAX_ENERGY = 100
MIN_ENERGY = 0


class Player:
    def __init__(self, idPlayer, nickName):
        self.__idPlayer = idPlayer
        self.__nickName = nickName
        self.__energy = (MAX_ENERGY - MIN_ENERGY) / 2

    def getIdPLayer(self):
        return self.__idPlayer

    def getNickName(self):
        return self.__nickName

    def getEnergy(self):
        return self.__energy

    def setIdPlayer(self, idPlayer):
        self.__idPlayer = idPlayer

    def setNickName(self, nickName):
        self.__nickName = nickName

    def __setEnergy(self, energy):
        self.__energy = energy

    def toString(self):
        return f"[{self.getIdPLayer()},{self.getNickName()},{self.getEnergy()}]"

    def boost(self, charge):
        self.__setEnergy(self.getEnergy() + charge)

        if isinstance(charge, int):
            if self.getEnergy() > MAX_ENERGY:
                self.__setEnergy(MAX_ENERGY)
            elif self.getEnergy() < MIN_ENERGY:
                self.__setEnergy(MIN_ENERGY)

        return charge, self.getEnergy()
