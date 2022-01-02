import turtle

def deslocaSE(raio):
   turtle.pu()
   turtle.rt(45)
   turtle.fd(raio//4)
   turtle.rt(45)
   turtle.pd()

def deslocaENE(raio):
   turtle.pu()
   turtle.lt(135)
   turtle.fd(raio//4)
   turtle.rt(45)
   turtle.forward(2 *raio)
   turtle.pd()

def aneis(raio):
   turtle.pensize(12)

   turtle.pencolor("blue")
   turtle.circle(raio)

   deslocaSE(raio)
   turtle.pencolor("yellow")
   turtle.circle(raio)

   deslocaENE(raio)
   turtle.pencolor("black")
   turtle.circle(raio)

   deslocaSE(raio)
   turtle.pencolor("green")
   turtle.circle(raio)

   deslocaENE(raio)
   turtle.pencolor("red")
   turtle.circle(raio)

