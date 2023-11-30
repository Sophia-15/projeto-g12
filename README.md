<h1 align="center">
 ECOWAVE ARCADE
</h1>

<p align="center">
  <a href="#sobre">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando">Rodando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#código">Explicando o código do menu?</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#arduino">Como construir?</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#jogos">Jogos</a>
</p> 

![ecowave](https://github.com/Sophia-15/projeto-g12/assets/67246528/fd7debaf-04e8-48dd-aedf-40059c31b361)


## Sobre
Este trabalho tem como objetivo o incentivo ao descarte adequado de materiais e
componentes eletrônicos comuns, para fins como reciclagem ou reutilização dos
mesmos. Além disso, ele oferece uma solução para a falta de reciclagem de componentes
eletrônicos, muito utilizados nas Smart Cities.

## Rodando
Clone esse projeto e acesse sua pasta

```bash
$ git clone https://github.com/Sophia-15/projeto-g12.git && cd projeto-g12
```

Siga os passos abaixo
```bash
# Instalar as dependências 
$ pip install -r requirements.txt
```
- Entre no arquivo de ```variables.py``` existentes na pasta ```menu``` e ```tetris``` e altere o caminho das variáveis
- Agora é só entrar na pasta ```menu``` no arquivo ```menu.py``` e rodar!

## Código
<p>

O fluxo do programa é iniciado com a chamada da função ```menu()```. Dentro dessa função, encontra-se a invocação da função ```resting_screen()```, responsável por exibir a tela de descanso do jogo enquanto o jogador não inserir uma pilha. Após a inserção da pilha pelo jogador, o contador responsável por determinar qual função será executada é ajustado para ```1```, revelando o menu com as opções de jogo.

Dentro do menu de jogos, há outro contador utilizado para a seleção dos tipos de jogos disponíveis, sendo o "Infinity Runner" representado pelo valor ```0``` e o "Tetris" pelo valor ```1```.

Ao concluir um jogo, a função ```handle_choose_name()``` é acionada, permitindo que o usuário insira seu nome de usuário. Esta função retorna o número ```0``` e, ao atribuir esse valor ao contador correspondente, o programa é redirecionado de volta à tela de descanso, reiniciando o ciclo do jogo representado pela função ```resting_screen()```.

Adicionalmente, implementamos a lógica para a alternância de cor do texto. Essa lógica calcula a diferença entre o tempo atual, medido em milissegundos, e o valor previamente registrado. Em seguida, compara essa diferença com o intervalo de tempo predefinido para o efeito de piscar. Se a diferença for superior a esse intervalo, a variável booleana ```show_text``` é modificada, e os milissegundos atuais são registrados na variável que mantém o último instante em que ocorreu a mudança de cor no texto.

![image](https://github.com/Sophia-15/projeto-g12/assets/67246528/63870354-d844-45f1-b5b3-b5ef1b9bbb8f)
</p>

## Arduino
<p>
 Abaixo, temos um tutorial de como construímos nosso arcade.
</p>

[Montagem do protótipo](https://github.com/Sophia-15/projeto-g12/files/13507701/Tutorial.de.Montagem.pdf)


## Jogos
<p>
  Dado que nosso projeto remete ao ambiente de fliperama, optamos por selecionar jogos clássicos, entre os quais se destacam o Tetris e o Infinity Runner.
</p>

### Infinity Runner
[PDf explicando o desenvolvimento do Infinity Runner](https://github.com/Sophia-15/projeto-g12/files/13507514/Tutorial_InfinityRunner.pdf)

---

Feito com 💚 por G12 




