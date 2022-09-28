#code to genrate the data
# from turtle import Turtle,Screen
# import pandas as pd
#
#
# turtle = Turtle()
# screen = Screen();
# screen.setup(width=700,height=600)
# screen.bgpic('./asset/labeled.png')
#
#
# state_name=[]
# x_coor=[]
# y_coor=[]
#
# exit = False
# def get_mouse_click_coor(x,y):
#    print(x,y)
#    input = screen.textinput("Enter the state name", "value")
#
#    if input == "exit":
#       states_dict = {
#          'state':state_name,
#          'x_coor':x_coor,
#          'y_coor':y_coor
#       }
#       states_df = pd.DataFrame(states_dict)
#       states_df.to_csv('states.csv')
#    else:
#       cleaned = input.capitalize()
#       print(cleaned)
#       turtle.penup()
#       turtle.goto(x, y)
#       turtle.pendown()
#       turtle.color("red")
#       turtle.write(cleaned, align="right", move=True, font=("Verdana",
#                                                             7, "normal"), )
#       state_name.append(cleaned)
#       x_coor.append(int(x))
#       y_coor.append(int(y))
#
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()


import turtle
from turtle import Turtle,Screen
import  pandas


file = pandas.read_csv("states.csv")



screen = Screen()
screen.title("NIGERIA STATE GAME")

img_path='./asset/blank.png'
screen.bgpic(img_path)



inputed_states=[]
missing_states=[]





state_column= file["state"].to_list()

while len(inputed_states) < 36:
    input = turtle.textinput(f"{len(inputed_states)}/36 GUESSED CORRECTLY", "Enter A State Name")

    input = input.capitalize()
    if input == "Exit":
        for state in state_column:
            if state not in inputed_states:
                missing_states.append(state)
        missing_states_dict = {
            'state': missing_states
        }
        missing_states_df = pandas.DataFrame(missing_states_dict)
        missing_states_df.to_csv('missing_states.csv')
        break
    if input in state_column:
        inputed_states.append(input)


        selected_state = file[file["state"] == input]
        t=Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(selected_state["x_coor"]),int(selected_state["y_coor"]))
        t.write(input)

# def get_mouse_click_cooor(x,y):
#     print(x,y)
#
#
# turtle.onscreenclick(get_mouse_click_cooor)
#
# turtle.mainloop()

