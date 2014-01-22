###The goal of this code is to simulate the motion of a ball through the air
###given initial conditions and a final height.  The final horizontal position
###will be calculated.

# STARTUP (Don't edit, typically)
from __future__ import division                 
from visual import *
from physutil import *
import math

# VISUALIZATION & GRAPH SETUP
# ===========================================
# Setup Display window for visualization
scene = display(x = 0, y = 0, width = 700, height = 700, range = 50,
                background = color.black,
                title = "Projectile Calc to find x")
# Create object for visualization
ball = sphere(color=color.red, radius = 1)
# Create a trail behind the object as it moves
trail = curve(color = color.green)
# Create sphere to mark the origin in Display window
origin = sphere(pos=vector(0,0,0), color = color.blue, radius = 0.01)
# Create arrows to represent vector quantities in the Display window
arrow1 = arrow(pos=ball.pos, axis = (0,0,0), color = color.yellow);
arrow2 = arrow(pos=ball.pos + vector(0,0.2,0), axis = (0,0,0), color = color.blue);

graph = PhysGraph(1) #Will use to graph posx v posy

###set givens for this problem
##Global givens
V = 20
theta = 30
ball.m = 0.1 # mass in kg
deltat = 0.01
t = 0

#Air Drag factors
Cd = 0.5
A = 0.01
p = 1.2

##x, y specific givens
y0 = 0
yf = -4
x0 = 0

#Convert angle to radians, calc components of vectors
#and vectorize everything that ought to be vectorized
theta = theta*math.pi/180 #converts angle to radians
vy0 = V*math.sin(theta)
vx = V*math.cos(theta)
ball.v = vector(vx, vy0, 0)
ball.pos = vector(x0, y0, 0)
g = vector(0, -9.8, 0)

#Is the ball ending up above, below or at the same height as it starts?
finalH = 1
if(yf > y0):
    finalH = 2
    
while((ball.y < y and finalH > 1) or (ball.y >= y and finalH == 1)):
    Fg = ball.m*g
    Fd = -0.5*Cd*p*A*ball.v*mag(ball.v) #You can add some factors later and then calc this
    Fnet = Fg + Fd
    ball.a = Fnet/ball.m
    ball.v = ball.v + ball.a*deltat
    ball.pos = ball.pos + ball.v*deltat

    #Evaluate whether we've hit the desired height -- may be hit twice!
    if(ball.y > y and finalH > 1):
        finalH = 1
        print(t, ball.pos.x, ball.pos.y, y)
    if(ball.y < y and finalH > 1 and ball.v.y < 0):
        print("Not going to make it!")
        break

    #EDIT THIS: Draw arrows to show quantities of interest
    arrow1.pos = ball.pos;
    arrow2.pos = ball.pos;
    arrowscale1= 5 # determines how long to draw arrows to represent
                   # vectors; here, the value of arrowscale 
                   # tells us what arrow length (in meters) 
                   # corresponds to a force with a magnitude of 1 Newton
                   #e-15 works well for forces
    arrow1.axis = Fg*arrowscale1;   #Fnet 
    arrow2.axis = Fd*arrowscale1;    #Resistant forces
    
    # advance the clock; here we're just keeping track of the total time.
    t = t + deltat

    graph.plot(ball.x, ball.y)

    rate(20)

print(t, ball.pos.x, ball.pos.y, y)

    

