from datetime import datetime
from application.game import game
from application import bl_parser
import csv
import os


class gamelist():
    def __init__(self, games: list = [], platforms: list = [],
                 outfile: str = "backlog.csv"):
        self._games = games
        self._platforms = platforms

        self.outfile = outfile
        self.fiels_string = "Title;Started on date;Beaten on date;" + \
                            "In game time;Platform;Comment"
        self.fields = self.fiels_string.split(sep=";")
        self.gamelist = self.build_list()
        self.export_to_csv()

    def build_list(self):
        """Used for building the list on launch
        """
        if self.outfile not in os.listdir():
            # Initialize list from input
            print("Creating " + self.outfile + " file")
            result = []
            for el, pl in zip(self._games, self._platforms):
                g = game(el, datetime.now(), pl)
                result += [g]
            return result
        else:
            # Read list from file
            print("Reading existing " + self.outfile + " file")
            result = []
            with open(self.outfile, "r") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                for row in reader:
                    if row != self.fields:
                        result += [
                            game(row[0], datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f"),
                                 row[2], row[4], row[5])
                            ]
            return result

    def export_to_csv(self):
        with open(self.outfile, "w+") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(self.fields)
            writer.writerows([g.get_fields() for g in self.gamelist])
        return "Saved gamelist to file " + self.outfile

    def import_from_backloggery(self, input_file):
        # This overwrites any previously entered entry and
        # should only be used on first run
        print("Importing list from backloggery file...")
        parser = bl_parser.bl_parser()
        self._games, self._platforms = parser.parse_txt_to_gamelist(input_file)
        result = []
        for g, p in zip(self._games, self._platforms):
            result += [game(g, plat=p)]
        self.gamelist = result
        self.export_to_csv()
        print("Importing complete.")

    def add_game(self, g: game):
        self.gamelist += [g]
        with open(self.outfile, "a") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(g.get_fields())

    def __add__(self, g: game):
        self.add_game(g)
        return self

    def __str__(self):
        return (f"List contains "
                f"{len(self.gamelist)} games\nLast added: {self.gamelist[-1]}")


if __name__ == "__main__":
    gl = gamelist([1, 2, 3, 4], [5, 6, 7, 8])
    print(gl.gamelist)
    for x in gl.gamelist:
        print(x.platform)
    print(gl)
    gl = gl + game("Grangianni")
    gl.add_game(game("Gianni"))
    gl.__add__(game("omegagianni"))
    print(gl)
