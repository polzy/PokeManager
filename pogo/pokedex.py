import inspect


class Pokedex(dict):

    # Enum pokemonIds
    MISSINGNO = 0
    BULBIZARRE = 1
    HERBIZARRE = 2
    FLORIZARRE = 3
    SALAMECHE = 4
    REPTINCEL = 5
    DRACAUFEU = 6
    CARAPUCE = 7
    CARABAFFE = 8
    TORTANK = 9
    CHENIPAN = 10
    CHRYSACIER = 11
    PAPILUSION = 12
    ASPICOT = 13
    COCONFORT = 14
    DARDARGNAN = 15
    ROUCOOL = 16
    ROUCOUPS = 17
    ROUCARNAGE = 18
    RATTATA = 19
    RATTATAC = 20
    PIAFABEC = 21
    RAPASDEPIC = 22
    ABO = 23
    ARBOK = 24
    PIKACHU = 25
    RAICHU = 26
    SABELETTE = 27
    SABLAIREAU = 28
    NIDORAN_FEMALE = 29
    NIDORINA = 30
    NIDOQUEEN = 31
    NIDORAN_MALE = 32
    NIDORINO = 33
    NIDOKING = 34
    MELOFEE = 35
    MELODELFE = 36
    GOUPIX = 37
    FEUNARD = 38
    RONDOUDOU = 39
    GRODOUDOU = 40
    NOSFERAPTI = 41
    NOSFERALTO = 42
    MYSTHERBE = 43
    ORTIDE = 44
    RAFFLESIA = 45
    PARAS = 46
    PARASECT = 47
    MIMITOSS = 48
    AEROMITE = 49
    TAUPIQUEUR = 50
    TRIOPIKEUR = 51
    MIAOUSS = 52
    PERSIAN = 53
    PSYKOKWAK = 54
    AKWAKWAK = 55
    FEROSINGE = 56
    COLOSSINGE = 57
    CANINOS = 58
    ARCANIN = 59
    PTITARD = 60
    TETARTE = 61
    TARTARD = 62
    ABRA = 63
    KADABRA = 64
    ALAKAZAM = 65
    MACHOC = 66
    MACHOPEUR = 67
    MACKOGNEUR = 68
    CHETIFLOR = 69
    BOUSTIFLOR = 70
    EMPIFLOR = 71
    TENTACOOL = 72
    TENTACRUEL = 73
    RACAILLOU = 74
    GRAVALANCH = 75
    GOLEM = 76
    PONYTA = 77
    GALOPA = 78
    RAMOLOSS = 79
    FLAGADOSS = 80
    MAGNETI = 81
    MAGNETON = 82
    CANARTICHO = 83
    DODUO = 84
    DODRIO = 85
    OTARIA = 86
    LAMANTINE = 87
    TADMORV = 88
    GROTADMORV = 89
    KOKIYAS = 90
    CRUSTABRI = 91
    FANTOMINUS = 92
    SPECTRUM = 93
    ECTOPLASMA = 94
    ONIX = 95
    SOPORIFIK = 96
    HYPNOMADE = 97
    KRABBY = 98
    KRABBOSS = 99
    VOLTORBE = 100
    ELECTRODE = 101
    NOEUNOEUF = 102
    NOADKOKO = 103
    OSSELAIT = 104
    OSSATUEUR = 105
    HITMONLEE = 106
    TYGNON = 107
    EXCELANGUE = 108
    SMOGO = 109
    SMOGOGO = 110
    RHINOCORNE = 111
    RHINOFEROS = 112
    LEVEINARD = 113
    SAQUEDENEU = 114
    KANGOUREX = 115
    HYPOTREMPE = 116
    HYPOCEAN = 117
    POISSIRENE = 118
    POISSOROY = 119
    STARI = 120
    STAROSS = 121
    MR_MIME = 122
    INSECATEUR = 123
    LIPPOUTOU = 124
    ELEKTEK = 125
    MAGMAR = 126
    SCARABRUTE = 127
    TAUROS = 128
    MAGICARPE = 129
    LEVIATOR = 130
    LOKHLASS = 131
    METAMORPH = 132
    EVOLI = 133
    AQUALI = 134
    VOLTALI = 135
    PYROLI = 136
    PORYGON = 137
    AMONITA = 138
    AMONISTAR = 139
    KABUTO = 140
    KABUTOPS = 141
    PTERA = 142
    RONFLEX = 143
    ARTIKODIN = 144
    ELECTHOR = 145
    SULFURA = 146
    MINIDRACO = 147
    DRACO = 148
    DRACOLOSSE = 149
    MEWTWO = 150
    MEW = 151

    rarity = {}
    evolves = {}

    def __init__(self):
        super(dict, self).__init__(self)

        # Some reflection, based on uppercase consts.
        attributes = inspect.getmembers(Pokedex, lambda attr :not(inspect.isroutine(attr)))
        for attr in attributes:
            if attr[0].isupper():
                self[attr[1]] = attr[0]

        # Ideally go back and lint for line lengths
        self.rarity[Rarity.MYTHIC] = [self.MEW]
        self.rarity[Rarity.LEGENDARY] = [
            self.ELECTHOR, self.SULFURA, self.MEWTWO, self.ARTIKODIN
        ]
        self.rarity[Rarity.EPIC] = [
            self.METAMORPH, self.FLORIZARRE, self.TAUROS, self.DRACOLOSSE, self.MELODELFE,
            self.DRACAUFEU, self.TORTANK
        ]
        self.rarity[Rarity.VERY_RARE] = [
            self.BOUSTIFLOR, self.CARABAFFE, self.RAFFLESIA, self.EMPIFLOR,
            self.AEROMITE, self.AQUALI, self.FLAGADOSS, self.RAICHU, self.TARTARD,
            self.SCARABRUTE, self.ROUCARNAGE, self.AMONISTAR, self.NIDOQUEEN, self.NIDOKING,
            self.GROTADMORV, self.OSSATUEUR, self.LOKHLASS, self.KANGOUREX, self.KABUTOPS, self.HERBIZARRE,
            self.LEVIATOR, self.GOLEM, self.ECTOPLASMA, self.NOADKOKO, self.DRACO, self.LAMANTINE,
            self.REPTINCEL, self.DARDARGNAN, self.ALAKAZAM
        ]
        self.rarity[Rarity.RARE] = [
            self.GRODOUDOU, self.SMOGOGO, self.TENTACRUEL, self.SAQUEDENEU,
            self.STAROSS, self.RONFLEX, self.INSECATEUR, self.POISSOROY, self.HYPOCEAN,
            self.RHINOFEROS, self.GALOPA, self.COLOSSINGE, self.PORYGON, self.TETARTE,
            self.PARASECT, self.ONIX, self.AMONITA, self.FEUNARD, self.NIDORINO,
            self.NIDORINA, self.MR_MIME, self.MAGMAR, self.MACHOPEUR, self.MACKOGNEUR,
            self.EXCELANGUE, self.KRABBOSS, self.VOLTALI, self.HYPNOMADE, self.TYGNON,
            self.ORTIDE, self.AKWAKWAK, self.PYROLI, self.RAPASDEPIC, self.CANARTICHO,
            self.ELEKTEK, self.TRIOPIKEUR, self.MINIDRACO, self.DODRIO, self.CRUSTABRI,
            self.LEVEINARD, self.PAPILUSION, self.ARCANIN, self.PTERA
        ]
        self.rarity[Rarity.UNCOMMON] = [
            self.GOUPIX, self.TENTACOOL, self.STARI, self.CARAPUCE, self.PIAFABEC,
            self.KOKIYAS, self.OTARIA, self.SABLAIREAU, self.RHINOCORNE, self.RATTATAC,
            self.PSYKOKWAK, self.PONYTA, self.PIKACHU, self.ROUCOUPS, self.PERSIAN,
            self.CHRYSACIER, self.MAGNETON, self.SMOGO, self.KADABRA, self.KABUTO,
            self.COCONFORT, self.LIPPOUTOU, self.RONDOUDOU, self.HYPOTREMPE, self.HITMONLEE,
            self.SPECTRUM, self.CANINOS, self.TADMORV, self.GRAVALANCH, self.NOSFERALTO,
            self.NOEUNOEUF, self.ELECTRODE, self.OSSELAIT, self.MELOFEE, self.SALAMECHE,
            self.BULBIZARRE, self.ARBOK, self.ABRA
        ]
        self.rarity[Rarity.COMMON] = [
            self.ASPICOT, self.VOLTORBE, self.MIMITOSS, self.RAMOLOSS, self.SABELETTE,
            self.PTITARD, self.PARAS, self.MYSTHERBE, self.NIDORAN_MALE, self.NIDORAN_FEMALE,
            self.MIAOUSS, self.FEROSINGE, self.MAGNETI, self.MAGICARPE, self.MACHOC, self.KRABBY,
            self.POISSIRENE, self.RACAILLOU, self.FANTOMINUS, self.EVOLI, self.ABO, self.SOPORIFIK,
            self.DODUO, self.TAUPIQUEUR, self.CHENIPAN, self.CHETIFLOR
        ]
        self.rarity[Rarity.CRITTER] = [self.NOSFERAPTI, self.ROUCOOL, self.RATTATA]

        self.evolves = {
            self.MISSINGNO: 0, self.BULBIZARRE: 25, self.HERBIZARRE: 100, self.FLORIZARRE: 0,
            self.SALAMECHE: 25, self.REPTINCEL: 100, self.DRACAUFEU: 0, self.CARAPUCE: 25,
            self.CARABAFFE: 100, self.TORTANK: 0, self.CHENIPAN: 12, self.CHRYSACIER: 50,
            self.PAPILUSION: 0, self.ASPICOT: 12, self.COCONFORT: 50, self.DARDARGNAN: 0, self.ROUCOOL: 12,
            self.ROUCOUPS: 50, self.ROUCARNAGE: 0, self.RATTATA: 25, self.RATTATAC: 0, self.PIAFABEC: 50,
            self.RAPASDEPIC: 0, self.ABO: 50, self.ARBOK: 0, self.PIKACHU: 50, self.RAICHU: 0,
            self.SABELETTE: 50, self.SABLAIREAU: 0, self.NIDORAN_FEMALE: 25, self.NIDORINA: 100,
            self.NIDOQUEEN: 0, self.NIDORAN_MALE: 25, self.NIDORINO: 100, self.NIDOKING: 0,
            self.MELOFEE: 50, self.MELODELFE: 0, self.GOUPIX: 50, self.FEUNARD: 0, self.RONDOUDOU: 50,
            self.GRODOUDOU: 0, self.NOSFERAPTI: 50, self.NOSFERALTO: 0, self.MYSTHERBE: 25, self.ORTIDE: 100,
            self.RAFFLESIA: 0, self.PARAS: 50, self.PARASECT: 0, self.MIMITOSS: 50, self.AEROMITE: 0,
            self.TAUPIQUEUR: 50, self.TRIOPIKEUR: 0, self.MIAOUSS: 50, self.PERSIAN: 0, self.PSYKOKWAK: 50,
            self.AKWAKWAK: 0, self.FEROSINGE: 50, self.COLOSSINGE: 0, self.CANINOS: 50, self.ARCANIN: 0,
            self.PTITARD: 25, self.TETARTE: 100, self.TARTARD: 0, self.ABRA: 25, self.KADABRA: 100,
            self.ALAKAZAM: 0, self.MACHOC: 25, self.MACHOPEUR: 100, self.MACKOGNEUR: 0, self.CHETIFLOR: 25,
            self.BOUSTIFLOR: 100, self.EMPIFLOR: 0, self.TENTACOOL: 50, self.TENTACRUEL: 0,
            self.RACAILLOU: 25, self.GRAVALANCH: 100, self.GOLEM: 0, self.PONYTA: 50, self.GALOPA: 0,
            self.RAMOLOSS: 50, self.FLAGADOSS: 0, self.MAGNETI: 50, self.MAGNETON: 0, self.CANARTICHO: 0,
            self.DODUO: 50, self.DODRIO: 0, self.OTARIA: 50, self.LAMANTINE: 0, self.TADMORV: 50, self.GROTADMORV: 0,
            self.KOKIYAS: 50, self.CRUSTABRI: 0, self.FANTOMINUS: 25, self.SPECTRUM: 100, self.ECTOPLASMA: 0,
            self.ONIX: 0, self.SOPORIFIK: 50, self.HYPNOMADE: 0, self.KRABBY: 50, self.KRABBOSS: 0, self.VOLTORBE: 50,
            self.ELECTRODE: 0, self.NOEUNOEUF: 50, self.NOADKOKO: 0, self.OSSELAIT: 50, self.OSSATUEUR: 0,
            self.HITMONLEE: 0, self.TYGNON: 0, self.EXCELANGUE: 0, self.SMOGO: 50, self.SMOGOGO: 0,
            self.RHINOCORNE: 50, self.RHINOFEROS: 0, self.LEVEINARD: 0, self.SAQUEDENEU: 0, self.KANGOUREX: 0,
            self.HYPOTREMPE: 50, self.HYPOCEAN: 0, self.POISSIRENE: 50, self.POISSOROY: 0, self.STARI: 50, self.STAROSS: 0,
            self.MR_MIME: 0, self.INSECATEUR: 0, self.LIPPOUTOU: 0, self.ELEKTEK: 0, self.MAGMAR: 0, self.SCARABRUTE: 0,
            self.TAUROS: 0, self.MAGICARPE: 400, self.LEVIATOR: 0, self.LOKHLASS: 0, self.METAMORPH: 0, self.EVOLI: 25,
            self.AQUALI: 0, self.VOLTALI: 0, self.PYROLI: 0, self.PORYGON: 0, self.AMONITA: 50, self.AMONISTAR: 0,
            self.KABUTO: 50, self.KABUTOPS: 0, self.PTERA: 0, self.RONFLEX: 0, self.ARTIKODIN: 0,
            self.ELECTHOR: 0, self.SULFURA: 0, self.MINIDRACO: 25, self.DRACO: 100, self.DRACOLOSSE: 0,
            self.MEWTWO: 0, self.MEW: 0
        }

    def getRarityByName(self, name):
        return self.RarityById(self[name])

    def getRarityById(self, pokemonId):
        for rarity in self.rarity:
            if pokemonId in self.rarity[rarity]:
                return rarity


class Rarity(object):
    CRITTER = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4
    EPIC = 5
    LEGENDARY = 6
    MYTHIC = 7

pokedex = Pokedex()
