from Stage import stage
from turtle import Turtle,Screen
import pyautogui
tao = Turtle()
tao2 = Turtle()
screen = Screen()
Stage = stage()

class Setting:
    def Play_One_round(List):
        List_ = []
        Color_list = ["aquamarine","royal blue","navy","green","yellow green","gold","indian red","firebrick","red","black"]
        for j in range(0,len(List)):
            screen.title(List[j])
            pyautogui.alert(title=f"{j+1}/10",text=f"{j+1} out of 10")
            pyautogui.alert(title=f"{j+1}/10",text=f"{List[j]}")
            Stage.Set_stage()
            tao2.hideturtle()
            tao2.penup()
            tao2.shape("turtle")
            tao2.pen(fillcolor=Color_list[j], pencolor=Color_list[j], pensize=3)
            tao2.setpos(-875,410)
            tao2.right(90)
            tao2.speed("normal")
            #tao2.speed("slowest")
            tao2.showturtle()
            tao2.pendown()
            tao2.goto(-875,-410)
            tao2.left(90)
            tao2.goto(875,-410)
            tao2.left(90)
            tao2.goto(875,410)
            tao2.left(90)
            tao2.goto(-875,410)
            tao2.left(90)
            if tao2.pos() == (-875,410):
                screen.title("Guess!")
                Answer = screen.textinput(title="Guess!",prompt="Answer = ")
                if Answer.upper() == List[j]:
                    List_.append(1)
                else:
                    List_.append(0)        
            else:
                pass
        return List_,List




