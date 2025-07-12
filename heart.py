from turtle import *
t = Turtle()
t.begin_fill()
t.fillcolor('red')
tracer(0)
'''
for i in range(2,100):
    for J in range(1,6):
        t.forward(i)
        t.right(61)
        update()
'''
t.penup()
t.shape(None)
print(t.pos())
t.pendown()
t.right(120)
t.forward(100)
t.right(115)
t.forward(100)
print(t.heading())
for i in range(20):
    t.right(i)
    t.forward(10)

t.forward(20)
t.pencolor('red')
t.setpos(0,0)
t.pendown()
t.setheading(60)
for i in range(20):
    t.left(i)
    t.forward(10)
t.forward(20)
#print(*dir(t),sep='\n')
t.pencolor('black')
style = ('Arial', 24, 'bold')


t.end_fill()
t.penup()

t.goto(-50,30)
m=t.write("Prabhu", font=style, align='center')

t.goto(-50,0)
m=t.write("Manju", font=style, align='center')
t.goto(-50,-90)
update()
exitonclick()
