import os
import fastf1
# enable cache and load session
def load_race(year, event, cache_dir):
    os.makedirs(cache_dir,exist_ok = True)
    
    fastf1.Cache.enable_cache(cache_dir)
    session = fastf1.get_session(
        year,
        event,
        "R"
    )
    session.load()
    
    return session