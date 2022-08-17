import turtle


object = turtle.Turtle()

object.penup()
object.goto(-50,50)
object.setheading(270)
object.pencolor('red')
object.pendown()
object.forward(100)
object.goto(-50,0)
object.setheading(0)
object.forward(50)
object.left(90)
object.forward(50)
object.backward(100)
object.penup()

object.goto(50,25)
object.pendown()
object.setheading(270)
object.forward(75)
object.penup()

object.goto(50,50)
object.pendown()
object.circle(2)

window = turtle.Screen()
window.mainloop()


