import customtkinter as ctk

janela = ctk.CTk()
janela._set_appearance_mode("dark")

#Configurando a jenela principal
janela.title("App test")
janela.geometry("700x400") #Dimensão da janela
janela.maxsize(width=800, height=500)
janela.minsize(width=600, height=400)
#janela tamanho fixo
janela.resizable(width=True, height=False) #bloqueia com FALSE o tamanho da tela

#Fecha a aplicação
#janela.iconify()
#
#
#Recuperar a tela
#janela.deiconify()


janela.mainloop()