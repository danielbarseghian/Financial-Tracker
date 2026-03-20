import sqlite3
import sys
from Identification.id import Identification
from random import randint
from datetime import date
from colorama import Fore, Style, init
init()

def generate_random(n):
    s = ""
    for _ in range(n):
        r = randint(0, 9)
        s = f"{s}{r}"
    return s

def get_date():
    return date.today()

def login():
    print(Fore.CYAN + "╔══════════════════════════╗")
    print("║        LOGIN MENU        ║")
    print("╠══════════════════════════╣")
    print("║  " + Fore.RED + "[1] Login to account" + Fore.CYAN + "    ║")
    print("║  " + Fore.BLUE + "[2] Create an account" + Fore.CYAN + "   ║")
    print("║  " + Fore.YELLOW + "[3] Quit" + Fore.CYAN + "                ║")
    print("╚══════════════════════════╝" + Style.RESET_ALL)
    choice = input("  Choose (1-3): ")

    match choice:
        case "1":
            return Identification.check_user(input("name: "), input("password: "))
        case "2":
            Identification.add_user(input("name: "), input("password: "))
        case "3":
            return
def main():

    con = sqlite3.connect("finance.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT,
        date        TEXT,
        description TEXT,
        type        TEXT,
        amount      REAL
    )''')

    while True:
        match input().lower().strip():

            case "add":

                cur.execute('''INSERT OR IGNORE INTO transactions VALUES(?, ?, ?, ?, ?, ?)''',(
                            generate_random(10),
                            input("What is the name of the pushace? "),
                            get_date(),
                            input("Short description of the pushace. "),
                            input("What type of pushace was this? "),
                            input("How much was this transaction? ")))
                
            case "show":

                for row in cur.execute('''SELECT * FROM transactions'''):
                    print(row)
            
            case "delete":
                
                d = input("What do you want to delete? ")
                cur.execute("DELETE FROM transactions WHERE name = ?", (d,))

            case "quit":
                sys.exit(0)

            case _:
                print("What ??")

        con.commit()

print(login())