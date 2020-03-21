# gamelog
Log your beaten games and display your gaming statistics

WIP CLI application for managing your game library locally, in its infant stage.
Features will include: 
* Optional backup to Google Drive Spreadsheet
* Display of various statistics such as:
   * Games beaten during a certain month/year
   * Games added during a certain month/year
   * Total playtime and by month/year
   * Games added by month
* Importing from backloggery.com (by literally manually copying-all your list from the website to a text file)
* More as they come to mind

Currently running main imports your list from a "backlog_paste.txt" file and allows for adding by manually running python functions in a python shell like this:
```python
python3 -i application/main.py
>>> gl = gamelist()
Reading existing backlog.csv file
>>> gl += game("The Legend of Zelda", platform="NES", comment="Classic!")
```
