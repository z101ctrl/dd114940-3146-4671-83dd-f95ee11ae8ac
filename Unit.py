from Types import UnitTypes

UNIT_DATA: dict[UnitTypes, dict] = {
    UnitTypes.PIKEMAN: {
        "force_points": 5,
        "train_cost": 5,
        "transform_cost": 5,
        "training_increment": 3,
    },
    UnitTypes.ARCHER: {
        "force_points": 10,
        "train_cost": 7,
        "transform_cost": 5,
        "training_increment": 7,
    },
    UnitTypes.HORSEMAN: {
        "force_points": 20,
        "train_cost": 10,
        "transform_cost": None,
        "training_increment": 10,
    },
}


class Unit:

    def __init__(self, type: UnitTypes):
        self.__type: UnitTypes = type
        self.__force_points: int = UNIT_DATA[self.__type]["force_points"]
        self.__training_increment: int = UNIT_DATA[self.__type]["training_increment"]
        self.__train_cost: int = UNIT_DATA[self.__type]["train_cost"]
        self.__transform_cost: int = UNIT_DATA[self.__type]["transform_cost"]

    ###############
    # GET/SET
    ###############

    def get_type(self) -> UnitTypes:
        return self.__type

    def get_force_points(self) -> None:
        return self.__force_points

    def get_training_increment(self) -> int:
        return self.__training_increment

    def get_train_cost(self) -> int:
        return self.__train_cost

    def get_transform_cost(self) -> int:
        return self.__transform_cost

    ###############
    # OTHER METHODS
    ###############

    def train_unit(self) -> None:
        self.__force_points += self.__training_increment

    def transform(self) -> None:
        # assuming that all training is lost when transforming.
        if self.get_transform_cost() is None:
            raise Exception(f"[TRANSFORM] This unit cannot be transformed.")
        self.__init__(UnitTypes(self.get_type().value + 1))
