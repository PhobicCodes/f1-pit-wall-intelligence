# F1 Pit-Wall Intelligence System

This is an in-progress Formula 1 data project using Python, FastF1, and pandas.

I started by exploring FastF1 and understanding the availale race, lap, tyre, and stint data. The current version can load a race, filter laps for basic pace analysis and produce a simple stint summary for a selected driver.


## Current features:
- load race session with FastF1
- Cache race data locally
- Select useful lap and tyre data
- Convert lap times to seconds for analysis/calculations
- filter out laps that are not useful for normal pace analysis
- Filter out by driver
- Create basic stint summaries with average, median, and fastest lap times.


I used the 2026 Italian Grand Prix as the current test/demo

## Running it
Install the requirements:
```bash
pip install -r requirements.txt
```
Then run:
```bash
python main.py
```

## Next steps (Planned features)
- analysing more races and seasons
- better pace and tyre degradation analysis
- storing processed data in SQL
- building simple predictive models 
- startegy and pit-window simulation
- adding a user interface later