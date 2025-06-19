import tkinter as tk
from tkinter import messagebox

tarefas = []

def adicionar_tarefa():
    new_entrada = entrada.get()
    if new_entrada:
        tarefas.append(new_entrada)
        atualizar_lista()
        entrada.delete(0, tk.END)
        messagebox.showinfo("", "Tarefa Adicionada")
    else:
        messagebox.showwarning("", "Digite uma tarefa antes de adicionar.")

def remover_tarefa():
    selecionado = show_tarefa.curselection()
    if selecionado:
        index = selecionado[0]
        del tarefas[index]
        atualizar_lista()
        messagebox.showinfo("", "Tarefa Removida")
    else:
        messagebox.showwarning("", "Selecione uma tarefa para remover.")

def atualizar_lista():
    show_tarefa.delete(0, tk.END)
    for i, tarefa in enumerate(tarefas, start=1):
        show_tarefa.insert(tk.END, f"{i}. {tarefa}")

# Janela principal
root = tk.Tk()
root.title("Tarefa Facil")
root.geometry("400x500")
root.config(bg="#121212")  # Fundo escuro
root.resizable(False, False)

# Título
titulo = tk.Label(root, text="Tarefa Certa", font=("Helvetica", 18, "bold"), bg="#121212", fg="#e0e0e0")
titulo.pack(pady=30)

# Entrada
entrada = tk.Entry(root, width=30, font=("Helvetica", 12), bg="#1e1e1e", fg="#e0e0e0", bd=2, relief="solid", justify="center", insertbackground="#e0e0e0")
entrada.pack(pady=10, ipady=6)

# Botões
frame_botoes = tk.Frame(root, bg="#121212")
frame_botoes.pack(pady=10)

botao_adicionar = tk.Button(frame_botoes, text="Adicionar", width=12, bg="#388e3c", fg="white",
                           font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5, bd=0,
                           activebackground="#2e7d32", activeforeground="white", command=adicionar_tarefa)
botao_adicionar.grid(row=0, column=0, padx=5)

botao_remover = tk.Button(frame_botoes, text="Remover", width=12, bg="#d32f2f", fg="white",
                          font=("Helvetica", 12, "bold"), relief="flat", padx=10, pady=5, bd=0,
                          activebackground="#b71c1c", activeforeground="white", command=remover_tarefa)
botao_remover.grid(row=0, column=1, padx=5)

# Lista de tarefas com barra de rolagem
frame_lista = tk.Frame(root, bg="#121212")
frame_lista.pack(pady=20)

scrollbar = tk.Scrollbar(frame_lista, bg="#121212", troughcolor="#2c2c2c", activebackground="#555555")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

show_tarefa = tk.Listbox(frame_lista, width=30, height=20, font=("Helvetica", 11), bg="#1e1e1e", fg="#e0e0e0",
                         yscrollcommand=scrollbar.set, bd=1, relief="solid", selectmode=tk.SINGLE,
                         selectbackground="#388e3c", selectforeground="white")
show_tarefa.pack(side=tk.LEFT)
scrollbar.config(command=show_tarefa.yview)

root.mainloop()
