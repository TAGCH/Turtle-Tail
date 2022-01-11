from turtle import Turtle,Screen
import time
tao = Turtle()
screen = Screen()
def Pen_down():
    tao.pendown()
def Pen_up():
    tao.penup()
def Clear():
    tao.clear()
def exit():
    screen.bye()

class stage:
    def Loading(self):
        screen.listen()
        screen.setup(width=1900,height=950,startx=0,starty=0)
        screen.onkey(fun=exit,key="q")
        screen.title("Turtle Tail")
        screen.bgcolor("black")
        screen.bgpic("Screen.png")
        tao.shape("turtle")
        tao.color("black")
        tao.hideturtle()
        tao.pen(fillcolor="black", pencolor="black", pensize=10)
        tao.penup()
        tao.setpos(-607,-313)
        tao.turtlesize(2,2,2)
        tao.showturtle()
        tao.pendown()
        tao.goto(603, -313)
        time.sleep(1)
        tao.hideturtle()
        screen.bgpic("Description.png")
        Name_list = []
        User = screen.textinput(title="Painter", prompt="Name of player 1: ")
        User2 = screen.textinput(title="Challenger", prompt="Name of player 2: ")
        if User2 in Name_list:
            while True:
                User2 = screen.textinput(title="This name has already used. Pls try again.", prompt="Name of player 2: ")
                if User2 in Name_list:
                    pass
                else:
                    Name_list.append(User2)
                    break
        else:
            Name_list.append(User2)
        screen.bgpic("BG.png")
        screen.reset()
        tao.reset()
        return Name_list

    def Set_stage(self):
        screen.listen()
        screen.bgcolor("black")
        tao.shape("turtle")
        tao.color("white")
        tao.turtlesize(2,2,2)
        tao.pen(fillcolor="white", pencolor="white", pensize=5)
        tao.penup()
        tao.heading()
        tao.speed("fastest")
        tao.ondrag(fun=tao.goto,btn=1,add=False)
        screen.onkey(fun=Pen_down,key="p")
        screen.onkey(fun=Pen_up,key="u")
        screen.onkey(fun=Clear,key="c")
        screen.onkey(fun=exit,key="q")





