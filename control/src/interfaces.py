from random import randint

from src.confdb import get_confdb_value, set_confdb_value


def beat() -> None:
    interfaces = get_confdb_value(
        "control-interfaces",
        fields=["stats"],
    )["stats"]

    for interface in interfaces.keys():
        # simulate packet flow
        up, down = randint(1, 10), randint(1, 10)
        interfaces[interface]["n-sent"] += up
        interfaces[interface]["n-received"] += down

        print(f"{interface}: {up} packets ↑, {down} packets ↓")

    set_confdb_value(
        "control-interfaces",
        {"stats": interfaces},
    )
