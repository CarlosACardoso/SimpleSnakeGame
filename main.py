import pygame, random
from pygame.locals import *

def on_grid_random(): #Função para randomizar a maça dentro do Grid de 10x10
    x = random.randint(10,590)
    y = random.randint(10,590)
    return (x//10 * 10, y//10 * 10) #Divisão inteira por 10 e multiplicação por 10 (enquanda números como 275 ou 298. os transformando em 270 e 290 respectivamente)

def collision(c1,c2): #Teste de colisões entre duas células
    return (c1[0] == c2[0] and c1[1] == c2[1])

#Direcionamento da snake
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init() #Inicialização do sistemade py.game
screen = pygame.display.set_mode((600,600)) #Produção da janela do jogo
pygame.display.set_caption('Snake') #Título da janela

#Snake
snake = [(200,200), (210,200), (220,200)] #Definição da posição inicial da Snake
snake_skin = pygame.Surface((10,10)) #Define o tamanho da Snake
snake_skin.fill((255,255,255)) #Pinta a Snake
my_direction = LEFT #Direção inicial da Snake

#Apple
apple = on_grid_random() #Definição da posição inicial da maça
apple_skin = pygame.Surface((10,10)) #Define o tamanho da maça
apple_skin.fill((255,0,0)) #Pinta a maça

#Paredes
wall = []
for k in range(0,600,10): #Criação da parede da esquerda
    wall.append((0,k))
for k in range(0,600,10): #Criação da parede de cima
    wall.append((k,0))
for k in range(0,600,10): #Criação da parede da direita
    wall.append((590,k))
for k in range(0,600,10): #Criação da parede de baixo
    wall.append((k,590))
wall_skin = pygame.Surface((10,10)) #Define cada quadrado da parede como 10x10
wall_skin.fill((0,0,255)) #Coloca a cor Azul como das paredes

clock = pygame.time.Clock() #Cria um controlador de FPS

while True:
    clock.tick(15) #Seta o FPS

    for event in pygame.event.get(): #Verificar se aconteceu alguma ação do player
        if event.type == QUIT: #Caso ele feche o jogo
            pygame.quit() #O jogo é fechado

        if event.type == KEYDOWN: #Caso ocorra um evento de click
            if event.key == K_UP:   #Evento de apertar a Key seta para cima
                my_direction = UP #Muda a direção, (direção definida na linha 13)
            if event.key == K_DOWN: #Evento de apertar a Key seta para baixo
                my_direction = DOWN #Muda a direção, (direção definida na linha 14)
            if event.key == K_LEFT: #Evento de apertar a Key seta para esquerda
                my_direction = LEFT #Muda a direção, (direção definida na linha 15)
            if event.key == K_RIGHT: #Evento de apertar a Key seta para direita
                my_direction = RIGHT #Muda a direção, (direção definida na linha 14)

    if collision(snake[0], apple): #Confere para ver se há colisão entre a maçã e a cabeça da Snake
        apple = on_grid_random() #Gera uma nova maçã
        snake.append((0,0)) #Adiciona mais um quadrado a Snake

    for j in range(1,len(snake)):
        if collision(snake[0], snake[j]): #Confere para ver se há colisões entre a cabeça da Snake e o corpo
            print('End Game.')
            pygame.quit() #Fecha o jogo

    for l in range(0,len(wall)):
        if collision(snake[0],wall[l]): #Confere para ver se há colisões entre a Snake e as paredes
            print('End Game')
            pygame.quit() #Fecha o jogo

    for i in range(len(snake) -1,0,-1): #Move todas as partes da cobra para a posição na sua frente
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Muda as direções da cobra de acordo com o grid de 10
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0)) #Limpa a tela

    screen.blit(apple_skin,apple) #Desenha a maça

    for pos in snake: #Desenha a cobra
        screen.blit(snake_skin,pos)

    for paredis in wall: #Desenha todas as paredes
        screen.blit(wall_skin, paredis)

    pygame.display.update() #Atualiza a janela com as novas informações.