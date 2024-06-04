import customtkinter as ctk

janela = ctk.CTk()


#Configurando a jenela principal
janela.title("App test")
janela.geometry("700x400") #Dimensão da janela
janela.maxsize(width=800, height=500)
janela.minsize(width=600, height=400)
#janela tamanho fixo
janela.resizable(width=True, height=False) #bloqueia com FALSE o tamanho da tela

#Aula 05 = frames
frame1 = ctk.CTkFrame(master= janela,width=200, height=330, fg_color="teal" , bg_color="transparent" ,corner_radius=30, border_width=10).place(x=10,y=60)

frame2 = ctk.CTkFrame(master= janela,width=200, height=330 , fg_color="green").place(x=230,y=60)

frame3 = ctk.CTkFrame(master= janela,width=200, height=330, fg_color="white").place(x=450,y=60)


janela.mainloop()