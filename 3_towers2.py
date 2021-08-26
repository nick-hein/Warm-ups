##############################################################################
#   a113_TR_tower_3colors.py
#   Example solution:
#     Multiple towers with 3 alternative colors every three floors
##############################################################################
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of turlte
x = -200
y = -100

# height of tower and a counter for each "floor"
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.color("gray")
  # modifed code 
  # new color when the remainder is 2 or 3
  rem = floor % 6
  if (rem < 2): # less elegant alternative, rem > 1
    painter.color("blue")
  # new color whent the remainder is 4 or 5
  if (rem > 3):
      painter.color("lime")
  # start a new building at new location
  rem = floor % 21
  if (rem == 0):
    x = x + 60
    y = 0
  # end modified section
  painter.goto(x, y)
  y = y + 5
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()