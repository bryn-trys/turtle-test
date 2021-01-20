import turtle

screen = turtle.Screen()
turtle.setup(700,700)
turtle.bgcolor("yellow")

mable = turtle.Turtle()

mable.pencolor("blue")
mable.pensize(2)
mable.shapesize(3,3,3)


def square(size):

	step = 0
	while step < 4:
		mable.forward(size)
		mable.right(90)
		step += 1



def star(size):
  step = 0
  while step < 5:
    mable.forward(size)
    mable.right(144)
    step += 1



def triangle(size):
  step = 0
  while step < 3:
    mable.forward(size)
    mable.right(120)
    step +=1




def circle(size):
  mable.circle(size)

print("Options: Triangle, Star, Square, and Circle ")
shape = input("What shape do you want to draw? : ")
size = int(input("Please specify what size you want for your shape. "))

if shape.lower() == "star":
  star(size)

elif shape.lower() == "circle":
  circle(size)

elif shape.lower() == "square":
  square(size)

else:
  triangle(size)
