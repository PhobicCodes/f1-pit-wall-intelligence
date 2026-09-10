from f1_pit_wall.data import load_race
from f1_pit_wall.cleaning import select_pace_columns, add_lap_time_seconds, filter_pace_laps

from f1_pit_wall.analysis import get_driver_laps, stint_summary

def main():
    year = 2026
    event = "Italian Grand Prix"
    driver = "ANT"  
    
    print(f"Loading {year} {event}...")
    
    session = load_race(year, event, "cache")
    laps = select_pace_columns(session.laps)
    laps = add_lap_time_seconds(laps)
    pace_laps = filter_pace_laps(laps)
    driver_laps = get_driver_laps(pace_laps, driver)
    
    summary = stint_summary(driver_laps)
    print()
    print(f"{driver} stint summary")
    print(summary)
    
    
if __name__ == "__main__":
    main()
    