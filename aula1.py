import customtkinter as ctk

janela = ctk.CTk()

janela._set_appearance_mode("dark")

btn = ctk.CTkButton(janela,text="Botão", bg_color="blue")
btn.pack()

janela.mainloop()