***Jogo SnakeHat***

Este é um jogo em Pygame baseado no livro "O Pequeno Príncipe". O objetivo do jogo é acertar uma cobra em um elefante, inspirado na imagem do livro da cobra que comeu um elefante. O jogo consiste em atirar a cobra do canhão do Pequeno Príncipe, evitando colisões com planetas e tentando acertar o elefante.

***Como jogar***

1. Clique no botão de play para iniciar o jogo.
2. Use o mouse para arrastar o canhão do Pequeno Príncipe para escolher a direção e a força do tiro. Quanto mais longe você arrastar, mais forte será o tiro.
3. Solte o mouse para atirar a cobra.
4. Desvie dos planetas e outros obstáculos no caminho para chegar ao elefante e acertá-lo.
5. O jogador possui vidas representadas por corações. Se o jogador não conseguir avançar até a última etapa do jogo sem perder todas as vidas, ele perde.

***Como executar o programa***

1. Instale o Pygame. Caso ainda não tenha instalado, você pode utilizar o seguinte comando no terminal: pip install pygame.
2. Clone este repositório.
3. Navegue até o diretório do repositório clonado.
4. Execute o arquivo main.py usando o seguinte comando no terminal: python main.py.


***Modelo Físico***

O modelo físico implementado no jogo é baseado na equação da gravitação universal de Newton, que descreve a força gravitacional entre duas partículas. A força gravitacional é diretamente proporcional ao produto das massas das partículas e inversamente proporcional ao quadrado da distância entre elas.

Neste jogo, a cobra é considerada uma partícula de massa m, enquanto o elefante e planetas são considerados partículas de massa M. A distância entre as partículas é calculada a partir da posição da cobra e dos outros objetos.

Usando a equação da gravitação universal, a força gravitacional é calculada e usada para alterar a velocidade da cobra ao longo do tempo, de acordo com a segunda lei de Newton (F = ma). A aceleração resultante é usada para atualizar a posição da cobra em cada quadro do jogo.

Além disso, o jogo inclui buracos de minhoca, alteram a posição da cobra para a de um outro buraco presente na tela. É apenas mantido os vetores da velocidade e trocando apenas a posição da cobra.

***Créditos***

Este jogo foi desenvolvido por Alan Matheus e Esdras Gomes. O modelo físico foi baseado em conceitos de física clássica e matemática. A imagem do elefante comendo a cobra é uma referência à história "O Pequeno Príncipe", de Antoine de Saint-Exupéry. Como na história, a cobra neste jogo é capaz de superar obstáculos aparentemente insuperáveis e até mesmo devorar um elefante. "O essencial é invisível aos olhos", mas neste jogo a precisão matemática e a estratégia são essenciais para atingir o objetivo.
