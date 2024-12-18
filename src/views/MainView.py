from tkinter import messagebox
import tkinter as tk
from src.models.Cliente import Cliente
from src.services.ClienteService import ClienteService


class MainView:
    def __init__(self):
        window = tk.Tk()
        window.title("Gerenciador de Clientes")
        WIDTH = 64

        cadastro_panel = tk.Frame(window)
        cadastro_panel.grid(row=0, column=0)

        campos_panel = tk.Frame(cadastro_panel)
        campos_panel.grid(row=0, column=0)

        nome_label = tk.Label(campos_panel, text="Nome", width=int((WIDTH-3/8)/2))
        nome_label.grid(row=0, column=0, padx=8, pady=8)

        self._nome_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self._nome_entry.grid(row=0, column=1, padx=8, pady=8)

        sobrenome_label = tk.Label(campos_panel, text="Sobrenome", width=int((WIDTH-3/8)/2))
        sobrenome_label.grid(row=1, column=0, padx=8, pady=8)

        self._sobrenome_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self._sobrenome_entry.grid(row=1, column=1, padx=8, pady=8)

        email_label = tk.Label(campos_panel, text="E-mail", width=int((WIDTH-3/8)/2))
        email_label.grid(row=2, column=0, padx=8, pady=8)

        self._email_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self._email_entry.grid(row=2, column=1, padx=8, pady=8)

        cpf_label = tk.Label(campos_panel, text="CPF", width=int((WIDTH-3/8)/2))
        cpf_label.grid(row=3, column=0, padx=8, pady=8)

        self._cpf_entry = tk.Entry(campos_panel, width=int((WIDTH-3/8)/2))
        self._cpf_entry.grid(row=3, column=1, padx=8, pady=8)

        botoes_panel = tk.Frame(cadastro_panel)
        botoes_panel.grid(row=1, column=0)

        todos_button = tk.Button(botoes_panel, text="Ver todos", width=WIDTH-4, command=self._listar)
        todos_button.grid(row=0, column=0, padx=8, pady=8)

        buscar_button = tk.Button(botoes_panel, text="Buscar", width=WIDTH-4)
        buscar_button.grid(row=1, column=0, padx=8, pady=8)

        inserir_button = tk.Button(botoes_panel, text="Inserir", width=WIDTH-4, command=self._inserir)
        inserir_button.grid(row=2, column=0, padx=8, pady=8)

        atualizar_button = tk.Button(botoes_panel, text="Atualizar Selecionados", width=WIDTH-4)
        atualizar_button.grid(row=3, column=0, padx=8, pady=8)

        deletar_button = tk.Button(botoes_panel, text="Deletar Selecionados", width=WIDTH-4)
        deletar_button.grid(row=4, column=0, padx=8, pady=8)

        fechar_button = tk.Button(botoes_panel, text="Fechar", width=WIDTH-4)
        fechar_button.grid(row=5, column=0, padx=8, pady=8)

        info_panel = tk.Frame(window)
        info_panel.grid(row=0, column=1, padx=8, pady=8)

        scrollbar = tk.Scrollbar(info_panel)
        scrollbar.pack(side="right", fill="y")

        self._clientes_list = tk.Listbox(info_panel, yscrollcommand=scrollbar.set, width=80, height=24)
        self._clientes_list.pack(side="left", fill="both")
        scrollbar.config(command=self._clientes_list.yview)

        window.mainloop()
    
    def _inserir(self):
        try:
            ClienteService().inserir(Cliente(
                self._nome_entry.get(),
                self._sobrenome_entry.get(),
                self._email_entry.get(),
                self._cpf_entry.get()
            ))
            self._listar()
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])
    
    def _listar(self):
        try:
            for cliente in ClienteService().listar():
                self._clientes_list.insert(
                    tk.END,
                    f"{cliente.id}: {cliente.nome} {cliente.sobrenome}. E-mail: {cliente.email}. CPF: {cliente.cpf}"
                )
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])