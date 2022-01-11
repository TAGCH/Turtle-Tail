import json
import pyautogui
from tabulate import tabulate

class report:
    def insert(self, Player, Score_list):
        score = Score_list.count(1)
        new_data = {Player:score}
        try:
            with open("Score.json", "r") as data_file:
                Data = json.load(data_file)
        except FileNotFoundError:
            with open ("Score.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            Data.update(new_data)
            with open ("Score.json", "w") as data_file:
                json.dump(Data, data_file, indent=4)

    def Load(self):
        with open("Score.json", encoding="utf8") as f:
            String_JSON = f.read()
            Dict_JSON = json.loads(String_JSON)
        Sort_Dict = {k: v for k, v in sorted(Dict_JSON.items(), key= lambda v: v[1])}
        List_Name = list(Sort_Dict.keys())
        List_Score = list(Sort_Dict.values())
        List_Name1 = List_Name[::-1]
        List_Score1 = List_Score[::-1]
        Dict_Score = {}
        Dict_Score["Name"] = List_Name1
        Dict_Score["Score"] = List_Score1 
        return Dict_Score, Dict_JSON
        
    def Rep(self, Name, Dict_JSON):
        Result_Play = pyautogui.confirm(text=f"Your score is {Dict_JSON[Name]}.\nDo you want to play again?",title=f"{Name}'s score!",buttons=("Yes","No"))
        return Result_Play
