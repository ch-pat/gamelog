from gamelist import gamelist


def main():
    gl = gamelist()
    gl.import_from_backloggery("backlog_paste.txt")
    # TODO: implement ui and main logic
    return


if __name__ == "__main__":
    from gamelist import gamelist
    from game import game
