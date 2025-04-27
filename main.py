import pygame as pg
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
    def __init__(self,w,h,x,y,color,text, text_color):
        self.rect = pg.Rect(x,y,w,h)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.label = pg.font.SysFont('arial',20).render(text, True, self.text_color)
    def draw(self):
        pg.draw.rect(win,self.color, self.rect)
        win.blit(self.label, (self.rect.x + 5, self.rect.y))

x,y = w,h
tab_clock = Tab(int(w/3),int(h/5), 0 , 0,(255,0,0),'Таймер',(255,255,255))
tab_sw = Tab(int(w/3),int(h/5), 120 , 0,(0,255,0),'Секундомер',(255,255,255))
tab_alarm = Tab(int(w/3),int(h/5), 240, 0,(0,0,255),'Будильник',(255,255,255))
clock_content = pg.font.SysFont('arial',65).render('00:00:00', True, (255,255,255))


while  run:
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
        win.fill((255,0,0))
        win.blit(clock_content,(int(w/5),int(h/2.5)))
    elif mode == "секундомер":
        win.fill((0,255,0))
    elif mode == "будильник":
        win.fill((0,0,255))
    tab_clock.draw()
    tab_sw.draw()
    tab_alarm.draw()
    pg.display.update()
    clock.tick(60)