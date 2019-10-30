from datetime import datetime

class game():
    def __init__(self, title : str, ts=None, plat=None):
        self.title = title
        self.beaten_timestamp = ts
        self.platform = plat
        self.comment = ""

    def set_comment(self, comment : str):
        self.comment = comment
    
    def set_platform(self, platform : str):
        self.platform = platform

if __name__ == "__main__":
    print(datetime.now())