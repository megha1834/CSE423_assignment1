from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import numpy as np

width , height = 800, 600                     
# Window size
backgroundcolor = [0.2,0.2,0.1]
drops= 120
bend =0

raindrops=[(random.randint(0,width),random.randint(0,height), random.choice([(0.1, 0.1, 1.0), (0.5, 0.5, 0.1)]))for _ in range(drops)]
def drawground():
    glBegin(GL_QUADS)
    glColor3f(0.5,0.3,0)
    glVertex2f(0,0)
    glVertex2f(800,0)
    glVertex2f(800,375)
    glVertex2f(0,375)
    glEnd()
def drawhouse():
    glBegin(GL_TRIANGLES)
    glColor3f(0.35,0,1.0)
    glVertex2f(225,350)          #ROOF
    glVertex2f(575,350)
    glVertex2f(400,450)

    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1,1,1.0)
    glVertex2f(245,220)          #BODY
    glVertex2f(555,220)
    glVertex2f(555,350)
    glVertex2f(245,350)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex2f(375, 220)          #DOOR
    glVertex2f(425, 220)
    glVertex2f(425, 280)
    glVertex2f(375, 280)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0,0,1)   
    glVertex2f(290, 250)  
         #WINDOWLEFT
    glVertex2f(350, 250)
    #glColor3f(1,1,1)
    glVertex2f(350, 315)

    glVertex2f(290, 315)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0,0,1)   
    glVertex2f(450, 250)          #WINDOWRIGHT
    glVertex2f(510, 250)
    glVertex2f(510, 315)
    glVertex2f(450, 315)
    glEnd()
    
    glColor3f(0.2,0.2,0.1)   
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(350,250)
    glVertex2f(290, 315)
    glEnd()
    glColor3f(0.2,0.2,0.1)    
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(290,250)
    glVertex2f(350, 315)
    glEnd()
    glColor3f(0.2,0.2,0.1)   
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(450,250)
    glVertex2f(510, 315)
    glEnd()
    glColor3f(0.2,0.2,0)   
    glLineWidth(2.5)
    glBegin(GL_LINES)
    glVertex2f(510,250)
    glVertex2f(450, 315)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1,1,1)   
    glVertex2f(410, 240)          #WINDOWRIGHT
    glVertex2f(415, 240)
    glVertex2f(415, 250)
    glVertex2f(410, 250)
    glEnd()
    
def tree():
    for i in range(10):
        g = i *100
        glBegin(GL_TRIANGLES)
        glColor3f(0,1,0)   
        glVertex2f(g, 250)    
        
        glColor3f(1,1,0)         #WINDOWRIGHT
        glVertex2f(g+50, 350)
        glColor3f(0,1,0) 
        glVertex2f(g+100, 250)
        glEnd()

def rain():
    glLineWidth(1.5)
    glBegin(GL_LINES)
    for x,y,colors in raindrops:
        glColor3f(colors[0], colors[1], colors[2])
        glVertex2f(x,y)
        glVertex2f(x+bend,y-25)
    glEnd()
def raining():
    global raindrops 
    for i in range(drops):
        x,y,colors=raindrops[i]
        y-=random.randint(8,12)
        if y<0:
            y= height+random.randint(0,100)
            x= random.randint(0,width)
        raindrops[i]=(x,y,colors)
    glutPostRedisplay()
def special_keys(key, x, y):
    global bend
    if key == GLUT_KEY_RIGHT and bend<=13:
        bend += 1 
    elif key == GLUT_KEY_LEFT and bend>=-13:
        bend -= 1  

    glutPostRedisplay()



def key_pressed(key,x, y):
    global backgroundcolor

    
    if key == b'n':  
        backgroundcolor = [max(c - 0.05, 0) for c in backgroundcolor]
    elif key == b'm':  
        backgroundcolor = [min(c + 0.05, 1) for c in backgroundcolor]

    glClearColor(*backgroundcolor, 1)
    glutPostRedisplay()




def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    drawground()
    tree()
    
    
    drawhouse()
    rain()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(00, 00, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)



def init_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width,height)
    glutCreateWindow(b"OpenGL Rain Animation")
    glutReshapeFunc(reshape)

    glClearColor(*backgroundcolor, 1)
    gluOrtho2D(0, width, 0,height)

    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
    glutSpecialFunc(special_keys)  # key presses
    glutReshapeFunc(reshape)
    glutIdleFunc(raining)
    glutMainLoop()


glutInit()
init_window()