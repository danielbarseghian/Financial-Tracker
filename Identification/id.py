CSV_FILE = "id.csv"  # This is for further testing
import csv
import os.path


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
            print("No users registered")
            return

    @classmethod
    def remove_user(cls, id, password):
        try:

            if cls.check_user(id, password):

                with open(CSV_FILE, "r") as f:

                    reader = csv.DictReader(f)
                    new_data = [i for i in reader if i["id"] != id]

                    with open(CSV_FILE, "w") as file:

                        writer = csv.DictWriter(file, fieldnames=["id", "password"])
                        writer.writeheader()

                        for row in new_data:
                            writer.writerow(row)
                        print("Successfully removed user! ")

            else:
                print("Invalid username or password")

        except FileNotFoundError:
            print("File does not exist")
