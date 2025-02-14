# Gerador de senha criptografada

Este projeto é uma aplicação GUI (Graphical User Interface) desenvolvida em Python utilizando a biblioteca Tkinter. O objetivo da aplicação é criptografar uma senha com base em um teclado virtual e uma seed fornecida pelo usuário.

## Dependências

- Python 3.X

## Como Funciona

A aplicação solicita ao usuário duas entradas: uma senha e uma seed. Com base na seed, um valor direcional é calculado, e a senha é modificada conforme a direção calculada.

### Algoritmo de Criptografia

1. **Coleta das Coordenadas**: Cada caractere da senha é mapeado para suas coordenadas no teclado virtual.
2. **Cálculo da Direção**: A seed é transformada em valores inteiros e a direção da modificação é calculada com base na soma dos valores.
3. **Modificação da Senha**:
   - Se a direção for `1`, a coordenada `y` de cada caractere é incrementada em `1`.
   - Se a direção for `2`, a coordenada `x` de cada caractere é incrementada em `1`.
   - Se a direção for `3`, a coordenada `y` de cada caractere é decrementada em `1`.
   - Se a direção for `0`, a coordenada `x` de cada caractere é decrementada em `1`.
4. **Construção da Senha Modificada**: Com base nas novas coordenadas, a senha modificada é construída.

## Estrutura do Projeto

- **main.py**: Arquivo principal contendo a lógica da aplicação.
- **Keyboard**: Matriz representando o teclado virtual utilizado para mapear as coordenadas dos caracteres.

## Instruções para Execução

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Execute o arquivo `main.py`:
   ```bash
   python main.py
