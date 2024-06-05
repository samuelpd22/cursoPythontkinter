import customtkinter as ctk

janela = ctk.CTk()



#Configurando a jenela principal
janela.title("App test")
janela.geometry("700x400") #Dimensão da janela
janela.maxsize(width=800, height=500)
janela.minsize(width=600, height=400)
#janela tamanho fixo
janela.resizable(width=True, height=False) #bloqueia com FALSE o tamanho da tela

#Aula 06
tabviwer = ctk.CTkTabview(master=janela,width=400 ,border_color="teal", border_width=1, corner_radius=20, fg_color="teal", segmented_button_selected_color="teal", segmented_button_selected_hover_color="blue")
tabviwer.pack()

tabviwer.add("Nomes")
tabviwer.add("Idades")
tabviwer.add("Genero")
tabviwer.tab("Nomes").grid_columnconfigure(0,weight=1)
tabviwer.tab("Idades").grid_columnconfigure(0,weight=1)
tabviwer.tab("Genero").grid_columnconfigure(0,weight=1)

#Adicionando elementos nas TABVIWER
texto1 = ctk.CTkLabel(tabviwer.tab("Nomes"), text="Nome:")
texto1.pack()
entry1 = ctk.CTkEntry( tabviwer.tab("Nomes"), placeholder_text="Preencha com seu nome" )
entry1.pack()

texto2 = ctk.CTkLabel(tabviwer.tab("Idades"), text="Idade:")
texto2.pack()
entry2 = ctk.CTkEntry(tabviwer.tab("Idades"), placeholder_text="Idade")
entry2.pack()

texto3 = ctk.CTkLabel(tabviwer.tab("Genero"), text="Genero:")
texto3.pack()
entry3 = ctk.CTkComboBox(tabviwer.tab("Genero"),values= ["Masculino", "Feminino"])
entry3.pack()


janela.mainloop()