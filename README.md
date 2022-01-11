# TURTLE TAIL
## Project overview and features
This project is a game that can play 2 players. Player one is a painter. The painter will draw the picture following the word that shows on the screen by the limited time by dragging the mouse then player 2 is a challenger will guess the word from the picture. Finally, the program will report the score. 

## Required libraries and tools
* Python 3.10.0 (Not fixed)
[Download lastest version] (https://www.python.org/)

### Import
* csv
* json
* turtle
* numpy
* tkinter
* pyautogui
* timer
* tabulate

## Program design
 * `Stage class` -- set the loading page, receive the user information, and prepare the turtle. 
 * `Word class` -- read the CSV file and return the list of question.
 * `Setting class` -- use to play the game in one round. 
 * `Report class` -- read the score file then return the score.
 * `Mix class` -- mix all of the classes into one attribute and show the leaderboard.

## Code structure 
 * `BG.png` -- Backgroung picture
 * `Description.png` -- Description picture
 * `Screen.png` -- Screen picture
 * `Score.json` -- Keep the user information
 * `Word.csv` -- Keep the  question
 * `Stage.py` -- Stage class
 * `Word.py` -- Word class
 * `Setting.py` -- Setting class
 * `Report.py` -- Report class
 * `Mix.py` -- Mix class
 * `main.py` -- Run program

Thank you for reading :}