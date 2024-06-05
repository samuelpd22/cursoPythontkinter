import customtkinter as ctk

janela = ctk.CTk()



#Configurando a jenela principal
janela.title("App test")
janela.geometry("700x400") #Dimensão da janela
janela.maxsize(width=800, height=500)
janela.minsize(width=600, height=400)
#janela tamanho fixo
janela.resizable(width=True, height=False) #bloqueia com FALSE o tamanho da tela

#Aula 08 - Caixas de dialogo (dialog)
def abrirDialog():
    dialog = ctk.CTkInputDialog(title="Dialog",text="Digite seu celular")
    print(dialog.get_input())

btn = ctk.CTkButton(master=janela, text="Abrir dialogo" ,command=abrirDialog)
btn.pack()

janela.mainloop()