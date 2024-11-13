
#init game
import pygame
import os
import math
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

os.system('cls')

clock = pygame.time.Clock()

win_w = 1920
win_h = 1080
draw_w = (win_w-(96*11))/2
draw_h = (win_h-(96*11))/2

win = pygame.display.set_mode((win_w, win_h), pygame.FULLSCREEN)
pygame.display.set_caption("Takeover")

#0 = void
#1* = red
#2* = Blue
#*0 / 1 = platform
#*1 = sniper
#*2 = cannon
#*3 = shotgun
#*9 = flag

_000 = pygame.image.load('images/000.png')
_001 = pygame.image.load('images/001.png')
_011 = pygame.image.load('images/011.png')
_012 = pygame.image.load('images/012.png')
_013 = pygame.image.load('images/013.png')
_019 = pygame.image.load('images/019.png')
_021 = pygame.image.load('images/021.png')
_022 = pygame.image.load('images/022.png')
_023 = pygame.image.load('images/023.png')
_029 = pygame.image.load('images/029.png')
_018 = pygame.image.load('images/018.png')
_028 = pygame.image.load('images/028.png')
_017 = pygame.image.load('images/017.png')
_027 = pygame.image.load('images/027.png')
_035 = pygame.image.load('images/035.png')
_034 = pygame.image.load('images/034.png')
_033 = pygame.image.load('images/033.png')
_032 = pygame.image.load('images/032.png')
_031 = pygame.image.load('images/031.png')
_039 = pygame.image.load('images/039.png')

#init game grid system
game = [
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,19,0,0,0,0,0,0,0,0,0,29,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0]
]

turn = 0
place = False
select = 0
select_click = False
place_click = False
action = 5
winning_score = 50

font_name = pygame.font.match_font('impact')

bullets = []

class shoot(object):
	def __init__(self, x11, y11, team, distance, power):
		self.x11 = x11
		self.y11 = y11
		self.team = team
		self.distance = distance
		self.power = power
		self.travel = 0
		self.pop = False

	def move(self):
		if self.team == 0:
			self.x11 += 1
			self.travel += 1
		elif self.team == 1:
			self.x11 -= 1
			self.travel += 1

	def destroy(self):
		if self.team == 1 and game[self.y11][self.x11] >= 10 and game[self.y11][self.x11] <= 18:
			game[self.y11][self.x11] = 0
			if bullet.power == 1 and game[self.y11][self.x11 - 1] != 19:
				game[self.y11][self.x11 - 1] = 0
			self.pop = True
		if self.team == 0 and game[self.y11][self.x11] >= 20 and game[self.y11][self.x11] <= 28:
			game[self.y11][self.x11] = 0
			if bullet.power == 1 and game[self.y11][self.x11 + 1] != 29:
				game[self.y11][self.x11 + 1] = 0
			self.pop = True

	def draw(self):
		if self.team == 0:
			win.blit(_017, (self.x11 * 96 - 96 + draw_w,self.y11 * 96 - 96 + draw_h))
		if self.team == 1:
			win.blit(_027, (self.x11 * 96 - 96 + draw_w,self.y11 * 96 - 96 + draw_h))	

def draw():
	#scan through game grid system for each tile
	# pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
	bgcolor = (20,20,20)
	pygame.draw.rect(win, bgcolor, (0, 0, draw_w, win_h))
	pygame.draw.rect(win, bgcolor, ((96*11) + draw_w, 0, draw_w, win_h))
	pygame.draw.rect(win, bgcolor, (0, 0, win_w, draw_h))
	pygame.draw.rect(win, bgcolor, (0,(96*11) + draw_h, win_w, draw_h))
	scanX = 0
	scanY = 0
	for row in game:
		for tile in row:
			if scanX >= 1 and scanX <= 11 and scanY >= 1 and scanY <= 11:
				if tile == 0:
					win.blit(_000, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 10 or tile == 20:
					win.blit(_001, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 11:
					win.blit(_011, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 12:
					win.blit(_012, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 13:
					win.blit(_013, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 19:
					win.blit(_019, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 21:
					win.blit(_021, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 22:
					win.blit(_022, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 23:
					win.blit(_023, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
				if tile == 29:
					win.blit(_029, (scanX * 96 - 96 + draw_w,scanY * 96 - 96 + draw_h))
			scanX += 1
		scanY += 1
		scanX = 0

		if action == 1:
			 win.blit(_031, (50,950))
		if action == 2:
			 win.blit(_032, (50,950))
		if action == 3:
			 win.blit(_033, (50,950))
		if action == 4:
			 win.blit(_034, (50,950))
		if action == 5:
			 win.blit(_035, (50,950))

		if turn == 0:
			win.blit(_001, (50,50))
			win.blit(_011, (50,200))
			win.blit(_012, (50,300))
			win.blit(_013, (50,400))
			if select == 1:
				win.blit(_018, (50,50))
			elif select == 2:
				win.blit(_018, (50,200))
			elif select == 3:
				win.blit(_018, (50,300))
			elif select == 4:
				win.blit(_018, (50,400))

			if place == True:
				win.blit(_018, (mouseX11 * 96 - 96 + draw_w,mouseY11 * 96 - 96 + draw_h))

		if turn == 2:
			win.blit(_001, (50,50))
			win.blit(_021, (50,200))
			win.blit(_022, (50,300))
			win.blit(_023, (50,400))
			if select == 1:
				win.blit(_028, (50,50))
			elif select == 2:
				win.blit(_028, (50,200))
			elif select == 3:
				win.blit(_028, (50,300))
			elif select == 4:
				win.blit(_028, (50,400))

			if place == True:
				win.blit(_028, (mouseX11 * 96 - 96 + draw_w,mouseY11 * 96 - 96 + draw_h))
		
		redpos = 1550 
		bluepos = 1600 

		pygame.draw.rect(win, (255,255,255),(1525, 40, 125, 10))

		pygame.draw.rect(win, (255,0,0),(redpos,win_h - 50 - (redscore * ((win_h - 100) / winning_score)),25,(redscore * ((win_h - 100) / winning_score))))
		pygame.draw.rect(win, (0,0,255),(bluepos,win_h - 50 - (bluescore * ((win_h - 100) / winning_score)),25,(bluescore * ((win_h - 100) / winning_score)))) 

		win.blit(_039, (win_w - 50 - 96,win_h - 50 - 96))

		pygame.display.update()

redscore = 1
bluescore = 1

while True:
#INIT
	clock.tick(30)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			select_click = True
			place_click = True
#DETECT POSITIONS
	mouseX, mouseY = pygame.mouse.get_pos()
	if mouseX > draw_w and mouseX < draw_w + (96*11) and mouseY > draw_h and mouseY < draw_h + (96*11):
		mouseX11 = (mouseX - (draw_w))/96
		mouseY11 = (mouseY - (draw_h))/96
		mouseX11 = int(mouseX11)
		mouseY11 = int(mouseY11)
		mouseX11 += 1
		mouseY11 += 1
	else:
		place = False

	gun_actions = 2
#TURN 0
	if turn == 0:
		if mouseX > draw_w and mouseX < draw_w + (96*11) and mouseY > draw_h and mouseY < draw_h + (96*11):
			if (select >= 2 and select <= 4 and game[mouseY11][mouseX11] == 10) or (select == 1 and game[mouseY11][mouseX11] == 0 and ((game[mouseY11 - 1][mouseX11] >= 10 and game[mouseY11 - 1][mouseX11] <= 19) or (game[mouseY11 + 1][mouseX11] >= 10 and game[mouseY11 + 1][mouseX11] <= 19) or (game[mouseY11][mouseX11 - 1] >= 10 and game[mouseY11][mouseX11 - 1] <= 19) or (game[mouseY11][mouseX11 + 1] >= 10 and game[mouseY11][mouseX11 + 1] <= 19)) and not ((game[mouseY11 - 1][mouseX11] >= 20 and game[mouseY11 - 1][mouseX11] <= 29) or (game[mouseY11 + 1][mouseX11] >= 20 and game[mouseY11 + 1][mouseX11] <= 29) or (game[mouseY11][mouseX11 - 1] >= 20 and game[mouseY11][mouseX11 - 1] <= 29) or (game[mouseY11][mouseX11 + 1] >= 20 and game[mouseY11][mouseX11 + 1] <= 29))):
				place = True
			else:
				place = False

		if place_click == True and place == True:
			if select == 1 and action >= 1: 
				game[mouseY11][mouseX11] = 10
				action -= 1
			elif select == 2 and action >= gun_actions:
				game[mouseY11][mouseX11] = 11
				action -= gun_actions
			elif select == 3 and action >= gun_actions:
				game[mouseY11][mouseX11] = 12
				action -= gun_actions
			elif select == 4 and action >= gun_actions:
				game[mouseY11][mouseX11] = 13
				action -= gun_actions
		if action == 0:
			turn += 1
			action = 5
			select = 0
#TURN 2
	if turn == 2:
		if mouseX > draw_w and mouseX < draw_w + (96*11) and mouseY > draw_h and mouseY < draw_h + (96*11):
			if (select >= 2 and select <= 4 and game[mouseY11][mouseX11] == 20) or (select == 1 and game[mouseY11][mouseX11] == 0 and ((game[mouseY11 - 1][mouseX11] >= 20 and game[mouseY11 - 1][mouseX11] <= 29) or (game[mouseY11 + 1][mouseX11] >= 20 and game[mouseY11 + 1][mouseX11] <= 29) or (game[mouseY11][mouseX11 - 1] >= 20 and game[mouseY11][mouseX11 - 1] <= 29) or (game[mouseY11][mouseX11 + 1] >= 20 and game[mouseY11][mouseX11 + 1] <= 29)) and not ((game[mouseY11 - 1][mouseX11] >= 10 and game[mouseY11 - 1][mouseX11] <= 19) or (game[mouseY11 + 1][mouseX11] >= 10 and game[mouseY11 + 1][mouseX11] <= 19) or (game[mouseY11][mouseX11 - 1] >= 10 and game[mouseY11][mouseX11 - 1] <= 19) or (game[mouseY11][mouseX11 + 1] >= 10 and game[mouseY11][mouseX11 + 1] <= 19))):
				place = True
			else:
				place = False

		if place_click == True and place == True:
			if select == 1 and action >= 1: 
				game[mouseY11][mouseX11] = 20
				action -= 1
			elif select == 2 and action >= gun_actions:
				game[mouseY11][mouseX11] = 21
				action -= gun_actions
			elif select == 3 and action >= gun_actions:
				game[mouseY11][mouseX11] = 22
				action -= gun_actions
			elif select == 4 and action >= gun_actions:
				game[mouseY11][mouseX11] = 23
				action -= gun_actions
		if action == 0:
			turn += 1
			action = 5
			select = 0
#TURN 1
	if turn == 1:
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if tile == 21:
					bullets.append(shoot(scanX,scanY,1,15,0))
				if tile == 22:
					bullets.append(shoot(scanX,scanY,1,5,1))
				if tile == 23:
					bullets.append(shoot(scanX,scanY,1,5,0))
					bullets.append(shoot(scanX,scanY + 1,1,5,0))
					bullets.append(shoot(scanX,scanY - 1,1,5,0))
				scanX += 1
			scanY += 1
			scanX = 0
			
		while len(bullets) > 0:
			for bullet in bullets:
				if bullet.x11 == 0 or bullet.x11 == 12 or bullet.pop or bullet.travel == bullet.distance:
					bullets.pop(bullets.index(bullet))
				else:
					bullet.move()
					bullet.destroy()
			for bullet in bullets:
				bullet.draw()
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if tile != 0 and tile != 19 and tile != 29:
					game[scanY][scanX] *= -1
				scanX += 1
			scanY += 1
			scanX = 0
		for i in range(25):
			scanX = 0
			scanY = 0
			for row in game:
				for tile in row:
					if game[scanY][scanX] >= 10 and game[scanY][scanX] <= 29:
						if game[scanY][scanX + 1] < 0:
							game[scanY][scanX + 1] *= -1
						if game[scanY][scanX - 1] < 0:
							game[scanY][scanX - 1] *= -1
						if game[scanY + 1][scanX] < 0:
							game[scanY + 1][scanX] *= -1
						if game[scanY - 1][scanX] < 0:
							game[scanY -1][scanX] *= -1
					scanX += 1
				scanY += 1
				scanX = 0
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if tile < 0:
					game[scanY][scanX] = 0
				scanX += 1
			scanY += 1
			scanX = 0
		turn += 1
#TURN 3
	if turn == 3:
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if tile == 11:
					bullets.append(shoot(scanX,scanY,0,15,0))
				if tile == 12:
					bullets.append(shoot(scanX,scanY,0,5,1))
				if tile == 13:
					bullets.append(shoot(scanX,scanY,0,5,0))
					bullets.append(shoot(scanX,scanY + 1,0,5,0))
					bullets.append(shoot(scanX,scanY - 1,0,5,0))
				scanX += 1
			scanY += 1
			scanX = 0
			
		while len(bullets) > 0:
			for bullet in bullets:
				if bullet.x11 == 0 or bullet.x11 == 12 or bullet.pop or bullet.travel == bullet.distance:
					bullets.pop(bullets.index(bullet))
				else:
					bullet.move()
					bullet.destroy()
			for bullet in bullets:
				bullet.draw()
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if tile != 0 and tile != 19 and tile != 29:
					game[scanY][scanX] *= -1
				scanX += 1
			scanY += 1
			scanX = 0
		for i in range(25):
			scanX = 0
			scanY = 0
			for row in game:
				for tile in row:
					if game[scanY][scanX] >= 10 and game[scanY][scanX] <= 29:
						if game[scanY][scanX + 1] < 0:
							game[scanY][scanX + 1] *= -1
						if game[scanY][scanX - 1] < 0:
							game[scanY][scanX - 1] *= -1
						if game[scanY + 1][scanX] < 0:
							game[scanY + 1][scanX] *= -1
						if game[scanY - 1][scanX] < 0:
							game[scanY - 1][scanX] *= -1
					scanX += 1
				scanY += 1
				scanX = 0
		scanX = 0
		scanY = 0
		for row in game:
			for tile in row:
				if tile < 0:
					game[scanY][scanX] = 0
				scanX += 1
			scanY += 1
			scanX = 0
		turn += 1
	place_click = False
#SCORE
	if turn == 4:
		redscore = 0
		bluescore = 0
		for row in game:
			for tile in row:
				if tile >= 10 and tile <= 19:
					redscore += 1	
				if tile >= 20 and tile <= 29:			
					bluescore += 1
		if not (redscore >= winning_score or bluescore >= winning_score):
			turn = 0
#SELECTIONS
	if mouseX > 50 and mouseX < 50 + 96 and mouseY > 50 and mouseY < 50 + 96 and select_click:
		select = 1
	if mouseX > 50 and mouseX < 50 + 96 and mouseY > 200 and mouseY < 200 + 96 and select_click:
		select = 2
	if mouseX > 50 and mouseX < 50 + 96 and mouseY > 300 and mouseY < 300 + 96 and select_click:
		select = 3
	if mouseX > 50 and mouseX < 50 + 96 and mouseY > 400 and mouseY < 400 + 96 and select_click:
		select = 4
	if mouseX > (win_w - 50 - 96) and mouseX < (win_w - 50) and mouseY > (win_h - 50 - 96) and mouseY < (win_h - 50) and select_click:
		pygame.quit()
	select_click = False
#DRAW GAME
	draw()