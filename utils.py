from colored import fg as color

# Console Formats 
def successMsg(msg):
    print(f'{color("white")}[{color("green")}+{color("white")}] {color("light_blue")}{msg} {color("white")}')

def normalMsg(msg):
    print(f'{color("white")}[{color("yellow")}+{color("white")}] {msg} {color("white")}')

def errorMsg(msg):
    print(f'{color("white")}[{color("red")}+{color("white")}]{color("light_blue")} {msg} {color("white")}')

def bannerPrint():
    banner = f"""{color('red_1')}

/$$$$$$$                        /$$           /$$$$$$$                                         
| $$__  $$                      | $$          | $$__  $$                                        
| $$  \ $$ /$$   /$$  /$$$$$$$ /$$$$$$        | $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$/| $$  | $$ /$$_____/|_  $$_/        | $$$$$$$/ /$$__  $$ /$$_____/ /$$__  $$| $$__  $$
| $$__  $$| $$  | $$|  $$$$$$   | $$          | $$__  $$| $$$$$$$$| $$      | $$  \ $$| $$  \ $$
| $$  \ $$| $$  | $$ \____  $$  | $$ /$$      | $$  \ $$| $$_____/| $$      | $$  | $$| $$  | $$
| $$  | $$|  $$$$$$/ /$$$$$$$/  |  $$$$/      | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/ \______/ |_______/    \___/        |__/  |__/ \_______/ \_______/ \______/ |__/  |__/
                                                                                                
By: {color('green')}@Codins{color("white")}
    """
    print(banner)