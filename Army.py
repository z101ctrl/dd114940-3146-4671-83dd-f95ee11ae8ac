from typing import List
from Types import CivTypes, UnitTypes, ResultTypes
from Unit import Unit
from random import randint


CIV_DATA: dict[CivTypes, dict] = {
    CivTypes.CHINESE: {
        UnitTypes.PIKEMAN: 2,
        UnitTypes.ARCHER: 25,
        UnitTypes.HORSEMAN: 2,
    },
    CivTypes.ENGLISH: {
        UnitTypes.PIKEMAN: 10,
        UnitTypes.ARCHER: 10,
        UnitTypes.HORSEMAN: 10,
    },
    CivTypes.BYZANTINES: {
        UnitTypes.PIKEMAN: 5,
        UnitTypes.ARCHER: 8,
        UnitTypes.HORSEMAN: 15,
    },
}


class Army:

    def __init__(self, type: CivTypes):
        self.__coins: int = 1000
        self.__type: CivTypes = type
        self.__battles: List[ResultTypes] = []
        force_points, units = self.__initialize_units()
        self.__force_points: int = force_points
        self.__units: List[Unit] = units

    def __initialize_units(self) -> tuple[int, List[Unit]]:
        units = []
        force_points = 0

        for unit_type, amount in CIV_DATA[self.get_type()].items():
            for _ in range(amount):
                unit = Unit(unit_type)
                units.append(unit)
                force_points += unit.get_force_points()
        units.sort(key=lambda x: x.get_force_points())
        return force_points, units

    ###############
    # GET/SET
    ###############
    def get_type(self) -> CivTypes:
        return self.__type

    def get_coins(self) -> int:
        return self.__coins

    def set_coins(self, coins: int) -> None:
        self.__coins = coins

    def get_force_points(self) -> List[Unit]:
        return self.__force_points

    def set_force_points(self, force_points: int) -> None:
        self.__force_points = force_points

    def get_units(self) -> List[Unit]:
        return self.__units

    ###############
    # OTHER METHODS
    ###############
    def append_battle(self, result: ResultTypes) -> None:
        self.__battles += [result]

    def add_coins(self, coins: int) -> None:
        self.set_coins(self.get_coins() + coins)

    def pop_two_max_points_units(self) -> None:
        for _ in range(2):
            unit = self.__units.pop()
            self.set_force_points(self.get_force_points() - unit.get_force_points())

    def pop_random_unit(self) -> None:
        unit = self.__units.pop(randint(0, len(self.__units)))
        self.set_force_points(self.get_force_points() - unit.get_force_points())

    def transform_unit(self, unit: UnitTypes) -> None:
        transform_cost = unit.get_transform_cost()
        if self.__coins >= transform_cost:
            try:
                old_unit_points = unit.get_force_points()
                unit.transform()
                self.set_force_points(
                    self.get_force_points()
                    + (unit.get_force_points() - old_unit_points)
                )
                self.__coins -= transform_cost
            except Exception as e:
                raise e
        else:
            raise Exception(f"[TRANSFORM] Not enough funds.")

    def train_unit(self, unit: UnitTypes) -> None:
        train_cost = unit.get_train_cost()
        if self.__coins >= train_cost:
            self.__coins -= train_cost
            unit.train_unit()
            self.set_force_points(
                self.get_force_points() + unit.get_training_increment()
            )
        else:
            raise Exception(f"[TRAIN] Not enough funds.")
