import customtkinter as ctk

janela = ctk.CTk()


#Configurando a jenela principal
janela.title("App test")
janela.geometry("700x400") #Dimensão da janela
janela.maxsize(width=800, height=500)
janela.minsize(width=600, height=400)
#janela tamanho fixo
janela.resizable(width=True, height=False) #bloqueia com FALSE o tamanho da tela




#Configurando tema
janela._set_appearance_mode("light")


#Criando nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry("500x250")

btn = ctk.CTkButton(master=janela,text="Abrir nova tela",command=nova_tela).place(x=300,y=100)


janela.mainloop()