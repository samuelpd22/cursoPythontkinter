import customtkinter as ctk

janela = ctk.CTk()



#Configurando a jenela principal
janela.title("App test")
janela.geometry("700x400") #Dimensão da janela
janela.maxsize(width=800, height=500)
janela.minsize(width=600, height=400)
#janela tamanho fixo
janela.resizable(width=True, height=False) #bloqueia com FALSE o tamanho da tela

#Aula 07 Caixa de texto (textbox)
textlabel = ctk.CTkLabel(master=janela, text="Caixa de texto:")
textlabel.pack()

textbox = ctk.CTkTextbox(master=janela, width=300, height=350, scrollbar_button_color="teal", scrollbar_button_hover_color="black",border_width=2, border_color="teal", corner_radius=15 ,fg_color="transparent" ,border_spacing=20)
textbox.pack()

textbox.insert("0.0","Titulo do seu texto" + "Olá dev, estou aqui programando e aprendendo"*40)


janela.mainloop()