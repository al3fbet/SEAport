# This opening readme will be added at a later date

# Modules imported
import os
import sys
import datetime
import socket
import terminology



# Program name / banner
string_port = """
  █████████  ██████████   █████████                                 █████      
 ███░░░░░███░░███░░░░░█  ███░░░░░███                               ░░███       
░███    ░░░  ░███  █ ░  ░███    ░███  ████████   ██████  ████████  ███████     
░░█████████  ░██████    ░███████████ ░░███░░███ ███░░███░░███░░███░░░███░      
 ░░░░░░░░███ ░███░░█    ░███░░░░░███  ░███ ░███░███ ░███ ░███ ░░░   ░███       
 ███    ░███ ░███ ░   █ ░███    ░███  ░███ ░███░███ ░███ ░███       ░███ ███   
░░█████████  ██████████ █████   █████ ░███████ ░░██████  █████      ░░█████    
 ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░  ░███░░░   ░░░░░░  ░░░░░        ░░░░░     
                                      ░███                                     
                                      █████                                    
                                     ░░░░░                                     
  █████████                                                                    
 ███░░░░░███                                                                   
░███    ░░░   ██████   ██████   ████████                                       
░░█████████  ███░░███ ░░░░░███ ░░███░░███                                      
 ░░░░░░░░███░███ ░░░   ███████  ░███ ░███                                      
 ███    ░███░███  ███ ███░░███  ░███ ░███                                      
░░█████████ ░░██████ ░░████████ ████ █████                                     
 ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░  v1.0                                     
                                                                               

                created by: al3fbet 
                
                visit: https://al3fbet.github.io
                       https://www.hackersforjesus.xyz

                            ~ HAK 4 JESUS ~
"""

# printing banner 
# Email me or reach out if you think I can make this program better
print(string_port)

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
clear()
