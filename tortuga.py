import turtle
t = turtle.Pen()
t.reset()
t.speed(0)
for x in range (1,72):
    t.forward (120)
    t.left(180)




""" 
lados=int(4)
t.speed(0)
for m in range (5,75):
    t.left(360/lados + 5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if(m%2==0):
        for n in range(lados):
            t.circle(m/3)
            t.right(360/lados)
    else:
        for n in range(lados):
            t.forward(m)
            t.right(360/lados) """



""" import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colores=["blue","white","green","yellow"]
nombre =("*")
t.speed(0)
for x in range(100):
    t.pencolor(colores[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(nombre, font=("Arial", int((x+4)/4), "bold"))
    t.left(95)
 """

""" colores = ['yellow','green', 'blue', 'red']
##begin_fill()
#  while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
s= 0
speed(200)
for x in range (150):
    pencolor (1,1,0)
    forward(x)
    left (91)  
    
# right (x*0.5)
#end_fill()
done() """