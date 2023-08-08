from Stage import stage
from Setting import Setting
from Report import report
from Word import word
from turtle import Turtle,Screen
from tabulate import tabulate
import random
from turtle import Turtle,Screen

class mix:
    def Run(self):
            Stage = stage()
            screen = Screen()
            tao = Turtle()
            User = Stage.Loading()
            while True:
                Word = word()
                Report = report()
                List1, List2, List3, List4, List5 = Word.Question_list()
                List_of_set = [List1,List2,List3,List4,List5]

                Ran = random.choice(List_of_set)
                List_of_set.remove(Ran)
                Score, List = Setting.Play_One_round(Ran)
                Report.insert(User[0],Score)
                Dict_Score,Dict_JSON = Report.Load()
                Result = Report.Rep(User[0],Dict_JSON)
                if Result == "Yes":
                    pass
                elif Result == "No":
                    screen.bye()
                    print("LEADERBOARD")
                    print(tabulate(Dict_Score, headers='keys', tablefmt='fancy_grid'))            
                    break