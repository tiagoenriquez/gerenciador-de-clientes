from tkinter import messagebox
import tkinter as tk


class MainView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gerenciador de Clientes")
        WIDTH = 64
        self.messagebox = messagebox

        cadastro_panel = tk.Frame(self.window)
        cadastro_panel.grid(row=0, column=0)

        campos_panel = tk.Frame(cadastro_panel)
        campos_panel.grid(row=0, column=0)

        nome_label = tk.Label(campos_panel, text="Nome", width=int((WIDTH-3/8)/2))
        nome_label.grid(row=0, column=0, padx=8, pady=8)

        self.nome_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self.nome_entry.grid(row=0, column=1, padx=8, pady=8)

        sobrenome_label = tk.Label(campos_panel, text="Sobrenome", width=int((WIDTH-3/8)/2))
        sobrenome_label.grid(row=1, column=0, padx=8, pady=8)

        self.sobrenome_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self.sobrenome_entry.grid(row=1, column=1, padx=8, pady=8)

        email_label = tk.Label(campos_panel, text="E-mail", width=int((WIDTH-3/8)/2))
        email_label.grid(row=2, column=0, padx=8, pady=8)

        self.email_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self.email_entry.grid(row=2, column=1, padx=8, pady=8)

        cpf_label = tk.Label(campos_panel, text="CPF", width=int((WIDTH-3/8)/2))
        cpf_label.grid(row=3, column=0, padx=8, pady=8)

        self.cpf_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self.cpf_entry.grid(row=3, column=1, padx=8, pady=8)

        botoes_panel = tk.Frame(cadastro_panel)
        botoes_panel.grid(row=1, column=0)

        self.todos_button = tk.Button(botoes_panel, text="Ver todos", width=WIDTH-4)
        self.todos_button.grid(row=0, column=0, padx=8, pady=8)

        self.buscar_button = tk.Button(botoes_panel, text="Buscar", width=WIDTH-4)
        self.buscar_button.grid(row=1, column=0, padx=8, pady=8)

        self.inserir_button = tk.Button(botoes_panel, text="Inserir", width=WIDTH-4)
        self.inserir_button.grid(row=2, column=0, padx=8, pady=8)

        self.atualizar_button = tk.Button(botoes_panel, text="Atualizar", width=WIDTH-4)
        self.atualizar_button.grid(row=3, column=0, padx=8, pady=8)

        self.deletar_button = tk.Button(botoes_panel, text="Deletar", width=WIDTH-4)
        self.deletar_button.grid(row=4, column=0, padx=8, pady=8)

        self.fechar_button = tk.Button(botoes_panel, text="Fechar", width=WIDTH-4)
        self.fechar_button.grid(row=5, column=0, padx=8, pady=8)

        info_panel = tk.Frame(self.window)
        info_panel.grid(row=0, column=1, padx=8, pady=8)

        scrollbar = tk.Scrollbar(info_panel)
        scrollbar.pack(side="right", fill="y")

        self.clientes_list = tk.Listbox(info_panel, yscrollcommand=scrollbar.set, width=80, height=24)
        self.clientes_list.pack(side="left", fill="both")
        scrollbar.config(command=self.clientes_list.yview)