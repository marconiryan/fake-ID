import requests
from tkinter import Tk, Button, Label, Frame
from PIL import ImageTk, Image
from io import BytesIO


class Interface:
    def __init__(self, root):
        self.root = root
        self.frame_photo = Frame(root, bg="#1C1C1C")
        self.frame_photo.grid(column=1)
        self.photo = Label(self.frame_photo, width=130, height=130, bg="#000000")
        self.name = Label(self.frame_photo, font=("Arial", 14), anchor="s", bg="#1C1C1C", fg="#F0FFFF")
        self.email = Label(root, text="Email: ", justify="left", bg="#1C1C1C", fg="#F0FFFF")
        self.usuario = Label(root, text="Username: ", justify="left", bg="#1C1C1C", fg="#F0FFFF")
        self.senha = Label(root, text="Password: ", justify="left", bg="#1C1C1C", fg="#F0FFFF")
        Label(self.frame_photo, bg="#1C1C1C").grid(row=0)
        self.photo.grid(row=1)
        self.name.grid(row=2)
        self.email.grid(row=3, column=1)
        self.usuario.grid(row=4, column=1)
        self.senha.grid(row=5, column=1)
        Label(bg="#1C1C1C").grid(row=7)
        Button(root, text="GERAR", command=self.button, relief="solid", bg="#1C1C1C", fg="#F0F8FF").grid(row=8,
                                                                                                         column=1)
        Label(bg="#1C1C1C").grid(row=9)
        self.button()

    def get_login(self, dados):
        self.email["text"] = "Email: " + dados["email"] + " "
        self.usuario["text"] = "Username: " + dados["usuario"]
        self.senha["text"] = "Password: " + dados["senha"]

    def get_name(self, dados):
        self.name["text"] = f"{dados['nome']} {dados['sobrenome']}"

    def button(self):
        dados = self.get_random_user()
        self.get_photo(dados)
        self.get_name(dados)
        self.get_login(dados)

    def get_photo(self, dados):
        image_url = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(dados["foto"]).content)))
        self.photo["image"] = image_url
        self.photo.image = image_url

    @staticmethod
    def get_random_user():
        r = requests.get("https://randomuser.me/api/")
        resultados = r.json()['results']
        dados = {}
        for i in resultados:
            dados.update(i)

        return {"nome": dados["name"]["first"], "sobrenome": dados["name"]["last"],
                "email": dados["email"], "usuario": dados["login"]["username"],
                "senha": dados["login"]["password"], "foto": dados["picture"]["large"]}


app = Tk()
interface = Interface(app)
app.config(bg="#1C1C1C")
app.resizable(False, False)
app.title("Fake-P")
app.mainloop()
