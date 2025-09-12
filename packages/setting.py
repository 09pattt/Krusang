import questionary
import time
from packages import system_console, system_json

class setting_json:
    def get_config():
        return system_json.read_json("./contents/setting.json")

class system_setting:
    def index():
        system_console.clear()
        print("")
        print("\33[44m\33[37m * System setting * \33[0m")
        print("")
        selection = questionary.select(
            "Setting option...",
            choices=[
                questionary.Choice(title="↩️ Return", value="return"),
                questionary.Choice(title="⭐️ General", value="general"),
                questionary.Choice(title="✨ Interface", value="interface"),
                questionary.Choice(title="🧑‍💻 Account", value="account")
            ]
        ).ask()
        if selection == "return":
            pass
        elif selection == "interface":
            system_setting.main_interface()
        else:
            print(selection)
        system_console.clear()
    
    def main_interface():
        system_console.clear()
        print("")
        print("\33[44m\33[37m * System setting * \33[0m")
        print("")
        config = setting_json.get_config()
        config = config["interface"]
        print(config)
        selection = questionary.checkbox(
            "✨Interface option",
            choices=[
                questionary.Choice(title= "📬 Show header above scanner", value="show_header", checked=config["show_header"]),
                questionary.Choice(title= "😄 Show emoji", value="emoji", checked=config["emoji"])
            ]
        ).ask()
        print(selection)
        questionary.press_any_key_to_continue().ask()
        
    def main_account():
        system_console.clear()
        print("")
        print("\33[44m\33[37m * System setting * \33[0m")
        print("")
        selection = questionary.select(
            "Interface setting option...",
            choices=[
                "Choice1",
                "Choice2",
                "Choice3",
                "Choice4"
            ]
        ).ask()
