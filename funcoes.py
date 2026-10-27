import pygame
import pgzrun
import random 

vel_bolso = 2

def redimensionar(ator,altura):
    escala = altura / ator.height
    novo = pygame.transform.smoothscale(
        ator._orig_surf, (int(ator.width*escala), altura))
    ator._orig_surf = ator._surf = novo
    ator._update_pos()


def draw():
    screen.fill((0, 255, 255))
    bananinha.draw()
    coraçao.draw()
    bolso.draw()
    screen.draw.text(f"pontos: {pontos}", (20, 20),
    fontsize=36, color="green")


def reiniciar_jogo():
    global pontos, vidas, estado_jogo
    pontos = 0
    vidas = 4
    bananinha.pos = (100, 100)
    coraçao.posn= (400,300)
    bolso.pos = (650, 450)
    estado_jogo = "JOGANDO"

def mover_bolso(bolso,bananinha):
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



    