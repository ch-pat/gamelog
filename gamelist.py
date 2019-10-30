from datetime import datetime
from game import game
from bl_parser import bl_parser

class gamelist():
    def __init__(self, games : list, plats : list):
        self.gamelist = self.build_list(games, plats)

    def build_list(self, games : list, plats : list):
        result = []
        for el, pl in zip(games, plats):
            g = game(el, datetime.now(), pl)
            result += [g]
        return result

    def export_to_csv(self, outfile : str):
        output = "              \
                Title;          \
                Beaten on date; \
                Platform;       \
                Comment;        \
                \n              \
        "
        for g in self.gamelist:
            output += (
                str(g.title)            + "; " + 
                str(g.beaten_timestamp) + "; " + 
                str(g.platform)         + "; " + 
                str(g.comment)          + "; " +
                "\n"
            )
        
        with open(outfile, "w+", encoding="utf8") as f:
            f.write(output)
        return "Saved to file " + outfile    


if __name__ == "__main__":
    gl = gamelist([1,2,3,4], [5,6,7,8])
    print(gl.gamelist)
    for x in gl.gamelist:
        print(x.platform)
    gl.export_to_csv("prova.csv")