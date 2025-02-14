import tkinter as tk
from tkinter import messagebox

# Função para obter as coordenadas de um caractere no teclado
def obter_coordenadas(char, keyboard):
    for y, linha in enumerate(keyboard):  # Percorre as linhas (y)
        for x, tecla in enumerate(linha):  # Percorre as colunas (x)
            if tecla == char:
                return [y, x]
    return None

# Função principal que será chamada ao clicar no botão
def processar_senha():
    Senha = entry_senha.get()
    Seed = entry_seed.get()

    if not Senha or not Seed:
        messagebox.showerror("Erro", "Por favor, preencha a senha e a seed.")
        return

    Val = [ord(i) for i in Seed]
    Direcao = sum(Val) % 4

    Key1 = [obter_coordenadas(char, Keyboard) for char in Senha]

    match Direcao:
        case 1:
            for z in Key1:
                z[0] += 1
        case 2:
            for z in Key1:
                z[1] += 1
        case 3:
            for z in Key1:
                z[0] -= 1
        case 0:
            for z in Key1:
                z[1] -= 1

    resultado = ''
    for i in Key1:
        try:
            resultado += Keyboard[i[0]][i[1]]
        except Exception as e:
            try:
                resultado += Keyboard[i[0]][0]
            except Exception as e:
                resultado += Keyboard[0][i[1]]

    label_resultado.config(text=f"Resultado: {resultado}")

# Definindo o teclado
Keyboard = [
    ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+"],
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç', '}'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', ':', '?'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '['],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', ']'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', ';', '/']
]

# Criando a janela principal
janela = tk.Tk()
janela.title("Criptografia de Senha")
janela.geometry("400x300")  # Tamanho da janela

# Estilo
fonte = ("Arial", 12)
cor_fundo = "#f0f0f0"
cor_botao = "#4CAF50"
cor_texto = "#000000"

janela.configure(bg=cor_fundo)

# Campo de entrada para a senha
label_senha = tk.Label(janela, text="Senha:", font=fonte, bg=cor_fundo, fg=cor_texto)
label_senha.pack(pady=5)

entry_senha = tk.Entry(janela, font=fonte)
entry_senha.pack(pady=5)

# Campo de entrada para a seed
label_seed = tk.Label(janela, text="Seed:", font=fonte, bg=cor_fundo, fg=cor_texto)
label_seed.pack(pady=5)

entry_seed = tk.Entry(janela, font=fonte)
entry_seed.pack(pady=5)

# Botão para processar
botao_processar = tk.Button(janela, text="Processar", font=fonte, bg=cor_botao, fg="white", command=processar_senha)
botao_processar.pack(pady=10)

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="Resultado: ", font=fonte, bg=cor_fundo, fg=cor_texto)
label_resultado.pack(pady=10)

# Iniciando o loop principal da interface gráfica
janela.mainloop()