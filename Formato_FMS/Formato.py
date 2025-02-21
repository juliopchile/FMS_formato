from enum import Enum
from typing import Union
import numpy as np
from Rondas import Ronda, RondaConBonos


class FormatoType(Enum):
    FMS_First = 0   # Primera jornada de la Temporada 1
    FMS_T1 = 1      # Temporada 1
    FMS_T2 = 2      # Temporada 2
    FMS_T3 = 3      # Temporada 3


class RondaType(Enum):
    EASYMODE = 1
    HARDMODE = 2
    TEMATICA = 3
    RANDOM = 4
    MINUTO_SANGRE = 5
    MINUTO_RESPUESTA = 6
    DELUXE = 7
    REPLICA = 8

class Batalla:
    def __init__(self, formato: FormatoType, rapper_1="MC1", rapper_2="MC2") -> None:
        self.rounds = []
        self.rapper1 = rapper_1,
        self.rapper2 = rapper_2,
        self.init_rounds_from_format(formato)
   
    def init_rounds_from_format(self, formato):
        if formato == FormatoType.FMS_T1:       # FMS Temporada 1
            self.rounds = [
                Ronda(largo=6, rapper=self.rapper1),    # EasyMode MC1
                Ronda(largo=6, rapper=self.rapper2),    # EasyMode MC2
                Ronda(largo=6, rapper=self.rapper2),    # HardMode MC2
                Ronda(largo=6, rapper=self.rapper1),    # HardMode MC1
                Ronda(largo=4, rapper=self.rapper1),    # Temática1 MC1
                Ronda(largo=4, rapper=self.rapper2),    # Temática1 MC2
                Ronda(largo=4, rapper=self.rapper2),    # Temática2 MC2
                Ronda(largo=4, rapper=self.rapper1),    # Temática2 MC1
                Ronda(largo=6, rapper=self.rapper1),    # PersonajesContarpuestos MC1
                Ronda(largo=6, rapper=self.rapper2),    # PersonajesContarpuestos MC2
                Ronda(largo=6, rapper=self.rapper2),            # Minuto a sangre MC2
                RondaConBonos(largo=6, rapper=self.rapper1),    # Minuto de respuesta MC1
                Ronda(largo=6, rapper=self.rapper1),            # Minuto a sangre MC1
                RondaConBonos(largo=6, rapper=self.rapper2),    # Minuto de respuesta MC2
                Ronda(largo=9, rapper=self.rapper2),    # Deluxe MC2
                Ronda(largo=9, rapper=self.rapper1),    # Deluxe MC1
            ]
        elif formato == FormatoType.FMS_T2:     # FMS Temporada 2
            self.rounds = [
                Ronda(largo=6, rapper=self.rapper1),    # EasyMode MC1
                Ronda(largo=6, rapper=self.rapper2),    # EasyMode MC2
                Ronda(largo=6, rapper=self.rapper2),    # HardMode MC2
                Ronda(largo=6, rapper=self.rapper1),    # HardMode MC1
                Ronda(largo=4, rapper=self.rapper1),    # Temática1 MC1
                Ronda(largo=4, rapper=self.rapper2),    # Temática1 MC2
                Ronda(largo=4, rapper=self.rapper2),    # Temática2 MC2
                Ronda(largo=4, rapper=self.rapper1),    # Temática2 MC1
                Ronda(largo=6, rapper=self.rapper1),    # PersonajesContarpuestos MC1
                Ronda(largo=6, rapper=self.rapper2),    # PersonajesContarpuestos MC2
                Ronda(largo=6, rapper=self.rapper2),            # Minuto a sangre MC2
                RondaConBonos(largo=6, rapper=self.rapper1),    # Minuto de respuesta MC1
                Ronda(largo=6, rapper=self.rapper1),            # Minuto a sangre MC1
                RondaConBonos(largo=6, rapper=self.rapper2),    # Minuto de respuesta MC2
                Ronda(largo=9, rapper=self.rapper2),    # Deluxe MC2
                Ronda(largo=9, rapper=self.rapper1),    # Deluxe MC1
            ]

