from datetime import datetime
from datetime import timedelta


class game():
    def __init__(self, title: str, started_ts: datetime = datetime.now(),
                 beaten_ts: datetime = None, plat: str = "",
                 comment: str = ""):
        self.title = title
        self.started_timestamp = started_ts
        self.beaten_timestamp = beaten_ts if beaten_ts is not None else ""
        self.platform = plat
        self.comment = comment
        self.in_game_play_time = ""  # Should be a timedelta object

    def set_comment(self, comment: str):
        self.comment = comment

    def set_platform(self, platform: str):
        self.platform = platform

    def get_fields(self):
        return [self.title, self.started_timestamp, self.beaten_timestamp,
                self.in_game_play_time, self.platform, self.comment]

    def __str__(self):
        return (
                str(self.title) + "; " +
                str(self.started_timestamp.date()) + "; " +
                str(self.beaten_timestamp) + "; " +
                str(self.in_game_play_time) + "; " +
                str(self.platform) + "; " +
                str(self.comment) + "; " +
                "\n"
        )


if __name__ == "__main__":
    print(timedelta(hours=157, minutes=14))
    g = game(title="Boku no piccolo", started_ts=datetime.now(),
             plat="NintendomegaDS")
    print(g)
