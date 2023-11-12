from tkinter import *


window=Tk()
window.minsize(width=300,height=400)
window.title('Caesar Cipher')
window.config(padx=10,pady=10)
x=''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# aksi untuk tombol
def zero():
    text.delete('1.0',END)
def d():
    tombol.config(text='Decoding')

def e():
    tombol.config(text='Encoding')

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        print('a')
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            print('b')
    print(cipher_direction)

    window2 = Toplevel()
    window2.minsize(width=300,height=400)
    result = Text(window2,height=20, width=50)
    result.insert(END,end_text)
    result.config(state='disabled')
    result.pack()







# dropdown
state_= StringVar()
encode = Radiobutton(text='Encode',value='encode',variable=state_,command=e)
decode = Radiobutton(text='Decode',value='decode',variable=state_,command=d)
encode.grid(column=0,row=0)
decode.grid(column=0,row=1)

# shift number
shift = Label(text="Type the shift number")
shift.grid(column=1,row=0)

spinbox = Spinbox(from_=0, to=100, width=5)
spinbox.grid(column=1,row=1)

# from pengisian
text = Text(height=20, width=50,bg='white')
text.grid(column=1,row=3)

# aksi tombol
def enter():
    start_text = text.get("0.0", END).lower()
    shift_amount = int(spinbox.get())
    cipher_direction = state_.get()
    caesar(start_text, shift_amount, cipher_direction)

tombol=Button(text='Decoding',command=enter,bg='red',fg='white')
tombol.grid(column=3,row=1,pady=(5,10))
reset=Button(text='Reset',command=zero,width=8)
reset.grid(column=3,row=0)
window.mainloop()