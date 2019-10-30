from bl_parser import bl_parser
from gamelist import gamelist

if __name__ == "__main__":
    parser = bl_parser()
    games, plats = parser.parse_to_gamelist("backlog_paste.txt")
    gl = gamelist(games, plats)
    gl.export_to_csv("backlog.csv")
    
