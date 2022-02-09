import turtle

screen = turtle.getscreen()
pen = turtle.Turtle()

# I
def draw_i():
	pen.forward(50)
	pen.backward(25)
	pen.right(90)
	pen.forward(140)
	pen.left(90)
	pen.forward(25)
	pen.backward(50)

def love(fill='pink'):
	# draw love
	pen.fillcolor(fill)
	pen.begin_fill()

	pen.left(50)
	pen.forward(100)
	pen.circle(40, 180)
	pen.left(260)
	pen.circle(40, 180)
	pen.forward(100)
	pen.end_fill()

def draw_u():
	pen.up()
	pen.left(90)
	pen.forward(170)
	pen.right(130)
	pen.backward(25)
	pen.down()        # start drawing
	pen.forward(100)
	pen.circle(40, 180)
	pen.forward(100)


pen.pensize(10)
pen.speed(2)

pen.up()
pen.left(180)
pen.forward(130)
pen.down()


draw_i()

pen.up()
pen.home()
pen.down()

love('red')

draw_u()

pen.up()
pen.home()

pen.fillcolor('black')
pen.right(90)
pen.forward(170)
pen.left(90)
pen.down()

pen.up()
pen.left(180)
pen.forward(130)
pen.down()


pen.up()
pen.left(170)
pen.forward(80)
pen.write("Crush!", font=('Arial', 18, 'bold'))

pen.screen.exitonclick()