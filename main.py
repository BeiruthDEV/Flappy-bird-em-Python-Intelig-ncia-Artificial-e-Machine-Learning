import pygame
import sys
from ai import treinar, jogar_humano, assistir_ia

pygame.init()
LARG, ALT = 500, 800
TELA = pygame.display.set_mode((LARG, ALT))
pygame.display.set_caption("Flappy AI")
FONTE = pygame.font.SysFont("arial", 44)
FONTE_SMALL = pygame.font.SysFont("arial", 28)
CONFIG_PATH = "config.txt"

def desenhar_menu(selecao):
    TELA.fill((20, 20, 25))
    titulo = FONTE.render("Flappy Bird • IA", True, (255, 255, 255))
    TELA.blit(titulo, (LARG//2 - titulo.get_width()//2, 120))
    opcoes = ["Jogar (Humano)", "Treinar IA", "Assistir IA"]
    for i, txt in enumerate(opcoes):
        cor_bg = (50, 50, 60) if i == selecao else (35, 35, 40)
        cor_tx = (255, 255, 255) if i == selecao else (200, 200, 210)
        rect = pygame.Rect(LARG//2 - 160, 260 + i*100, 320, 70)
        pygame.draw.rect(TELA, cor_bg, rect, border_radius=16)
        label = FONTE_SMALL.render(txt, True, cor_tx)
        TELA.blit(label, (rect.centerx - label.get_width()//2, rect.centery - label.get_height()//2))
    dica = FONTE_SMALL.render("↑↓ para navegar • Enter para selecionar", True, (160, 160, 170))
    TELA.blit(dica, (LARG//2 - dica.get_width()//2, ALT - 80))
    pygame.display.update()

def main():
    selecao = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        desenhar_menu(selecao)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_UP, pygame.K_w):
                    selecao = (selecao - 1) % 3
                if e.key in (pygame.K_DOWN, pygame.K_s):
                    selecao = (selecao + 1) % 3
                if e.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if selecao == 0:
                        jogar_humano()
                    elif selecao == 1:
                        treinar(CONFIG_PATH, geracoes=50, salvar_em="best.pkl")
                    elif selecao == 2:
                        assistir_ia(CONFIG_PATH, genome_path="best.pkl")
        pygame.display.update()

if __name__ == "__main__":
    main()
