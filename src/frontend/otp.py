import datetime
import sys, os.path
be_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/backend/')
sys.path.append(be_dir)
from be_otp import otp
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, filedialog, messagebox
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def openVigenere():
    from vigenere import Vigenere
    Vigenere(window)

def openExtended():
    from extended import Extended
    Extended(window)

def openPlayfair():
    from playfair import Playfair
    Playfair(window)

class OnetimePad():
    def __init__(self, screen):
        self.screen = screen
        global window
        screen.destroy()

        window = Tk()

        window.title("One-time Pad Cipher")
        window.geometry("900x600")
        window.configure(bg = "#E8DFCA")


        canvas = Canvas(
            window,
            bg = "#E8DFCA",
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        # judul
        canvas.place(x = 0, y = 0)
        image_image_title = PhotoImage(
            file=relative_to_assets("title.png"))
        image_title = canvas.create_image(
            97.0,
            97.0,
            image=image_image_title
        )

        # tombol vigenere
        button_image_vigenere = PhotoImage(
            file=relative_to_assets("vigenere.png"))
        button_vigenere = Button(
            image=button_image_vigenere,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: openVigenere(),
            relief="flat"
        )
        # posisi tombol vigenere
        button_vigenere.place(
            x=22.0,
            y=190.0,
            width=150.0,
            height=40.0
        )

        # tombol extended vigenere
        button_image_extended = PhotoImage(
            file=relative_to_assets("extended.png"))
        button_extended = Button(
            image=button_image_extended,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: openExtended(),
            relief="flat"
        )
        # posisi tombol extended vigenere
        button_extended.place(
            x=22.0,
            y=269.0,
            width=150.0,
            height=40.0
        )

        # tombol playfair
        button_image_playfair = PhotoImage(
            file=relative_to_assets("playfair.png"))
        button_playfair = Button(
            image=button_image_playfair,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: openPlayfair(),
            relief="flat"
        )
        # posisi tombol playfair
        button_playfair.place(
            x=22.0,
            y=348.0,
            width=150.0,
            height=40.0
        )

        # tombol otp
        button_image_otp_on = PhotoImage(
            file=relative_to_assets("otp_on.png"))
        button_otp_on = Button(
            image=button_image_otp_on,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("otp_on clicked"),
            relief="flat"
        )
        # posisi tombol otp
        button_otp_on.place(
            x=22.0,
            y=427.0,
            width=150.0,
            height=40.0
        )

        # line
        canvas.create_rectangle(
            194.0,
            0.0,
            199.0,
            600.0,
            fill="#7895B2",
            outline="")

        # input label
        canvas.create_text(
            221.0,
            27.0,
            anchor="nw",
            text="Input : ",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        def select_plain_file():
            file_path = filedialog.askopenfilename(initialdir = Path(__file__),
                                                filetypes = (("Text files", "*.txt"),))
            with open(file_path, "r") as file:
                plain_text = file.read()
            entry_input.delete("1.0", tk.END)
            entry_input.insert("1.0", plain_text)

        # tombol choose file untuk input (bisa plaintext atau ciphertext)
        button_image_import = PhotoImage(
            file=relative_to_assets("import.png"))
        button_import = Button(
            image=button_image_import,
            borderwidth=0,
            highlightthickness=0,
            command=select_plain_file,
            relief="flat"
        )
        # posisi tombol choose file untuk input
        button_import.place(
            x=221.0,
            y=50.0,
            width=657.0,
            height=30.0
        )

        # kolom input
        entry_image_input = PhotoImage(
            file=relative_to_assets("input.png"))
        entry_bg_input = canvas.create_image(
            549.5,
            121.5,
            image=entry_image_input
        )
        # format input
        entry_input = Text(
            bd=0,
            bg="#F5EFE6",
            fg="#000716",
            font=("Poppins Regular", 15 * -1),
            highlightthickness=0
        )
        # posisi kolom input
        entry_input.place(
            x=221.0,
            y=85.0,
            width=657.0,
            height=71.0
        )

        # key label
        canvas.create_text(
            221.0,
            178.0,
            anchor="nw",
            text="Key :",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        def generate_key():
            o = otp()
            o.generate_key()
            entry_key.delete("1.0", tk.END)
            entry_key.insert("1.0", o.K)

        # tombol generate key (untuk enkripsi)
        button_image_generate = PhotoImage(
            file=relative_to_assets("generate_key.png"))
        button_generate = Button(
            image=button_image_generate,
            borderwidth=0,
            highlightthickness=0,
            command=generate_key,
            relief="flat"
        )
        # posisi tombol generate key
        button_generate.place(
            x=221.0,
            y=201.0,
            width=317.0,
            height=30.0
        )

        def choose_key():
            file_path = filedialog.askopenfilename(initialdir = Path(__file__),
                                                filetypes = (("Text files", "*.txt"),))
            with open(file_path, "r") as file:
                key = file.read()
            entry_key.delete("1.0", tk.END)
            entry_key.insert("1.0", key)

        # tombol choose key file untuk dekripsi
        button_image_import_key = PhotoImage(
            file=relative_to_assets("import_key.png"))
        button_import_key = Button(
            image=button_image_import_key,
            borderwidth=0,
            highlightthickness=0,
            command=choose_key,
            relief="flat"
        )
        # posisi tombol choose key file
        button_import_key.place(
            x=561.0,
            y=201.0,
            width=317.0,
            height=30.0
        )
        
        # kolom input key
        entry_image_key = PhotoImage(
            file=relative_to_assets("key.png"))
        entry_bg_key = canvas.create_image(
            549.5,
            271.5,
            image=entry_image_key
        )
        # format input key
        entry_key = Text(
            bd=0,
            bg="#F5EFE6",
            fg="#000716",
            font=("Poppins Regular", 15 * -1),
            highlightthickness=0
        )
        # posisi kolom key
        entry_key.place(
            x=221.0,
            y=236.0,
            width=657.0,
            height=71.0
        )
        is_five_letter_formatted = tk.IntVar()
        # checkbutton untuk menggunakan spasi atau tidak
        check = Checkbutton(
                window,
                anchor = "nw",
                bg = "#E8DFCA",
                text = "add a space after 5 letters",
                font=("Poppins Regular", 15 * -1),
                variable=is_five_letter_formatted
        )
        # posisi checkbutton
        check.pack()
        check.place(
            x = 222.0,
            y = 324.0
        )

        def encrypt():
            # plain teks
            plain_teks = entry_input.get('1.0', 'end')
            key = entry_key.get('1.0', 'end')
            if key == '\n':
                tk.messagebox.showwarning(message="Keynya jangan kosong, hadeh")
                return
            o = otp(M=plain_teks, K=key)
            o.encrypt()
            entry_output.delete("1.0", tk.END)
            if is_five_letter_formatted.get():
                o.five_letter_format()
            entry_output.insert("1.0", o.C)

        # posisi tombol encrypt
        button_image_encrypt = PhotoImage(
            file=relative_to_assets("encrypt.png"))
        button_encrypt = Button(
            image=button_image_encrypt,
            borderwidth=0,
            highlightthickness=0,
            command=encrypt,
            relief="flat"
        )
        # posisi tombol encrypt
        button_encrypt.place(
            x=221.0,
            y=359.0,
            width=317.0,
            height=40.0
        )


        def decrypt():
            # plain teks
            cipher_teks = entry_input.get('1.0', 'end')
            key = entry_key.get('1.0', 'end')
            if key == '\n':
                tk.messagebox.showwarning(message="Keynya jangan kosong, hadeh")
                return
            o = otp(C=cipher_teks, K=key)
            o.decrypt()
            entry_output.delete("1.0", tk.END)
            entry_output.insert("1.0", o.M)

        # tombol decrypt
        button_image_decrypt = PhotoImage(
            file=relative_to_assets("decrypt.png"))
        button_decrypt = Button(
            image=button_image_decrypt,
            borderwidth=0,
            highlightthickness=0,
            command=decrypt,
            relief="flat"
        )
        # posisi tombol decrypt
        button_decrypt.place(
            x=561.0,
            y=359.0,
            width=317.0,
            height=40.0
        )

        # output label
        canvas.create_text(
            221.0,
            419.0,
            anchor="nw",
            text="Ouput : ",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        # kolom output
        '''canvas.create_rectangle(
            221.0,
            442.0,
            878.0,
            515.0,
            fill="#F5EFE6",
            outline="")'''
        
        # kolom output
        entry_image_output = PhotoImage(
            file=relative_to_assets("output.png"))
        entry_bg_output = canvas.create_image(
            549.5,
            121.5,
            image=entry_image_output
        )
        # format output
        entry_output = Text(
            bd=0,
            bg="#F5EFE6",
            fg="#000716",
            font=("Poppins Regular", 15 * -1),
            highlightthickness=0
        )
        # posisi kolom output
        entry_output.place(
            x=221.0,
            y=442.0,
            width=657.0,
            height=71.0
        )

        def save_file():
            file_content = entry_output.get('1.0', 'end')
            filename = "otp-" + datetime.datetime.now().strftime("%H%M%S-%Y%m%d") + ".txt"
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/file/' + filename, "w") as file:
                file.write(file_content)

        # tombol save dari output
        button_image_save = PhotoImage(
            file=relative_to_assets("save.png"))
        button_save = Button(
            image=button_image_save,
            borderwidth=0,
            highlightthickness=0,
            command=save_file,
            relief="flat"
        )
        # posisi tombol save
        button_save.place(
            x=221.0,
            y=520.0,
            width=657.0,
            height=30.0
        )

        # message save
        canvas.create_text(
            222.0,
            550.0,
            anchor="nw",
            text="*please check src/file/ to see the saved file!",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )
        
        # message save
        canvas.create_text(
            228.0,
            570.0,
            anchor="nw",
            text="format file name : otp-hms-ymd.txt",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        window.resizable(False, False)
        window.mainloop()
