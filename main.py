import questionary
from packages import system_translate, system_console, system_time, system_json

#Application program
#Change directory to project => [On Shell : python3 app.py]

# On program start

main_loop = False



# Top level function

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
        else:
            print("")
            print("\33[43m\33[30m Termination cancelled \33[0m")

    def option():
        selection = questionary.select(
            "Option...",
            choices=[
                "Resume",
                "Clear",
                "Pause",
                "Manual",
                "Setting",
                "Terminate"
            ]
        ).ask()
        if selection == "Resume":
            pass
        elif selection == "Clear":
            system_console.clear()
        elif selection == "Pause":
            system_console.pause()
        elif selection == "Manual":
            command.manual()
        elif selection == "Setting":
            system_console.setting()
        elif selection == "Terminate":
            print("")
            command.quit()
        else :
            pass
    
    def manual(): # **เปลี่ยนเป็นเก็บข้อมูลไว้ใน .JSON และพิมพ์ออกด้วยการอ่านไฟล์
        dictionary = system_json.read_json("./contents/manual.json")
        command = dictionary["command"]
        manual = dictionary["manual"]
        for i in range(0, len(command)):
            print("\33[35m " + command[i] + " \33[0m - " + manual[i])
            



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
        system_console.datetime()
    elif cmd in {""}: # ขึ้นหน้าเมนู resume, preferrence, quit, pause
        command.option()
    elif cmd in {"pause", "stop"}:
        system_console.pause()
    elif cmd in {"setting"}:
        system_console.setting()
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

system_console.start() # clear console interface

system_console.datetime() # print header (datetime)

start_main_loop() # start main loop processing

print("")
print("\33[41m\33[37m * TERMINATED * \33[0m")
print("")