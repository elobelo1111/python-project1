import turtle 
screen=turtle.Screen()
t=turtle.Turtle()

def draw_shape(n,size):
    for _ in range(n):
        t.forward(size)
        t.left(360/n)




t.speed(9)


for row in range(4):
    
    
    for col in range(4):
        
       
        x = -100 + (col * 70)
        y = 100 - (row * 70)
        
       
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()
        
       
        if (row + col) % 2 == 0:
            size = 20
            color = "yellow"
        else:
            size = 35
            color = "purple"
            
      
        t.fillcolor(color)
        t.pencolor("black")
        t.pensize(1.5)
        t.begin_fill()
        
        for _ in range(5):
            t.forward(size)
            t.right(144)
            
        t.end_fill()
















































turtle.done()