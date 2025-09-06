import os

#system_console - 

class system_console:
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

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