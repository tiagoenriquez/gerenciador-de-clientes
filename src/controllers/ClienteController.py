import tkinter as tk
from src.models.Cliente import Cliente
from src.services.ClienteService import ClienteService
from src.views.MainView import MainView


class ClienteController():
    def __init__(self):
        self.view = MainView()
        self._adicionar_eventos()
        self.view.window.mainloop()

    def _adicionar_eventos(self):
        self.view.todos_button.config(command=self._listar)
        self.view.buscar_button.config(command=self._procurar)
        self.view.inserir_button.config(command=self._inserir)
        self.view.atualizar_button.config(command=self._atualizar)
        self.view.deletar_button.config(command=self._excluir)
        self.view.fechar_button.config(command=self._fechar)

    def _inserir(self):
        try:
            ClienteService().inserir(Cliente(
                self.view.nome_entry.get(),
                self.view.sobrenome_entry.get(),
                self.view.email_entry.get(),
                self.view.cpf_entry.get()
            ))
            self._listar()
        except Exception as exception:
            self.view.messagebox.showerror("Erro", exception.args[0])
    
    def _listar(self):
        try:
            self.view.clientes_list.delete(0, tk.END)
            for cliente in ClienteService().listar():
                self.view.clientes_list.insert(
                    tk.END,
                    f"{cliente.id}: {cliente.nome} {cliente.sobrenome}. E-mail: {cliente.email}. CPF: {cliente.cpf}"
                )
            self._limpar()
        except Exception as exception:
            self.view.messagebox.showerror("Erro", exception.args[0])
    
    def _procurar(self):
        try:
            self._cliente = ClienteService().procurar(int(self.view.clientes_list.selection_get().split(":")[0]))
            self.view.nome_entry.delete(0, tk.END)
            self.view.nome_entry.insert(0, self._cliente.nome)
            self.view.sobrenome_entry.delete(0, tk.END)
            self.view.sobrenome_entry.insert(0, self._cliente.sobrenome)
            self.view.email_entry.delete(0, tk.END)
            self.view.email_entry.insert(0, self._cliente.email)
            self.view.cpf_entry.delete(0, tk.END)
            self.view.cpf_entry.insert(0, self._cliente.cpf.replace(".", "").replace("-", ""))
        except Exception as exception:
            self.view.messagebox.showerror("Erro", exception.args[0])
    
    def _limpar(self):
        self._cliente = None
        self.view.nome_entry.delete(0, tk.END)
        self.view.nome_entry.insert(0, "")
        self.view.sobrenome_entry.delete(0, tk.END)
        self.view.sobrenome_entry.insert(0, "")
        self.view.email_entry.delete(0, tk.END)
        self.view.email_entry.insert(0, "")
        self.view.cpf_entry.delete(0, tk.END)
        self.view.cpf_entry.insert(0, "")
    
    def _atualizar(self):
        try:
            ClienteService().atualizar(Cliente(
                self.view.nome_entry.get(),
                self.view.sobrenome_entry.get(),
                self.view.email_entry.get(),
                self.view.cpf_entry.get(),
                self._cliente.id
            ))
            self._listar()
        except Exception as exception:
            self.view.messagebox.showerror("Erro", exception.args[0])
    
    def _excluir(self):
        try:
            ClienteService().excluir(self._cliente.id)
            self._listar()
        except Exception as exception:
            self.view.messagebox.showerror("Erro", exception.args[0])
    
    def _fechar(self):
        self.view.window.destroy()