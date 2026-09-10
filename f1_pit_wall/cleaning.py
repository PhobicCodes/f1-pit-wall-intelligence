# clean the dataframe, select important info for my analysis

PACE_COLUMNS = [
    "Driver",
    "LapNumber",
    "LapTime",
    "Stint",
    "Compound",
    "TyreLife",
    "FreshTyre",
    "PitInTime",
    "PitOutTime",
    "TrackStatus",
    "Position",
    "IsAccurate"
]

def select_pace_columns(laps):
    return laps[PACE_COLUMNS].copy()

# make laptime readable from fastf1 template to normal seconds to calculate stats
def add_lap_time_seconds(laps):
    laps = laps.copy()
    laps["LapTimeSeconds"] = laps["LapTime"].dt.total_seconds()
    return laps

def filter_pace_laps(laps):
    pace_laps = laps[
        laps["LapTime"].notna()
        & laps["IsAccurate"]
        & laps["PitInTime"].isna()
        & laps["PitOutTime"].isna()
        & (laps["TrackStatus"] == "1")
    ].copy()
    
    return pace_laps