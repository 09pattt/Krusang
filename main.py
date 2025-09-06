import questionary
from packages import system_translate, system_time, system_console

#Application program
#Change directory to project => [On Shell : python3 app.py]

# On program start

main_loop = False



# Top level function

def command_line_header():
    now = system_time.now()
    print("\33[47m\33[30m" + str(now["hour"]) + ":" + str(now["minute"]) + ":" + str(now["second"]) + ":" + str(now["millisecond"]), system_translate.weekday(now["day"]), str(now["day"]), system_translate.month(now["month"]), str(now["year"]) + "\33[0m")

def scan_cmd(indicator):
    return input(indicator + "\33[33m >> ").lower().replace(" ", "")

def start_main_loop():
    global main_loop
    main_loop = True
    do_main_loop()

def break_main_loop():
    global main_loop
    main_loop = False




#Command function

class command:
    def quit():
        selection = questionary.select(
            "Terminate this program?",
            choices=[
                "Yes",
                "No"
            ]
        ).ask()
        if selection == "Yes":
            break_main_loop()
    
    def manual(): # **เปลี่ยนเป็นเก็บข้อมูลไว้ใน .JSON และพิมพ์ออกด้วยการอ่านไฟล์
        print("quit - to break main_loop then program terminate.")
        print("man - to open manual page (this page).")
        print("clear - clear console and print header.")
        print("option - to open options selection menu.")



#Error function

class error:
    def undefined():
        print("\33[41m\33[37m Encountered to undefined error. \33[0m")

    def no_command(cmd):
        print("\33[41m\33[37m >>" + cmd + "<< is out of bound. \33[0m")



#Command line

def command_line(cmd):
    if cmd in {"quit", "exit", "terminate"}:
        command.quit()
    elif cmd in {"clear", "cl"}:
        system_console.clear()
    elif cmd in {"manual", "man"}:
        command.manual()
    elif cmd in {"time", "date", "datetime"}:
        system_time.show_datetime()
    elif cmd in {""}:
        pass
    else:
        error.no_command(cmd)



# Main loop processing

def do_main_loop():
    global main_loop
    while main_loop:
        print("")
        cmd = scan_cmd("")
        print("\033[0m")
        command_line(cmd)



#System cycle

system_console.clear() # clear console interface

command_line_header() # print header (datetime)

start_main_loop() # start main loop processing

print("")
print("\33[43m\33[30m * KRUSANG by Metatosh™ * ")
print("")