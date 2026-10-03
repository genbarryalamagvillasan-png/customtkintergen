import customtkinter as ctk
from PIL import Image
gen = ctk.CTk()
gen.title("CustomTkinter Test")
gen.geometry("1000x800")

img = Image.open("background.jpg")
bg_image = ctk.CTkImage(light_image=img, dark_image=img, size=(1000, 800))

bg_label = ctk.CTkLabel(gen, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

f1 = ctk.CTkFrame(gen, width=600,height=300,border_color="white",border_width=1, fg_color="green")
f1.place(relx=0.5,rely=0.5,anchor = "center")

loginlabel = ctk.CTkLabel(f1, text="Login into your account", text_color="white", font=("arial", 20, "bold"))
loginlabel.place(relx=0.3,rely=0.15,anchor = "center")

login = ctk.CTkEntry(f1, width=500,height=50, corner_radius=20,placeholder_text="Email", border_color="white",fg_color="green",placeholder_text_color="white")
login.place(relx=0.5,rely=0.35,anchor = "center")

password = ctk.CTkEntry(f1, width=500,height=50, corner_radius=20,placeholder_text="Password",border_color="white",fg_color="green", placeholder_text_color="white", show="*")
password.place(relx=0.5,rely=0.55,anchor = "center")

loginbutton = ctk.CTkButton(f1, width=500,height=50,text="Login", text_color="green", fg_color="white", corner_radius=20, cursor = "hand2")
loginbutton.place(relx=0.5,rely=0.75,anchor = "center")

dont = ctk.CTkLabel(f1, text="Don't have an account?", text_color="white", font=("arial", 10),width=False, height=False)
dont.place(relx=0.2,rely=0.9,anchor = "center")

register = ctk.CTkLabel(f1, text="Register here", text_color="white",font=("arial", 10, "underline", "bold"), width=False, height=False, cursor="hand2")
register.place(relx=0.353,rely=0.9,anchor = "center")

gen.mainloop()