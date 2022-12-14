# Task 15
# Turtle graphics
# Rhombus
import turtle
t = turtle
t.hideturtle()
t.fillcolor("grey")
t.begin_fill()
t.goto (50,-50)
t.goto (100, 0)
t.goto (50, 50)
t.goto (-50, -50)
t.goto (-100, 0)
t.goto (-50, 50)
t.goto (0, 0)
t.end_fill()
t.done()

# Triangles
import turtle
t = turtle
t.hideturtle()
t.fillcolor("grey")
t.begin_fill()
t.goto (100, 0)
t.goto (50, 50)
t.goto (0, 0)
t.end_fill()
t.goto (50, 100)
t.goto (100, 0)
t.done()

# Parallelepiped
import turtle
t = turtle
t.hideturtle()
t.fillcolor("grey")
t.begin_fill()
t.goto (100, 0)
t.goto (50, 50)
t.goto (0, 0)
t.end_fill()
t.goto (50, 100)
t.goto (100, 0)
t.done()

# Rings
import turtle
t = turtle
t.hideturtle()
t.circle(20)
t.penup ()
t.goto (50, 0)
t.pendown ()
t.circle (20)
t.penup ()
t.goto (100, 0)
t.pendown ()
t.circle (20)
t.penup ()
t.goto (25, -20)
t.pendown ()
t.circle (20)
t.penup ()
t.goto (75, -20)
t.pendown ()
t.circle (20)
t.done()

# Cardinal directions
import turtle
t = turtle
t.hideturtle()
t.goto (0, -25)
t.circle (25)
t.goto (0, -100)
t.goto (0, 100)
t.goto (0, 0)
t.goto (100, 0)
t.goto (-100, 0)
t.penup ()
t.goto (-6, -120)
t.write ("Юг")
t.goto (-140, -7)
t.write ("Запад")
t.goto (110, -7)
t.write ("Восток")
t.goto (-15, 103)
t.write ("Север")
t.done()

#Квадрат, пунктир, точки
import turtle
t = turtle
t.hideturtle()
t.pensize (2)
t.dot ()
t.goto (100, -100)
t.dot ()
t.goto (100, 100)
t.dot ()
t.goto (-100, -100)
t.dot ()
t.goto (-100, 100)
t.dot ()
t.goto (0, 0)
t.goto (-100, 100)
t.goto (-80, 100)
t.penup ()
t.goto (-60, 100)
t.pendown ()
t.goto (-10, 100)
t.penup ()
t.goto (10, 100)
t.pendown ()
t.goto (60, 100)
t.penup ()
t.goto (80, 100)
t.pendown ()
t.goto (100, 100)
t.penup ()
t.goto (-100, -100)
t.pendown ()
t.goto (-80, -100)
t.penup ()
t.goto (-60, -100)
t.pendown ()
t.goto (-10, -100)
t.penup ()
t.goto (10, -100)
t.pendown ()
t.goto (60, -100)
t.penup ()
t.goto (80, -100)
t.pendown ()
t.goto (100, -100)
t.done()