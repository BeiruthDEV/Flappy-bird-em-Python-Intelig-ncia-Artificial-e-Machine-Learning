<p align="center">
  <img src="assets/logo-vassouras.png" alt="Universidade de Vassouras" width="400"/>
</p>

<h3 align="center">
  Universidade de Vassouras  
</h3>

---

### 📚 Curso: **Engenharia de Software**  
### 🖥️ Disciplina: **Inteligência Artificial e Machine Learning**  
### 👨‍🎓 Autor: **Matheus Beiruth**

---

🐦 Flappy Bird com Inteligência Artificial (NEAT + Python)

Este projeto é uma recriação do clássico Flappy Bird, desenvolvido em Python com a biblioteca Pygame, e com suporte a Inteligência Artificial via NEAT (NeuroEvolution of Augmenting Topologies).

A IA é capaz de aprender a jogar sozinha, evoluindo a cada geração até superar a pontuação humana.
O jogador também pode escolher jogar manualmente.

🚀 Funcionalidades

🎮 Modo Jogador – você controla o pássaro com a barra de espaço.

🤖 Modo Treinar IA – populações de pássaros são treinadas usando NEAT.

👀 Modo Assistir IA – carrega um modelo treinado (best.pkl) e deixa a IA jogar sozinha.

📊 HUD Profissional – exibe pontuação, geração, número de pássaros vivos e melhor pontuação histórica.

🔊 Sons e Gráficos – gameplay fiel ao original.


## 📂 Estrutura do Projeto
```bash
FlappyBird/
│── main.py              # Ponto de entrada (menu principal)
│── ai.py                # Treinamento e execução da IA (NEAT)
│── game.py              # Classes do jogo (Pássaro, Cano, Chão, HUD)
│── config.txt           # Configurações do NEAT
│── best.pkl             # Modelo treinado salvo (gerado após treino)
│── assets/              # Imagens, sons e fontes
│── README.md            # Este arquivo
```

## ⚙️ Instalação
1. Clone o repositório

```bash
git clone https://github.com/BeiruthDEV/Flappy-bird-em-Python-Intelig-ncia-Artificial-e-Machine-Learning
cd flappybird-ia
```

2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv

Ativar:

Windows (VsCode)
```bash
.\venv\Scripts\Activate
```

Linux / Mac
```bash
source venv/bin/activate
```

3. Instale as dependências
pip install pygame neat-python


▶️ Como Rodar

Sempre execute o main.py

No menu inicial, escolha:

Jogar (Humano) → controle com barra de espaço

Treinar IA → roda várias gerações e salva o melhor modelo em best.pkl

Assistir IA → usa o best.pkl salvo para jogar automaticamente



🧠 Treinamento da IA

O algoritmo NEAT cria uma população inicial de redes neurais.

A cada geração, os melhores pássaros (maior pontuação) são usados para reproduzir novas redes.

Depois de algumas gerações, a IA consegue jogar de forma estável.

O melhor genome é salvo em best.pkl.


🖼️ Demonstração

## 🖼️ Demonstração
![Gameplay](assets/demo.gif)


👨‍💻 Tecnologias

Python 3.11+

Pygame
 – gráficos e sons

NEAT-Python
 – IA evolutiva


📜 Licença

Este projeto foi desenvolvido para fins educacionais.
Você pode usá-lo livremente, mas dê os créditos.