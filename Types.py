from enum import Enum


class ResultTypes(Enum):
    TIE = 0
    WIN = 1
    LOSE = 2


class UnitTypes(Enum):
    PIKEMAN = 0
    ARCHER = 1
    HORSEMAN = 2


class CivTypes(Enum):
    CHINESE = 0
    ENGLISH = 1
    BYZANTINES = 2
