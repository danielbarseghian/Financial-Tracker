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
    print("║  " + Fore.WHITE + "[1] Login to account" + Fore.CYAN + "    ║")
    print("║  " + Fore.WHITE + "[2] Create an account" + Fore.CYAN + "   ║")
    print("║  " + Fore.WHITE + "[3] Delete an account" + Fore.CYAN + "   ║")
    print("║  " + Fore.WHITE + "[4] Quit" + Fore.CYAN + "                ║")
    print("╚══════════════════════════╝" + Style.RESET_ALL)

    while True:
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
            case "3":
                Identification.remove_user(input("name: "), input("password: "))
                continue
            case "4":
                sys.exit(0)
            case _:
                print("Please enter a number from 1 to 4")
                continue


def main():
    login()
    print(Fore.MAGENTA + "╔══════════════════════════╗")
    print("║        LOGIN MENU        ║")
    print("╠══════════════════════════╣")
    print("║  " + Fore.WHITE + "[1] Add transaction" + Fore.MAGENTA + "     ║")
    print("║  " + Fore.WHITE + "[2] Show transactions" + Fore.MAGENTA + "   ║")
    print("║  " + Fore.WHITE + "[3] Delete a trasaction" + Fore.MAGENTA + " ║")
    print("║  " + Fore.WHITE + "[4] Quit" + Fore.MAGENTA + "                ║")
    print("╚══════════════════════════╝" + Style.RESET_ALL)

    con = sqlite3.connect("finance.db")
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT,
        date        TEXT,
        description TEXT,
        type        TEXT,
        amount      REAL
    )"""
    )

    while True:
        ch = input("Choose (1-4): ").strip().lower()
        match ch:

            case "1" | "delete":

                cur.execute(
                    """INSERT OR IGNORE INTO transactions VALUES(?, ?, ?, ?, ?, ?)""",
                    (
                        generate_random(10),
                        input("What is the name of the pushace? "),
                        get_date(),
                        input("Short description of the pushace. "),
                        input("What type of pushace was this? "),
                        input("How much was this transaction? "),
                    ),
                )

            case "2" | "show":

                for row in cur.execute("""SELECT * FROM transactions"""):
                    print(row)

            case "3" | "delete":

                d = input("What do you want to delete? ")
                cur.execute("DELETE FROM transactions WHERE name = ?", (d,))

            case "4" | "quit":

                sys.exit(0)

            case _:
                print("What ??")

        con.commit()


main()
