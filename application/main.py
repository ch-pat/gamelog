from bl_parser import bl_parser
from gamelist import gamelist


def main():
    parser = bl_parser()
    games, plats = parser.parse_to_gamelist("backlog_paste.txt")
    gl = gamelist(games, plats)
    gl.export_to_csv("backlog.csv")


if __name__ == "__main__":
    main()
