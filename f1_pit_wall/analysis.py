# functiont to return driver's laps
def get_driver_laps(laps, driver):
    driver_laps = laps[laps["Driver"] == driver].copy()
    return driver_laps

# stint summary 
def stint_summary(laps):
    summary = (
        laps.groupby(["Driver", "Stint", "Compound"]).agg(
            Laps=("LapNumber", "count"),
            MeanLapTime=("LapTimeSeconds", "mean"),
            MedianLapTime=("LapTimeSeconds", "median"),
            FastestLap=("LapTimeSeconds", "min"),
            StartTyreLife=("TyreLife", "min"),
            EndTyreLife=("TyreLife", "max")
        )
        .reset_index()
    )

    return summary              