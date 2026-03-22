CSV_FILE = "id.csv"  # This is for further testing
DB_FILE = "finance.db"
import csv
import os.path
import os


class Identification:
    @classmethod
    def add_user(cls, id, password):
        file_exists = os.path.isfile(CSV_FILE)
        with open(CSV_FILE, "a+") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "password"])
            if not file_exists:
                writer.writeheader()
            new_data = {"id": id, "password": password}
            writer.writerow(new_data)

    @classmethod
    def check_user(cls, id, password):
        try:
            with open(CSV_FILE, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["id"] == id and row["password"] == password:
                        return True
                return False
        except FileNotFoundError:
            print("No users registered")
            return False

    @classmethod
    def get_user(cls):
        try:
            with open(CSV_FILE, "r") as file:
                reader = csv.DictReader(file)
                return [i for i in reader]
        except FileNotFoundError:
            return

    @classmethod
    def remove_user(cls, id, password):
        file_exists_csv = os.path.isfile(CSV_FILE)
        file_exists_db = os.path.isfile(DB_FILE)

        while True:
            if cls.check_user(id, password):
                match input("Do you really want to delete the user and all the data? "):
                    case "yes":
                        if file_exists_csv:
                            os.remove("id.csv")
                        if file_exists_db:
                            os.remove(DB_FILE)
                        print("successfully deleted all the data")
                        break
                    case "no":
                        return
                    case _:
                        continue
            else:
                break