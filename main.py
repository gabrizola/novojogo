import pygame
import pgzrun
import random 
WIDTH = 800
HEIGHT = 600
TITLE = "primeiro jogo em Py"
estado_jogo= "JOGANDO"
pontos = 0

from funcoes import redimensionar

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

pontos = 0

def reiniciar_jogo():
    global pontos, vidas, estado_jogo
    pontos = 0
    vidas = 4
    bananinha.pos = (100, 100)
    coraçao.posn= (400,300)
    bolso.pos = (650, 450)
    estado_jogo = "JOGANDO"

def mover_bolso():
    if bolso.x < bananinha.x:
        bolso.x += vel_bolso
    elif bolso.x > bananinha.x:
        bolso.x -= vel_bolso

    if bolso.y < bananinha.y:
        bolso.y += vel_bolso
    elif bolso.y < bananinha.y:
        bolso.y -= vel_bolso

def spaw_coraçao():
    if estado_jogo != "JOGANDO" or len(coraçao) >= 5:
        return
    m = Actor("moeda", (random.randint(60, WIDTH - 60),random.randint(60, HEIGHT - 200)))
    redimensionar(m, 40)
    coraçao.append(m)

    clock.schedule_interval(spaw_coraçao, 3)


def draw():
    global pontos
    screen.fill((25, 30, 45))

    if estado_jogo == "JOGANDO":
        bananinha.draw()
        coraçao.draw()
        bolso.draw()
        
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