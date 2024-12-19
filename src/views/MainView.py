from tkinter import messagebox
import tkinter as tk
from src.models.Cliente import Cliente
from src.services.ClienteService import ClienteService


class MainView:
    def __init__(self):
        self._window = tk.Tk()
        self._window.title("Gerenciador de Clientes")
        WIDTH = 64

        cadastro_panel = tk.Frame(self._window)
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

        buscar_button = tk.Button(botoes_panel, text="Buscar", width=WIDTH-4, command=self._procurar)
        buscar_button.grid(row=1, column=0, padx=8, pady=8)

        inserir_button = tk.Button(botoes_panel, text="Inserir", width=WIDTH-4, command=self._inserir)
        inserir_button.grid(row=2, column=0, padx=8, pady=8)

        atualizar_button = tk.Button(
            botoes_panel,
            text="Atualizar Selecionados",
            width=WIDTH-4,
            command=self._atualizar
        )
        atualizar_button.grid(row=3, column=0, padx=8, pady=8)

        deletar_button = tk.Button(botoes_panel, text="Deletar Selecionados", width=WIDTH-4, command=self._excluir)
        deletar_button.grid(row=4, column=0, padx=8, pady=8)

        fechar_button = tk.Button(botoes_panel, text="Fechar", width=WIDTH-4, command=self._fechar)
        fechar_button.grid(row=5, column=0, padx=8, pady=8)

        info_panel = tk.Frame(self._window)
        info_panel.grid(row=0, column=1, padx=8, pady=8)

        scrollbar = tk.Scrollbar(info_panel)
        scrollbar.pack(side="right", fill="y")

        self._clientes_list = tk.Listbox(info_panel, yscrollcommand=scrollbar.set, width=80, height=24)
        self._clientes_list.pack(side="left", fill="both")
        scrollbar.config(command=self._clientes_list.yview)

        self._window.mainloop()
    
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
            self._clientes_list.delete(0, tk.END)
            for cliente in ClienteService().listar():
                self._clientes_list.insert(
                    tk.END,
                    f"{cliente.id}: {cliente.nome} {cliente.sobrenome}. E-mail: {cliente.email}. CPF: {cliente.cpf}"
                )
            self._limpar()
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])
    
    def _procurar(self):
        try:
            self._cliente = ClienteService().procurar(int(self._clientes_list.selection_get().split(":")[0]))
            self._nome_entry.delete(0, tk.END)
            self._nome_entry.insert(0, self._cliente.nome)
            self._sobrenome_entry.delete(0, tk.END)
            self._sobrenome_entry.insert(0, self._cliente.sobrenome)
            self._email_entry.delete(0, tk.END)
            self._email_entry.insert(0, self._cliente.email)
            self._cpf_entry.delete(0, tk.END)
            self._cpf_entry.insert(0, self._cliente.cpf.replace(".", "").replace("-", ""))
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])
    
    def _limpar(self):
        self._cliente = None
        self._nome_entry.delete(0, tk.END)
        self._nome_entry.insert(0, "")
        self._sobrenome_entry.delete(0, tk.END)
        self._sobrenome_entry.insert(0, "")
        self._email_entry.delete(0, tk.END)
        self._email_entry.insert(0, "")
        self._cpf_entry.delete(0, tk.END)
        self._cpf_entry.insert(0, "")
    
    def _atualizar(self):
        try:
            ClienteService().atualizar(Cliente(
                self._nome_entry.get(),
                self._sobrenome_entry.get(),
                self._email_entry.get(),
                self._cpf_entry.get(),
                self._cliente.id
            ))
            self._listar()
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])
    
    def _excluir(self):
        try:
            ClienteService().excluir(self._cliente.id)
            self._listar()
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])
    
    def _fechar(self):
        self._window.destroy()