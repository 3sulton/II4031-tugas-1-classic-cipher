
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton


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

def openOnetimePad():
    from otp import OnetimePad
    OnetimePad(window)

class Enigma():
    def __init__(self, screen):
        self.screen = screen
        global window
        screen.destroy()

        window = Tk()

        window.title("Enigma Cipher")
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
            87.0,
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
            y=174.0,
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
            y=249.0,
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
            y=324.0,
            width=150.0,
            height=40.0
        )

        # tombol otp
        button_image_otp = PhotoImage(
            file=relative_to_assets("otp.png"))
        button_otp = Button(
            image=button_image_otp,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: openOnetimePad(),
            relief="flat"
        )
        # posisi tombol otp
        button_otp.place(
            x=22.0,
            y=399.0,
            width=150.0,
            height=40.0
        )

        # tombol engima
        button_image_enigma_on = PhotoImage(
            file=relative_to_assets("enigma_on.png"))
        button_enigma_on = Button(
            image=button_image_enigma_on,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("enigma_on clicked"),
            relief="flat"
        )
        # posisi tombol enigma
        button_enigma_on.place(
            x=22.0,
            y=475.0,
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

        # tombol choose file untuk input (bisa plaintext bisa ciphertext)
        button_image_import = PhotoImage(
            file=relative_to_assets("import.png"))
        button_import = Button(
            image=button_image_import,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("import clicked"),
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
            text="Rotor Key :",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        # slow key label
        canvas.create_text(
            221.0,
            206.0,
            anchor="nw",
            text="Slow :",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        # kolom input slow key
        entry_image_slow = PhotoImage(
            file=relative_to_assets("entry_slow.png"))
        entry_bg_slow = canvas.create_image(
            327.0,
            244.0,
            image=entry_image_slow
        )
        # format input slow key
        entry_slow = Text(
            bd=0,
            bg="#F5EFE6",
            fg="#000716",
            font=("Poppins Regular", 15 * -1),
            highlightthickness=0
        )
        # posisi input slow key
        entry_slow.place(
            x=221.0,
            y=229.0,
            width=212.0,
            height=28.0
        )

        # medium key label
        canvas.create_text(
            444.0,
            206.0,
            anchor="nw",
            text="Medium : ",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        # kolom input medium key
        entry_image_medium = PhotoImage(
            file=relative_to_assets("entry_medium.png"))
        entry_bg_medium = canvas.create_image(
            550.0,
            244.0,
            image=entry_image_medium
        )
        # format input medium key
        entry_medium = Text(
            bd=0,
            bg="#F5EFE6",
            fg="#000716",
            font=("Poppins Regular", 15 * -1),
            highlightthickness=0
        )
        # posisi kolom input medium key
        entry_medium.place(
            x=444.0,
            y=229.0,
            width=212.0,
            height=28.0
        )

        # fast key label
        canvas.create_text(
            666.0,
            206.0,
            anchor="nw",
            text="Fast : ",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        # kolom input fast key
        entry_image_fast = PhotoImage(
            file=relative_to_assets("entry_fast.png"))
        entry_bg_fast = canvas.create_image(
            772.0,
            244.0,
            image=entry_image_fast
        )
        # format input fast key
        entry_fast = Text(
            bd=0,
            bg="#F5EFE6",
            fg="#000716",
            font=("Poppins Regular", 15 * -1),
            highlightthickness=0
        )
        # posisi kolom input fast key
        entry_fast.place(
            x=666.0,
            y=229.0,
            width=212.0,
            height=28.0
        )

        # checkbutton untuk menggunakan spasi atau tidak
        check = Checkbutton(
                window,
                anchor = "nw",
                bg = "#E8DFCA",
                text = "add a space after 5 letters",
                font = ("Poppins Regular", 15 * -1)
        )
        # posisi checkbox
        check.pack()
        check.place(
            x = 222.0,
            y = 285.0
        )

        # tombol encrypt
        button_image_encrypt = PhotoImage(
            file=relative_to_assets("encrypt.png"))
        button_encrypt = Button(
            image=button_image_encrypt,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("encrypt clicked"),
            relief="flat"
        )
        # posisi tombol encrypt
        button_encrypt.place(
            x=221.0,
            y=324.0,
            width=317.0,
            height=40.0
        )

        # tombol decrypt
        button_image_decrypt = PhotoImage(
            file=relative_to_assets("decrypt.png"))
        button_decrypt = Button(
            image=button_image_decrypt,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("decrypt clicked"),
            relief="flat"
        )
        # posisi tombol decrypt
        button_decrypt.place(
            x=561.0,
            y=324.0,
            width=317.0,
            height=40.0
        )

        # output label
        canvas.create_text(
            221.0,
            384.0,
            anchor="nw",
            text="Ouput : ",
            fill="#000000",
            font=("Poppins Regular", 15 * -1)
        )

        # kolom output
        '''canvas.create_rectangle(
            221.0,
            407.0,
            878.0,
            480.0,
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
            y=407.0,
            width=657.0,
            height=71.0
        )

        # tombol save file dari output
        button_image_save = PhotoImage(
            file=relative_to_assets("save.png"))
        button_save = Button(
            image=button_image_save,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("save clicked"),
            relief="flat"
        )
        # posisi tombol save file
        button_save.place(
            x=221.0,
            y=485.0,
            width=657.0,
            height=30.0
        )
        
        window.resizable(False, False)
        window.mainloop()
