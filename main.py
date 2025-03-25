from Types import ResultTypes
from Army import Army


def battle(army_1: Army, army_2: Army) -> None:
    if army_1.get_force_points() == army_2.get_force_points():
        # if there's a tie then pop a random unit from each army unit list
        army_1.append_battle(ResultTypes.TIE)
        army_1.pop_random_unit()

        army_2.append_battle(ResultTypes.TIE)
        army_2.pop_random_unit()

    elif army_1.get_force_points() > army_2.get_force_points():
        army_1.append_battle(ResultTypes.WIN)
        army_1.add_coins(100)

        army_2.append_battle(ResultTypes.LOSE)
        army_2.pop_two_max_points_units()

    elif army_1.get_force_points() < army_2.get_force_points():
        army_2.append_battle(ResultTypes.WIN)
        army_2.add_coins(100)

        army_1.append_battle(ResultTypes.LOSE)
        army_1.pop_two_max_points_units()