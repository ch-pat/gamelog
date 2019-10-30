import re

class bl_parser():

    def __init__(self):
        return
    
    def parse_titles_to_file(self, backlog_text, output_file):
        with open(backlog_text, "r", encoding="utf8") as file:
            content = file.read()
            content = content.splitlines()
            c = 0
            trimmed = ""
            for line in content:
                if re.match(r"[EUJ]\s\([uBbCcMmU-]\)", line):
                    game_name = line[6:]
                    print(c, game_name)
                    c += 1
                    trimmed += game_name + "\n"
            with open(output_file, "w+", encoding="utf8") as f:
                f.write(trimmed)

    
    def parse_to_gamelist(self, backlog_text : str):
        """Extracts a list of game titles
        returns a tuple containing the list of games and the respective list of platforms as strings
        """
        with open(backlog_text, "r", encoding="utf8") as file:
            content = file.read()
            content = content.splitlines()
            #c = 0
            games = []
            platforms = []
            for i, line in zip(range(len(content)), content):
                if re.match(r"[EUJ]\s\([uBbCcMmU-]\)", line):
                    game_name = line[6:]
                    plat = content[i+1].split()[0]
                    #print(c, game_name)
                    #c += 1
                    games += [game_name]
                    platforms += [plat] 
        return games, platforms

if __name__ == "__main__":
    parser = bl_parser()
    g, p = parser.parse_to_gamelist("backlog_paste.txt")
    print((g, p))
    print(len(g), len(p))

