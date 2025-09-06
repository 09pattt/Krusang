import os
import json
import questionary
from datetime import datetime

#system_infra - system infrastructure function

class system_json:
    def read_json(path : str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)




#system_console - console interface

class system_console:
    def clear():
        os.system("clear")

    def pause():
        system_console.datetime()

    def start():
        system_console.clear()
        print("\33[43m\33[30m * KRUSANG by Metatosh™ * \33[0m")
        print("")
        print('Type "manual" for system manual.')
        print("")
        user = os.name
        if user == "posix":
            print("os : " + user + " (Unix-based)")
            print("\33[42m\33[30m Software compatible to system. ")
        else:
            print("os : " + user + " (Unknown)")
            print("\33[41m\33[37m Software incompatible to system. (\"posix\" system is requires) \33[0m")
        print("")
        key = questionary.press_any_key_to_continue("Press any key to continue... ").ask()
        system_console.clear()
        
        

    def datetime():
        now = system_time.now()
        print("\33[47m\33[30m" + str(now["hour"]) + ":" + str(now["minute"]) + ":" + str(now["second"]) + ":" + str(now["millisecond"]), system_translate.weekday(now["day"]), str(now["day"]), system_translate.month(now["month"]), str(now["year"]) + "\33[0m")



class system_translate:
    def month(month):
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return months[month]
    
    def weekday(day):
        weekday = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return weekday[day]
    
    def normalize(word):
        synonyms = {
            "quit": "quit",
            "exit": "quit",
            "terminate": "quit",

            "pause": "pause",
            "hold": "pause",
            "wait": "pause",

            "settings": "settings",
            "config": "settings",
            "options": "settings",
        }

        return synonyms.get(word, None)
    


now = datetime.now()

class system_time():
    def now():
        now = datetime.now()
        day = now.weekday()
        return {
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "hour": now.hour,
            "minute": now.minute,
            "second": now.second,
            "millisecond": now.microsecond // 1000,
            "microsecond": now.microsecond,
            "day": day
        }
    