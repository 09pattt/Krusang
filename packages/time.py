from datetime import datetime

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

    def show_datetime():
        now = system_time.now()
        print(str(now["day"]) + "/" + str(now["month"]) + "/" + str(now["year"]) + " | " + str(now["hour"]) + ":" + str(now["minute"]) + ":" + str(now["second"]) + ":" + str(now["millisecond"]))