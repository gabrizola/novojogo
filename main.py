import pygame
import pgzrun
import random 

from funcoes import redimensionar, mover_bolso, reiniciar_jogo, spaw_coraçao

WIDTH = 800
HEIGHT = 600
TITLE = "primeiro jogo em Py"

estado_jogo= "JOGANDO"
pontos = 0


bananinha = Actor("banana cat pixels",(100,100))
redimensionar(bananinha,100)

coraçao = Actor ("_", (400, 300))
redimensionar(coraçao,50)

bolso = Actor("bolsonara butterfly (1)",(700, 500))
redimensionar(bolso,100)

    
def draw():
    screen.fill((0, 255, 255))
    bananinha.draw()
    coraçao.draw()
    bolso.draw()
    screen.draw.text(f"pontos: {pontos}", (20, 20),
    fontsize=36, color="green")
        
def update():
    global pontos
    if keyboard.left:
        bananinha.x = bananinha.x - 1
    if keyboard.right:
        bananinha.x = bananinha.x + 1 
    if keyboard.up:
        bananinha.y = bananinha.y - 1
    if keyboard.down:
        bananinha.y = bananinha.y + 1        

    if bananinha.colliderect(coraçao):
        coraçao.x = random.randint(50, WIDTH - 50)
        coraçao.y = random.randint(50, HEIGHT - 50)
        pontos = pontos + 3

    mover_bolso()
    

pgzrun.go()