from enum import Enum
from typing import Union
import numpy as np


class Ronda:
    def __init__(self,
                largo: int,
                rapper: str = "MC",
                intervenciones=None,
                skills: float = None,
                flow: float = None,
                puesta_en_escena: float = None,
                total: float = None):
        self.rapper = rapper
        self.interventions = np.zeros(largo) if intervenciones is None else np.array(intervenciones)
        self.casilla_skills = 0 if skills is None else skills
        self.casilla_flow = 0 if flow is None else flow
        self.casilla_escena = 0 if puesta_en_escena is None else puesta_en_escena
        self.total = self.add_total() if total is None else total

    def add_intervenciones(self, intervenciones):
        self.interventions = np.array(intervenciones)

    def add_skill(self, skill):
        self.casilla_skills = skill
    
    def add_flow(self, flow):
        self.casilla_flow = flow

    def add_puesta_en_escena(self, escena):
        self.casilla_escena = escena

    def add_casillas_extras(self, casillas):
        self.add_skill(casillas[0])
        self.add_flow(casillas[1])
        self.add_puesta_en_escena(casillas[2])

    def add_total(self) -> float:
        return self.interventions.sum() + self.casilla_skills + self.casilla_flow + self.casilla_escena


class RondaConBonos(Ronda):
    def __init__(self,
                largo: int,
                rapper: str = "MC",
                intervenciones=None,
                skills: float = None,
                flow: float = None,
                puesta_en_escena: float = None,
                total: float = None,
                bonos=None):
        super().__init__(largo, rapper, intervenciones, skills, flow, puesta_en_escena, total)  # Llama al constructor de la superclase
        self.casillas_bono = np.zeros(largo) if bonos is None else np.array(bonos)

    def add_bonos(self, bonos):
        self.bonos = np.array(bonos)
