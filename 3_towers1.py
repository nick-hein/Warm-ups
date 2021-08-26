##############################################################################
#   a113_TR_multiple_towers.py
#   Excample solution: 
#     Create a new tower aftr 21 floors are rendered
##############################################################################
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of turtle
x = -150
y = 0

# height of tower and a counter for each "floor"
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.color("gray")
  # modifed code 
  # new color when the remainder is 3, 4, or 5
  rem = floor % 6
  if (rem > 2):
    painter.color("blue")
  # start a new building at new x,y location
  rem = floor % 21
  if (rem == 0):
    x = x + 60 # this value can vary slighhtly
    y = 0  
  # end modified section
  painter.goto(x, y)
  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()