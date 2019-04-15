def Get_Events(file_name):
    import xml.etree.ElementTree as ET
    import pandas as pd
    import os
    import glob
    import numpy as np
    tree = ET.ElementTree(file = file_name)
    gameFile = tree.getroot()
    
    #Import Game Data
    main_list = []

    for game in gameFile:
        away_team = game.attrib.get("away_team_id")
        print (away_team)
        home_team = game.attrib.get("home_team_id")
        print (home_team)
        for Event in game:
             for q in Event:
                 qualifier = q.attrib.get("qualifier_id")
                 if qualifier == "277":
                     half = Event.attrib.get("period_id")
                     if half == "1":
                         Stoppage_1 = (q.attrib.get("value"))
                     if half == "2":
                         Stoppage_2 = (q.attrib.get("value"))
                 event_listing = {"Y": Event.attrib.get("y"), 
                                  "X": Event.attrib.get("x"),
                                  "Outcome": Event.attrib.get("outcome"),
                                  "Team ID": Event.attrib.get("team_id"),
                                  "Player ID": Event.attrib.get("player_id"),
                                  "Sec": Event.attrib.get("sec"),
                                  "Minute": Event.attrib.get("min"),
                                  "Period ID": Event.attrib.get("period_id"),
                                  "Type ID": Event.attrib.get("type_id"),
                                  "Event ID": Event.attrib.get("event_id"),
                                  "Qualifier ID": q.attrib.get("qualifier_id"),
                                  "Value": q.attrib.get("value")}
                 main_list.append(event_listing)     
    event_df = pd.DataFrame(main_list)
    event_df.loc[(event_df["Team ID"] == away_team), "Home/Away"] = 0
    event_df.loc[(event_df["Team ID"] == home_team), "Home/Away"] = 1

    event_df.to_clipboard()    
    return (event_df)



