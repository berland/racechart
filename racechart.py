import pandas as pd
import time

DISTANCES = {
    "1 km": 1000,
    "200 m": 200,
    "400 m": 400,
    "3000 m": 3000,
    "5 km": 5000,
    "10 km": 10000,
    "1/2 M": 21097.5,
    "Marathon": 42195,
}


def racechart(startsec=4 * 60, endsec=5 * 60):
    dframe = pd.DataFrame()
    dframe["seconds_pr_km"] = range(startsec, endsec + 1)
    for distance_name, length in DISTANCES.items():
        dframe[distance_name] = (dframe["seconds_pr_km"] * length / 1000.0).apply(
            prettyprintseconds
        )

    dframe["km/t"] = (60 * 60 / dframe["seconds_pr_km"]).round(2)
    return dframe.drop("seconds_pr_km", axis=1)


def prettyprintseconds(seconds):
    seconds = round(seconds)
    if seconds < 60 * 60:
        return time.strftime("%-M:%S", time.gmtime(seconds))
    return time.strftime("%-H:%M:%S", time.gmtime(seconds))


assert prettyprintseconds(0) == "0:00"
assert prettyprintseconds(60) == "1:00"
assert prettyprintseconds(61) == "1:01"

print(racechart().to_latex(column_format="c" * (len(DISTANCES) + 1), index=False))
