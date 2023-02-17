import platform

def about():
    s_color = "\033[92m" if platform.system() != "Windows" else ""
    e_color = "\033[0m" if platform.system() != "Windows" else ""
    about = f"""{s_color}

            Blackzsploit Framework
            Author : BlackLeakz
            Contact : blueleakz96@outlook.de
            Project Github : https://github.com/blackleakz/blackzsploit
            Other Projects : https://github.com/blackleakz

    {e_color}"""
    print(about)
