import tkinter  # importamos a biblioteca tkinter


class App:
    """
    Aplicativo para somar e diminuir utilizando uma interface gráfica.
    """

    def __init__(self):

        self.janela = tkinter.Tk()  # Criamos a variável "janela" e nela iniciamos o Tkinter.
        self.valor = 6  # Informamos um valor inicial.
        self.janela.title("Tkinter - Soma e Subtração")  # Informamos um título para a "janela".
        self.janela.minsize(width=360, height=540)  # Aqui passamos o tamanho mínimo da tela.
        self.janela.maxsize(width=360, height=640)  # Com o width máximo igual ao mínimo a tela não altera.

        # Criamos a variável texto para exibir o valor.
        self.texto = tkinter.Label(text="7", font="Arial 80 bold", pady=50)
        self.texto.pack()

        # Aqui vamos criar um frame/quadro que auxilia na organização dos botões
        self.frame = tkinter.Frame(self.janela, bg="white")
        self.frame.pack()

        # Agora vamos criar os botões e informar os seguintes parâmetros.
        # Localização; texto; background color, tamanho, comando/função.
        self.button_plus = tkinter.Button(self.frame, text="UP", bg="green", width=12, command=self.plus)
        # Posicionamento do botão
        self.button_plus.pack(side='left')

        self.button_down = tkinter.Button(self.frame, text="DOWN", bg="red", width=12, command=self.down)
        self.button_down.pack(side="right")

        # Mainloop() serve para manter a janela aberta.
        self.janela.mainloop()

    def plus(self):
        """Função adiciona um número enquanto o valor for menor que 16."""
        if self.valor < 16:
            self.valor += 1
            self.texto.config(text=f"{self.valor}")

    def down(self):
        """Função subtrai um número enquanto o valor for maior que 1."""
        if self.valor > 1:
            self.valor -= 1
            self.texto.config(text=f'{self.valor}')


App()
