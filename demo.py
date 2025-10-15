from tkinter import *
from tkinter import ttk
window = Tk() #instantiate an instance of a window for us
window.geometry("1300x700")
window.title("Saray's Resistance Calculator DEMO")
cat = PhotoImage(file='Screenshot 2025-10-11 214609.png')
window.iconphoto(True,cat)
window.config(background="#ffd87d")

#label = an area widget that holds text and/or an image within a window
powder = Label(window,text="   Resistance Calculator   ",font=('Times New Roman',30,'bold', 'italic'),
               bg='#f0c560',
               relief=RAISED,
               bd=10)
powder.pack()
#powder.place(x=20, y=0)
#for the label to appear, give the name for the label, "powder", make it a label in the function capital L "Label", put it in the window and give your text.




intro = Label(window,text="This is a four-band resistance calculator. To create your resistor, choose the colors that will correspond to its final resistance!",
              font=('Times New Roman',14,'bold'), bg='#ffd87d',)
intro.place(x=115, y=100)


first = Label(window,text=" First Band ",font=('Times New Roman',15,'bold'),
               bg='#f0c560',
               relief=RAISED,
               bd=10)
first.place(x=40, y=150)

brwn = 0
def click():
    brwn=1
    brown_label.config(text=brwn*10)

brown = Button(window,text='     Brown     ',font=('Times New Roman',13,'bold'),bg='brown')
brown.config(command=click)#performs call back of function
brown_label = Label(window,text=brwn)
brown_label.config(font=('Times New Roman',15,'bold'))
brown_label.place(x=915, y=230)
brown.place(x=58, y=200)


def click():
    brwn=2
    brown_label.config(text=brwn*10)
red = Button(window,text='     Red     ',font=('Times New Roman',13,'bold'),bg='red')
red.config(command=click)#performs call back of function
red.place(x=58, y=240)

def click():
    brwn=3
    brown_label.config(text=brwn*10)
orange = Button(window,text='     Orange     ',font=('Times New Roman',13,'bold'),bg='orange')
orange.config(command=click)#performs call back of function
orange.place(x=58, y=280)

def click():
    brwn=4
    brown_label.config(text=brwn*10)
yellow = Button(window,text='     Yellow     ',font=('Times New Roman',13,'bold'),bg='yellow')
yellow.config(command=click)#performs call back of function
yellow.place(x=58, y=320)

def click():
    brwn=5
    brown_label.config(text=brwn*10)
green = Button(window,text='     Green     ',font=('Times New Roman',13,'bold'),bg='green')
green.config(command=click)#performs call back of function
green.place(x=58, y=360)

def click():
    brwn=6
    brown_label.config(text=brwn*10)
blue = Button(window,text='     Blue     ',font=('Times New Roman',13,'bold'),bg='blue')
blue.config(command=click)#performs call back of function
blue.place(x=58, y=400)

def click():
    brwn=7
    brown_label.config(text=brwn*10)
violet = Button(window,text='     Violet     ',font=('Times New Roman',13,'bold'),bg='purple')
violet.config(command=click)#performs call back of function
violet.place(x=58, y=440)

def click():
    brwn=8
    brown_label.config(text=brwn*10)
grey = Button(window,text='     Grey     ',font=('Times New Roman',13,'bold'),bg='grey')
grey.config(command=click)#performs call back of function
grey.place(x=58, y=480)

def click():
    brwn=9
    brown_label.config(text=brwn*10)
white = Button(window,text='     White     ',font=('Times New Roman',13,'bold'),bg='white')
white.config(command=click)#performs call back of function
white.place(x=58, y=520)




plus = Label(window,text="+",font=('Arial',18,'bold'),
               bg='#ffd87d')
plus.place(x=950,y=225)

par = Label(window,text="(",font=('Arial',18,'bold'),
               bg='#ffd87d')
par.place(x=900,y=225)

ren = Label(window,text=")",font=('Arial',18,'bold'),
               bg='#ffd87d')
ren.place(x=990,y=225)

mul = Label(window,text="x",font=('Arial',18,'bold'),
               bg='#ffd87d')
mul.place(x=1005,y=225)


second = Label(window,text=" Second Band ",font=('Times New Roman',15,'bold'),
               bg='#f0c560',
               relief=RAISED,
               bd=10)
second.place(x=210, y=150)

blk = 0
def click():
    blk = brwn + 0
    black_label.config(text=blk)
black = Button(window,text='     Black     ',font=('Times New Roman',13,'bold'),bg='black')
black.config(command=click)#performs call back of function
black_label = Label(window,text=blk)
black_label.config(font=('Times New Roman',15,'bold'))
black_label.place(x=975, y=230)
black.place(x=220, y=200)

def click():
    blk= brwn + 1
    black_label.config(text=blk)
Brown = Button(window,text='     Brown     ',font=('Times New Roman',13,'bold'),bg='brown')
Brown.config(command=click)#performs call back of function
Brown.place(x=220, y=240)

def click():
    blk= brwn + 2
    black_label.config(text=blk)
Red = Button(window,text='     Red     ',font=('Times New Roman',13,'bold'),bg='red')
Red.config(command=click)#performs call back of function
Red.place(x=220, y=280)

def click():
    blk= brwn + 3
    black_label.config(text=blk)
Orange = Button(window,text='     Orange     ',font=('Times New Roman',13,'bold'),bg='orange')
Orange.config(command=click)#performs call back of function
Orange.place(x=220, y=320)

def click():
    blk= brwn + 4
    black_label.config(text=blk)
Yellow = Button(window,text='     Yellow     ',font=('Times New Roman',13,'bold'),bg='yellow')
Yellow.config(command=click)#performs call back of function
Yellow.place(x=220, y=360)

def click():
    blk= brwn + 5
    black_label.config(text=blk)
Green = Button(window,text='     Green     ',font=('Times New Roman',13,'bold'),bg='green')
Green.config(command=click)#performs call back of function
Green.place(x=220, y=400)

def click():
    blk= brwn + 6
    black_label.config(text=blk)
Blue = Button(window,text='     Blue     ',font=('Times New Roman',13,'bold'),bg='blue')
Blue.config(command=click)#performs call back of function
Blue.place(x=220, y=440)

def click():
    blk= brwn + 7
    black_label.config(text=blk)
Violet = Button(window,text='     Violet     ',font=('Times New Roman',13,'bold'),bg='purple')
Violet.config(command=click)#performs call back of function
Violet.place(x=220, y=480)

def click():
    blk= brwn + 8
    black_label.config(text=blk)
Grey = Button(window,text='     Grey     ',font=('Times New Roman',13,'bold'),bg='grey')
Grey.config(command=click)#performs call back of function
Grey.place(x=220, y=520)

def click():
    blk= brwn + 9
    black_label.config(text=blk)
White = Button(window,text='     White     ',font=('Times New Roman',13,'bold'),bg='white')
White.config(command=click)#performs call back of function
White.place(x=220, y=560)





third = Label(window,text=" Third Band ",font=('Times New Roman',15,'bold'),
               bg='#f0c560',
               relief=RAISED,
               bd=10)
third.place(x=410, y=150)

multiplier = 10

def click():
    multiplier=10
    dark_label.config(text=multiplier**0)
dark = Button(window,text='     Black     ',font=('Times New Roman',13,'bold'),bg='black')
dark.config(command=click)#performs call back of function
dark_label = Label(window,text=brwn)
dark_label.config(font=('Times New Roman',15,'bold'))
dark_label.place(x=1030, y=230)
dark.place(x=420, y=200)

def click():
    multiplier=10
    dark_label.config(text=multiplier**1)
chocolate = Button(window,text='     Brown     ',font=('Times New Roman',13,'bold'),bg='Brown')
chocolate.config(command=click)#performs call back of function
chocolate.place(x=420, y=240)

def click():
    multiplier=10
    dark_label.config(text=multiplier**2)
strawberry = Button(window,text='     Red     ',font=('Times New Roman',13,'bold'),bg='Red')
strawberry.config(command=click)#performs call back of function
strawberry.place(x=420, y=280)

def click():
    multiplier=10
    dark_label.config(text=multiplier**3)
frosty = Button(window,text='     Orange     ',font=('Times New Roman',13,'bold'),bg='Orange')
frosty.config(command=click)#performs call back of function
frosty.place(x=420, y=320)

def click():
    multiplier=10
    dark_label.config(text=multiplier**4)
sun = Button(window,text='     Yellow     ',font=('Times New Roman',13,'bold'),bg='Yellow')
sun.config(command=click)#performs call back of function
sun.place(x=420, y=360)

def click():
    multiplier=10
    dark_label.config(text=multiplier**5)
grass = Button(window,text='     Green     ',font=('Times New Roman',13,'bold'),bg='Green')
grass.config(command=click)#performs call back of function
grass.place(x=420, y=400)

def click():
    multiplier=10
    dark_label.config(text=multiplier**6)
ocean = Button(window,text='     Blue     ',font=('Times New Roman',13,'bold'),bg='Blue')
ocean.config(command=click)#performs call back of function
ocean.place(x=420, y=440)

def click():
    multiplier=10
    dark_label.config(text=multiplier**7)
sky = Button(window,text='     Violet     ',font=('Times New Roman',13,'bold'),bg='Purple')
sky.config(command=click)#performs call back of function
sky.place(x=420, y=480)

def click():
    multiplier=10
    dark_label.config(text=multiplier**8)
bland = Button(window,text='     Grey     ',font=('Times New Roman',13,'bold'),bg='Grey')
bland.config(command=click)#performs call back of function
bland.place(x=420, y=520)

def click():
    multiplier=10
    dark_label.config(text=multiplier**9)
ice = Button(window,text='     White     ',font=('Times New Roman',13,'bold'),bg='White')
ice.config(command=click)#performs call back of function
ice.place(x=420, y=560)

def click():
    multiplier=10
    dark_label.config(text=multiplier**(-1))
gold = Button(window,text='     Gold     ',font=('Times New Roman',13,'bold'),bg='Gold')
gold.config(command=click)#performs call back of function
gold.place(x=420, y=600)

def click():
    multiplier=10
    dark_label.config(text=multiplier**(-2))
silver = Button(window,text='     Silver     ',font=('Times New Roman',13,'bold'),bg='silver')
silver.config(command=click)#performs call back of function
silver.place(x=420, y=640)


fourth = Label(window,text=" Fourth Band ",font=('Times New Roman',15,'bold'),
               bg='#f0c560',
               relief=RAISED,
               bd=10)
fourth.place(x=595, y=150)

tol = Label(window,text="Tolerance:",font=('Times New Roman',14,'bold'),
               bg='#ffd87d')
tol.place(x=900,y=270)

perc = Label(window,text="±",font=('Times New Roman',14,'bold'),
               bg='#ffd87d')
perc.place(x=1000,y=270)


tolerance = 0

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 1.00)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
mocha = Button(window,text='     Brown     ',font=('Times New Roman',13,'bold'),bg='brown')
mocha.config(command=click)#performs call back of function
mocha_label = Label(window,text=brwn)
mocha_label.config(font=('Times New Roman',15,'bold'))
mocha_label.place(x=1015, y=270)
mocha.place(x=610, y=200)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 2.00)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
tomato = Button(window,text='     Red     ',font=('Times New Roman',13,'bold'),bg='red')
tomato.config(command=click)#performs call back of function
tomato.place(x=610, y=240)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 0.05)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
citrus = Button(window,text='     Orange     ',font=('Times New Roman',13,'bold'),bg='orange')
citrus.config(command=click)#performs call back of function
citrus.place(x=610, y=280)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 0.02)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
burn = Button(window,text='     Yellow     ',font=('Times New Roman',13,'bold'),bg='yellow')
burn.config(command=click)#performs call back of function
burn.place(x=610, y=320)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 0.5)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
lime = Button(window,text='     Green     ',font=('Times New Roman',13,'bold'),bg='green')
lime.config(command=click)#performs call back of function
lime.place(x=610, y=360)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 0.25)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
neptune = Button(window,text='     Blue     ',font=('Times New Roman',13,'bold'),bg='blue')
neptune.config(command=click)#performs call back of function
neptune.place(x=610, y=400)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 0.1)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
skyline = Button(window,text='     Violet     ',font=('Times New Roman',13,'bold'),bg='purple')
skyline.config(command=click)#performs call back of function
skyline.place(x=610, y=440)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 0.01)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
gray = Button(window,text='     Grey     ',font=('Times New Roman',13,'bold'),bg='grey')
gray.config(command=click)#performs call back of function
gray.place(x=610, y=480)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 5.00)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
karat = Button(window,text='     Gold     ',font=('Times New Roman',13,'bold'),bg='gold')
karat.config(command=click)#performs call back of function
karat.place(x=610, y=520)

def click():
    tolerance=0
    mocha_label.config(text=tolerance + 10.0)
    percent = Label(window, text="%")
    percent.place(x=1065,y=272)
fox = Button(window,text='     Silver     ',font=('Times New Roman',13,'bold'),bg='silver')
fox.config(command=click)#performs call back of function
fox.place(x=610, y=560)


final = Label(window,text=" Final Calculations ",font=('Times New Roman',15,'bold'),
               bg='#f0c560',
               relief=RAISED,
               bd=10)
final.place(x=880, y=150)


#KEEP EVERYTHING YOU WRITE INSIDE OF THE MAINLOOP
window.mainloop() #place window on computer screen, listen for events
