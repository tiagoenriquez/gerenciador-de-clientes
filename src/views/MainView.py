import tkinter as tk


class MainView:
    def __init__(self):
        self._window = tk.Tk()
        self._window.title("Gerenciador de Clientes")

        self._cadastro_panel = tk.Frame(self._window)
        self._cadastro_panel.grid(row=0, column=0)

        self._campos_panel = tk.Frame(self._window)
        self._campos_panel.grid(row=0, column=0)

        self._nome_label = tk.Label(self._campos_panel, text="Nome")
        self._nome_label.grid(row=0, column=0, padx=8, pady=8)

        self._nome_entry = tk.Entry(self. _campos_panel)
        self._nome_entry.grid(row=0, column=1, padx=8, pady=8)

        self._sobrenome_label = tk.Label(self._campos_panel, text="Sobrenome")
        self._sobrenome_label.grid(row=1, column=0, padx=8, pady=8)

        self._sobrenome_entry = tk.Entry(self. _campos_panel)
        self._sobrenome_entry.grid(row=1, column=1, padx=8, pady=8)

        self._email_label = tk.Label(self._campos_panel, text="E-mail")
        self._email_label.grid(row=2, column=0, padx=8, pady=8)

        self._email_entry = tk.Entry(self. _campos_panel)
        self._email_entry.grid(row=2, column=1, padx=8, pady=8)

        self._cpf_label = tk.Label(self._campos_panel, text="CPF")
        self._cpf_label.grid(row=3, column=0, padx=8, pady=8)

        self._cpf_entry = tk.Entry(self. _campos_panel)
        self._cpf_entry.grid(row=3, column=1, padx=8, pady=8)

        self._botoes_panel = tk.Frame(self._window)
        self._botoes_panel.grid(row=1, column=0)

        self._todos_button = tk.Button(self._botoes_panel, text="Ver todos")
        self._todos_button.grid(row=0, column=0, padx=8, pady=8)

        self._buscar_button = tk.Button(self._botoes_panel, text="Buscar")
        self._buscar_button.grid(row=1, column=0, padx=8, pady=8)

        self._inserir_button = tk.Button(self._botoes_panel, text="Inserir")
        self._inserir_button.grid(row=2, column=0, padx=8, pady=8)

        self._atualizar_button = tk.Button(self._botoes_panel, text="Atualizar Selecionados")
        self._atualizar_button.grid(row=3, column=0, padx=8, pady=8)

        self._deletar_button = tk.Button(self._botoes_panel, text="Deletar Selecionados")
        self._deletar_button.grid(row=4, column=0, padx=8, pady=8)

        self._fechar_button = tk.Button(self._botoes_panel, text="Fechar")
        self._fechar_button.grid(row=5, column=0, padx=8, pady=8)

        self._info_panel = tk.Frame(self._window)
        self._info_panel.grid(row=0, column=1, padx=8, pady=8)

        self._window.mainloop()