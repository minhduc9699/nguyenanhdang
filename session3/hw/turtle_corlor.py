from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)
# for edge in range(3, 8):
#     color(colors[edge - 3])
#     for i in range(edge):
#         forward(100)
#         left(360/edge)

for i in range(5):
    color(colors[i])
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)
mainloop()