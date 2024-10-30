from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from pytube import YouTube

def baixar_video():
    url = url_entry.get().strip()
    
    # Validação de URL básica
    if not url.startswith("https://www.youtube.com/watch"):
        messagebox.showwarning("Erro", "Por favor, insira uma URL válida do YouTube.")
        return
    
    if not url:
        messagebox.showwarning("Erro", "Por favor, insira a URL do vídeo.")
        return
    
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        
        video.download()
        messagebox.showinfo("Sucesso", f"Vídeo '{yt.title}' baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível baixar o vídeo.\nErro: {str(e)}")

app = Tk()
app.title("Downloader de Vídeos do YouTube")
app.geometry("400x200")
app.resizable(False, False)

url_var = StringVar()
Label(app, text="Insira a URL do vídeo do YouTube:", font=("Arial", 12)).pack(pady=10)
url_entry = Entry(app, textvariable=url_var, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

Button(app, text="Baixar Vídeo", command=baixar_video, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=20)

app.mainloop()
