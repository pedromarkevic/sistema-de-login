import customtkinter as ctk
import json
import os
import hashlib

# ================================
# FUNÇÕES DE ARQUIVO
# ================================
def carregar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

# ================================
# CONFIGURAÇÕES DA JANELA
# ================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Sistema de Login")
janela.geometry("400x400")

usuarios = carregar_usuarios()

# ================================
# FUNÇÕES DAS TELAS
# ================================
def mostrar_login():
    frame_cadastro.pack_forget()
    frame_login.pack(fill="both", expand=True)

def mostrar_cadastro():
    frame_login.pack_forget()
    frame_cadastro.pack(fill="both", expand=True)

def cadastrar():
    usuario = entrada_usuario_cadastro.get()
    senha = entrada_senha_cadastro.get()

    if usuario == "" or senha == "":
        label_msg_cadastro.configure(text="Preencha todos os campos!")
        return

    if usuario in usuarios:
        label_msg_cadastro.configure(text="Usuário já existe!")
        return

    usuarios[usuario] = criptografar_senha(senha)
    salvar_usuarios(usuarios)
    label_msg_cadastro.configure(text="")
    mostrar_login()

def login():
    usuario = entrada_usuario_login.get()
    senha = entrada_senha_login.get()

    if usuario == "" or senha == "":
        label_msg_login.configure(text="Preencha todos os campos!")
        return

    if usuario not in usuarios or usuarios[usuario] != criptografar_senha(senha):
        label_msg_login.configure(text="Usuário ou senha incorretos!")
        return

    label_msg_login.configure(text="")
    mostrar_principal()

def mostrar_principal():
    frame_login.pack_forget()
    frame_principal.pack(fill="both", expand=True)

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# ================================
# TELA DE LOGIN
# ================================
frame_login = ctk.CTkFrame(janela)
ctk.CTkLabel(frame_login, text="🔐 Login", font=("Arial", 22, "bold")).pack(pady=20)
ctk.CTkLabel(frame_login, text="Usuário:").pack()
entrada_usuario_login = ctk.CTkEntry(frame_login, width=200)
entrada_usuario_login.pack(pady=5)
ctk.CTkLabel(frame_login, text="Senha:").pack()
entrada_senha_login = ctk.CTkEntry(frame_login, width=200, show="*")
entrada_senha_login.pack(pady=5)
label_msg_login = ctk.CTkLabel(frame_login, text="", text_color="red")
label_msg_login.pack()
ctk.CTkButton(frame_login, text="Entrar", command=login).pack(pady=10)
ctk.CTkButton(frame_login, text="Criar conta", command=mostrar_cadastro).pack()

# ================================
# TELA DE CADASTRO
# ================================
frame_cadastro = ctk.CTkFrame(janela)
ctk.CTkLabel(frame_cadastro, text="📝 Cadastro", font=("Arial", 22, "bold")).pack(pady=20)
ctk.CTkLabel(frame_cadastro, text="Usuário:").pack()
entrada_usuario_cadastro = ctk.CTkEntry(frame_cadastro, width=200)
entrada_usuario_cadastro.pack(pady=5)
ctk.CTkLabel(frame_cadastro, text="Senha:").pack()
entrada_senha_cadastro = ctk.CTkEntry(frame_cadastro, width=200, show="*")
entrada_senha_cadastro.pack(pady=5)
label_msg_cadastro = ctk.CTkLabel(frame_cadastro, text="", text_color="red")
label_msg_cadastro.pack()
ctk.CTkButton(frame_cadastro, text="Cadastrar", command=cadastrar).pack(pady=10)
ctk.CTkButton(frame_cadastro, text="Já tenho conta", command=mostrar_login).pack()

# ================================
# TELA PRINCIPAL
# ================================
frame_principal = ctk.CTkFrame(janela)
ctk.CTkLabel(frame_principal, text="✅ Bem vindo!", font=("Arial", 22, "bold")).pack(pady=20)
ctk.CTkButton(frame_principal, text="Sair", command=mostrar_login).pack()

# ================================
# INICIAR
# ================================
mostrar_login()
janela.mainloop()