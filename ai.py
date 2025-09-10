import pygame
import neat
import pickle
import os
from game import Passaro, Cano, Chao, desenhar_tela, TELA_LARGURA, TELA_ALTURA

def treinar(config_path, geracoes=50, salvar_em="best.pkl"):
    geracao = 0
    recorde = 0

    def main(genomas, config):
        nonlocal geracao, recorde
        geracao += 1
        redes = []
        lista_genomas = []
        passaros = []
        for _, genoma in genomas:
            rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            redes.append(rede)
            genoma.fitness = 0
            lista_genomas.append(genoma)
            passaros.append(Passaro(230, 350))
        chao = Chao(730)
        canos = [Cano(700)]
        tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
        pontos = 0
        relogio = pygame.time.Clock()
        rodando = True
        while rodando:
            relogio.tick(30)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
            indice_cano = 0
            if len(passaros) > 0:
                if len(canos) > 1 and passaros[0].x > (canos[0].x + canos[0].CANO_TOPO.get_width()):
                    indice_cano = 1
            else:
                rodando = False
                break
            for i, passaro in enumerate(passaros):
                passaro.mover()
                lista_genomas[i].fitness += 0.1
                output = redes[i].activate((
                    passaro.y,
                    abs(passaro.y - canos[indice_cano].altura),
                    abs(passaro.y - canos[indice_cano].pos_base)
                ))
                if output[0] > 0.5:
                    passaro.pular()
            chao.mover()
            adicionar_cano = False
            remover_canos = []
            for cano in canos:
                for i, passaro in enumerate(passaros):
                    if cano.colidir(passaro):
                        passaros.pop(i)
                        lista_genomas[i].fitness -= 1
                        lista_genomas.pop(i)
                        redes.pop(i)
                    if not cano.passou and passaro.x > cano.x:
                        cano.passou = True
                        adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)
            if adicionar_cano:
                pontos += 1
                if pontos > recorde:
                    recorde = pontos
                canos.append(Cano(600))
                for genoma in lista_genomas:
                    genoma.fitness += 10
            for cano in remover_canos:
                canos.remove(cano)
            for i, passaro in enumerate(passaros):
                if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                    passaros.pop(i)
                    lista_genomas.pop(i)
                    redes.pop(i)
            desenhar_tela(tela, passaros, canos, chao, pontos, True, geracao, len(passaros), recorde)

    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )
    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())
    vencedor = populacao.run(main, geracoes)
    with open(salvar_em, "wb") as f:
        pickle.dump(vencedor, f)

def jogar_humano():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True
    while rodando:
        relogio.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                passaros[0].pular()
        indice_cano = 0
        if len(canos) > 1 and passaros[0].x > (canos[0].x + canos[0].CANO_TOPO.get_width()):
            indice_cano = 1
        for passaro in passaros:
            passaro.mover()
        chao.mover()
        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for passaro in passaros:
                if cano.colidir(passaro):
                    rodando = False
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)
        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)
        for passaro in passaros:
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                rodando = False
        desenhar_tela(tela, passaros, canos, chao, pontos, False, 0, 0, 0)

def assistir_ia(config_path, genome_path="best.pkl"):
    if not os.path.exists(genome_path):
        return
    with open(genome_path, "rb") as f:
        genome = pickle.load(f)
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )
    rede = neat.nn.FeedForwardNetwork.create(genome, config)
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    recorde = 0
    relogio = pygame.time.Clock()
    geracao = 0
    rodando = True
    while rodando:
        relogio.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        indice_cano = 0
        if len(canos) > 1 and passaros[0].x > (canos[0].x + canos[0].CANO_TOPO.get_width()):
            indice_cano = 1
        p = passaros[0]
        p.mover()
        saida = rede.activate((p.y, abs(p.y - canos[indice_cano].altura), abs(p.y - canos[indice_cano].pos_base)))
        if saida[0] > 0.5:
            p.pular()
        chao.mover()
        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            if cano.colidir(p):
                rodando = False
            if not cano.passou and p.x > cano.x:
                cano.passou = True
                adicionar_cano = True
            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)
        if adicionar_cano:
            pontos += 1
            if pontos > recorde:
                recorde = pontos
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)
        if (p.y + p.imagem.get_height()) > chao.y or p.y < 0:
            rodando = False
        desenhar_tela(tela, passaros, canos, chao, pontos, True, geracao, 1, recorde)
