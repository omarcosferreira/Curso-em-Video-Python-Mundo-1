import pygame
# Inicializar o Pygame
pygame.init()
# Criar uma janela
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Reproduzindo Música")
pygame.mixer.music.load('aex021.mp3')
pygame.mixer.music.play()
# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Finalizar o Pygame
pygame.quit()
