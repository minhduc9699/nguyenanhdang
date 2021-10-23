from turtle import *
speed(-1)

number_of_edge = int(input('enter number of edge: '))

for i in range(number_of_edge):
    forward(100)
    left(360/number_of_edge)

mainloop()