#Сделано by Tor-vi 2025
import pygame as pg
import datetime as dt
import time
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
pg.init()
pg.mixer.init()
pg.font.init()
pg.display.set_caption('MultyClock')

w = 360
h = 200
bg_color= (200,255,255)
win = pg.display.set_mode((w,h))
run = True
clock = pg.time.Clock()
mode = 'таймер'

class Tab():
    def __init__(self,w,h,x,y,color,text, text_color,text_size,shift_x,shift_y):
        self.rect = pg.Rect(x,y,w,h)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.label = pg.font.SysFont('arial',text_size).render(text, True, self.text_color)
        self.shift_x = shift_x
        self.shift_y = shift_y
    def draw(self):
        pg.draw.rect(win,self.color, self.rect)
        win.blit(self.label, (self.rect.x + self.shift_x, self.rect.y + self.shift_y))
    def get_border(self):
        pg.draw.rect(win,((0,0,0)), self.rect,2)

class Button():
    def __init__(self,w,h,x,y,color,text, text_color,text_size):
        self.rect = pg.Rect(x,y,w,h)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.label = pg.font.SysFont('arial',text_size).render(text, True, self.text_color)
    def draw(self):
        pg.draw.rect(win,self.color, self.rect)
        win.blit(self.label, (self.rect.x + 20, self.rect.y))
    def get_border(self):
        pg.draw.rect(win,((0,0,0)), self.rect,2)

t = dt.datetime.now().time()
x,y = w,h
ho = 00
h2 = 0
m2 = 0
m = 00
s =00
co = 0
sound1 = pg.mixer.Sound('lol.ogg')
sound2 = pg.mixer.Sound('lol.ogg')
f = False
stop = True
tab_clock = Tab(int(w/3),int(h/5), 0 , 0,(255,0,0),'Часы',(255,255,255),20,22,0)
tab_sw = Tab(int(w/3),int(h/5), 120 , 0,(0,255,0),'Секундомер',(255,255,255),20,22,0)
tab_alarm = Tab(int(w/3),int(h/5), 240, 0,(0,0,255),'Будильник',(255,255,255),20,22,0)
clock_content = pg.font.SysFont('arial',65).render(f"{str(t.hour)}:{str(t.minute)}:{str(t.second)}", True, (255,255,255))
alarm_content = pg.font.SysFont('arial',65).render(f"{str(h2)}:{str(m2)}", True, (255,255,255))
stopwatch_content = pg.font.SysFont('arial',65).render('00:00:00', True, (255,255,255))
sw_start = Tab(int(w/5),int(h/8), int(w*0.2) , int(h*0.80),(255,255,255),'старт',(0,0,0),20,18,0)
sw_stop = Tab(int(w/5),int(h/8), int(w*0.4) , int(h*0.80),(255,255,255),'стоп',(0,0,0),20,18,0)
sw_reset = Tab(int(w/5),int(h/8), int(w*0.6) , int(h*0.80),(255,255,255),'заново',(0,0,0),20,18,0)
ah_plus =Tab(int((w/5)/2.5),int(h/8.1), int(w*0.35) , int(h*0.25),(255,255,255),'+',(0,0,0),50,3,-18)
ah_minus=Tab(int((w/5)/2.5),int(h/8), int(w*0.35) , int(h*0.78),(255,255,255),'-',(0,0,0),50,3,-18)
am_plus=Tab(int((w/5)/2.5),int(h/8.1), int(w*0.63) , int(h*0.25),(255,255,255),'+',(0,0,0),50,7,-18)
am_minus=Tab(int((w/5)/2.5),int(h/8), int(w*0.63) , int(h*0.78),(255,255,255),'-',(0,0,0),50,7,-18)
a_start = Tab(int((w/3.5)),int(h/8), int(w*0.05) , int(h*0.3),(255,255,255),'Старт',(0,0,0),23,23,-3)
a_stop = Tab(int((w/3.5)),int(h/8), int(w*0.05) , int(h*0.6),(255,255,255),'Стоп',(0,0,0),23,27,-3)
a_choose = Tab(int((w/3.2)),int(h/8), int(w*0.035) , int(h*0.8),(255,255,255),'Выбор файла (ogg)',(0,0,0),14,5,2.5)



while  run:
    
    if f == True:
        if s < 60:
            co += 1
            if co == 60:
                s+=1
                co = 0
                if s == 60:
                    m += 1
                    s = 0
                    if m == 60:
                        ho+=1
                        m = 0
    stopwatch_content = pg.font.SysFont('arial',65).render(f"{str(ho)}:{str(m)}:{str(s)}", True, (255,255,255))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.MOUSEBUTTONDOWN:
            x,y = e.pos
    
    if tab_clock.rect.collidepoint(x,y):
        mode = "таймер"
    elif tab_sw.rect.collidepoint(x,y):
        mode = "секундомер"
    elif tab_alarm.rect.collidepoint(x,y):
        mode = "будильник"
    if mode == 'таймер':
        t = dt.datetime.now().time()
        clock_content = pg.font.SysFont('arial',65).render(f"{str(t.hour)}:{str(t.minute)}:{str(t.second)}", True, (255,255,255))
        win.fill((255,0,0))
        win.blit(clock_content,(int(w/5),int(h/2.5)))
    
        
    elif mode == "секундомер":
        if sw_reset.rect.collidepoint(x,y):
            ho = 0
            m = 0
            s =0
            f = False
            stopwatch_content = pg.font.SysFont('arial',65).render(f"{str(ho)}:{str(m)}:{str(s)}", True, (255,255,255))
        elif sw_start.rect.collidepoint(x,y):
            f = True

        elif sw_stop.rect.collidepoint(x,y):
            x,y = -1,-1
            f = False
        win.fill((0,255,0))
        win.blit(stopwatch_content,(int(w/3.1),int(h/2.5)))
        sw_reset.draw()
        sw_reset.get_border()
        sw_start.draw()
        sw_start.get_border()
        sw_stop.draw()
        sw_stop.get_border()
    elif mode == "будильник":
        if ah_plus.rect.collidepoint(x,y) and stop == True:
            x,y = -1,-1
            h2 += 1

        elif ah_minus.rect.collidepoint(x,y)and stop == True:
            x,y = -1,-1
            h2 -= 1
        elif h2 < 0:
            h2 = 23
        elif h2 > 23:
            h2= 0
        elif am_plus.rect.collidepoint(x,y)and stop == True:
            x,y = -1,-1
            m2 += 1
        elif am_minus.rect.collidepoint(x,y)and stop == True:
            x,y = -1,-1
            m2 -= 1
        elif m2 < 0:
            m2 = 59
        elif m2 > 59:
            m2 = 0
        alarm_content = pg.font.SysFont('arial',65).render(f"{str(h2)}:{str(m2)}", True, (255,255,255))
        if a_start.rect.collidepoint(x,y):
            corn = dt.datetime.now().time()
            stop = False
            if h2 == corn.hour and m2 == corn.minute and stop == False:
                sound2.play()
                h2 = 0
                m2 = 0
                stop = True
        if a_stop.rect.collidepoint(x,y) and stop == False:
            stop = True
            sound2.stop()
            x,y = -1,-1

        if a_choose.rect.collidepoint(x,y)and stop == True:
            choose = filedialog.askopenfile()
            if choose != None:
                sound2 = pg.mixer.Sound(choose)
            else:
                sound2 = pg.mixer.Sound('lol.ogg')
            x,y = -1,-1
            stop == False




        
        win.fill((0,0,255))
        win.blit(alarm_content,(int(w/2.9),int(h/2.5)))
        ah_plus.draw()
        ah_plus.get_border()
        ah_minus.draw()
        ah_minus.get_border()
        am_plus.draw()
        am_plus.get_border()
        am_minus.draw()
        am_minus.get_border()
        a_start.draw()
        a_start.get_border()
        a_stop.draw()
        a_stop.get_border()
        a_choose.draw()
        a_choose.get_border()
        

    tab_clock.draw()
    tab_sw.draw()
    tab_alarm.draw()
    pg.display.update()
    clock.tick(60)