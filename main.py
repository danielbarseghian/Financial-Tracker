DB_FILE = "finance.db"
import sqlite3
import sys
from Identification.id import Identification
from random import randint
from datetime import date
from colorama import Fore, Style, init
from tabulate import tabulate

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
    while True:
        print(Fore.CYAN + "╔══════════════════════════╗")
        print("║        LOGIN MENU        ║")
        print("╠══════════════════════════╣")
        print("║  " + Fore.WHITE + "[1] Login to account" + Fore.CYAN + "    ║")
        print("║  " + Fore.WHITE + "[2] Create an account" + Fore.CYAN + "   ║")
        print("║  " + Fore.WHITE + "[3] Delete an account" + Fore.CYAN + "   ║")
        print("║  " + Fore.WHITE + "[4] Quit" + Fore.CYAN + "                ║")
        print("╚══════════════════════════╝" + Style.RESET_ALL)
        choice = input("  Choose (1-4): ")

        match choice:
            case "1":
                id = input("name: ")
                if Identification.check_user(id, input("password: ")):
                    return id
                else:
                    print("Account not existante")
                    continue
            case "2":
                if Identification.get_user() is None or len(Identification.get_user()) == 0:
                    while True:
                        id = input("name: ")
                        password = input("password: ")
                        if not Identification.check_user(
                            id, password
                        ):  # If user none existante
                            Identification.add_user(id, password)
                            return id
                        else:
                            print("User already existante")
                else:
                    print("An account is already created please delete it to create a new one")
                    continue                    
            case "3":
                Identification.remove_user(input("name: "), input("password: "))
                continue
            case "4" | "quit":
                sys.exit(0)
            case _:
                print("Please enter a number from 1 to 4")
                continue


def main():
    login()

    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT,
        date        TEXT,
        description TEXT,
        amount      REAL
    )"""
    )

    while True:
        print(Fore.MAGENTA + "╔══════════════════════════╗")
        print("║        LOGIN MENU        ║")
        print("╠══════════════════════════╣")
        print("║  " + Fore.WHITE + "[1] Add transaction" + Fore.MAGENTA + "     ║")
        print("║  " + Fore.WHITE + "[2] Show transactions" + Fore.MAGENTA + "   ║")
        print("║  " + Fore.WHITE + "[3] Delete a trasaction" + Fore.MAGENTA + " ║")
        print("║  " + Fore.WHITE + "[4] Quit" + Fore.MAGENTA + "                ║")
        print("╚══════════════════════════╝" + Style.RESET_ALL)
        ch = input("Choose (1-4): ").strip().lower()
        match ch:

            case "1" | "delete":

                cur.execute(
                    """INSERT OR IGNORE INTO transactions VALUES(?, ?, ?, ?, ?)""",
                    (
                        generate_random(10),
                        input("What is the name of the pushace? "),
                        get_date(),
                        input("Short description of the pushace. "),
                        input("How much was this transaction? "),
                    ),
                )

            case "2" | "show":

                content = cur.execute("""SELECT * FROM transactions""")
                headers = [i[0] for i in cur.description]
                print(tabulate(content, headers, tablefmt="grid"))   
                input("Press enter to continue :")                 

            case "3" | "delete":

                d = input("What do you want to delete? ")
                cur.execute("DELETE FROM transactions WHERE name = ?", (d,))
                print("succesfully deleted the transaction")

            case "4" | "quit":

                sys.exit(0)

            case _:
                print("What ??")

        con.commit()


main()
