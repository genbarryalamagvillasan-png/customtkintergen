import customtkinter as ctk
from PIL import Image
gen = ctk.CTk()
gen.title("CustomTkinter Test")
gen.geometry("800x600")

def show_login(event):
    registerframe.place_forget()
    loginframe.place(relx=0.5, rely=0.5, anchor="center")

def show_register(event):
    loginframe.place_forget()
    registerframe.place(relx=0.5, rely=0.5, anchor="center")

img = Image.open("gen.jpg")
bg_image = ctk.CTkImage(light_image=img, dark_image=img, size=(800, 600))

bg_label = ctk.CTkLabel(gen, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

loginframe = ctk.CTkFrame(gen, width = 500, height = 400, border_color = 'red', border_width= 2, fg_color = "white")
loginframe.place(relx = 0.5, rely = 0.5, anchor = 'center')
loginframe.pack_propagate(False)

welcomeback = ctk.CTkLabel(loginframe, text = "Welcome Back!", font = ('Helvetica', 30, 'bold'))
welcomeback.pack(pady = (15, 0))

signin = ctk.CTkLabel(loginframe, text = "Sign in to continue", font = ('Helvetica', 12), text_color="gray")
signin.pack(pady = (0, 15))

username = ctk.CTkLabel(loginframe, text = "Username", font=('Helvetica', 14), anchor = "w", width = 350)
username.pack(pady = (5 , 0))

email = ctk.CTkEntry(loginframe, placeholder_text= "Email", placeholder_text_color="black", width= 350, height = 50, border_color="red")
email.pack(pady = (2, 0))

password1 = ctk.CTkLabel(loginframe, text = "Password", font=('Helvetica', 14), anchor = "w", width = 350)
password1.pack(pady = (5, 0))

password2 = ctk.CTkEntry(loginframe, placeholder_text= "Password", placeholder_text_color="black", width = 350, height = 50, border_color = "red", show = "*")
password2.pack(pady = (2, 0))

loginbutton = ctk.CTkButton(loginframe, text = "Login", width = 350, height = 50, fg_color= "red", cursor = "hand2")
loginbutton.pack(pady=(10, 0))

signupframe = ctk.CTkFrame(loginframe, fg_color='transparent', width = 350)
signupframe.pack(pady = 5)
signupframe.pack_propagate(False)

dont = ctk.CTkLabel(signupframe, text = "don't have an account?", font = ('helvetica', 10))
dont.pack(side = "left")

signup = ctk.CTkLabel(signupframe, text="Sign up", text_color="red", font = ('helvetica', 10, "underline", "bold"), cursor = "hand2")
signup.pack(side = "left", padx = (5,0))
signup.bind("<Button-1>", show_register)

#OOOOOOOOOOOOOOOOOOOPS
registerframe = ctk.CTkFrame(gen, width = 500, height = 400, border_color = 'red', border_width= 2, fg_color = "white")
registerframe.place(relx = 0.5, rely = 0.5, anchor = 'center')
registerframe.pack_propagate(False)

createaccount = ctk.CTkLabel(registerframe, text = "Create Account", font = ('Helvetica', 30, 'bold'))
createaccount.pack(pady = (15, 0))

signin = ctk.CTkLabel(registerframe, text = "Sign in to continue", font = ('Helvetica', 12), text_color="gray")
signin.pack(pady = (0, 15))

username = ctk.CTkLabel(registerframe, text = "Username", font=('Helvetica', 14), anchor = "w", width = 350)
username.pack(pady = (5 , 0))

email = ctk.CTkEntry(registerframe, placeholder_text= "Email", placeholder_text_color="black", width= 350, height = 50, border_color="red")
email.pack(pady = (2, 0))

password1 = ctk.CTkLabel(registerframe, text = "Password", font=('Helvetica', 14), anchor = "w", width = 350)
password1.pack(pady = (5, 0))

password2 = ctk.CTkEntry(registerframe, placeholder_text= "Password", placeholder_text_color="black", width = 350, height = 50, border_color = "red", show = "*")
password2.pack(pady = (2, 0))

registerbutton = ctk.CTkButton(registerframe, text = "Register", width = 350, height = 50, fg_color= "red", cursor = "hand2")
registerbutton.pack(pady=(10, 0))

ops = ctk.CTkFrame(registerframe, fg_color='transparent', width = 350)
ops.pack(pady = 5)
ops.pack_propagate(False)

already = ctk.CTkLabel(ops, text = "Already have an account?", font = ('helvetica', 10))
already.pack(side = "left")

signup = ctk.CTkLabel(ops, text="Login", text_color="red", font = ('helvetica', 10, "underline", "bold"), cursor = "hand2")
signup.pack(side = "left", padx = (5,0))
signup.bind("<Button-1>", show_login)


gen.mainloop()