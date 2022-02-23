from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from  main import  LSBAudioStego


root = Tk()


# create window using from in Tkinter
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Audio Steganography")
        self.Enocoding()
        self.Decoding()



    def Enocoding(self):
        # encode Label
        self.encodeVar = StringVar()
        self.encodelabel = Label(root, textvariable=self.encodeVar, font=("Comic Sans MS", 30, "bold"))
        self.encodelabel.place(x=20, y=50)
        self.encodeVar.set("Encode")

        # creating a button instance
        self.selectFileButton = Button(root, text="Select File To Encode", command=self.selectFile)
        self.selectFileButton.place(x=20, y=140)

        # file location label
        self.var = StringVar()
        self.label = Label(root, textvariable=self.var)
        self.label.place(x=20, y=180)

        # entry box
        self.entryText = Entry(root)
        self.entryText.place(x=20, y=220)
        self.entryText.insert(0, "Enter text here")
        # encode Button
        self.encodeButton = Button(root, text="Encode", command=self.encode)
        self.encodeButton.place(x=20, y=260)

        # encoded  location label
        self.enocdedLocation = StringVar()
        self.locationOfEncodeFile = Label(root, textvariable=self.enocdedLocation)
        self.locationOfEncodeFile.place(x=20, y=300)

    def Decoding(self):
        # decode Label
        self.decodeVar = StringVar()
        self.decodelabel = Label(root, textvariable=self.decodeVar, font=("Comic Sans MS", 30, "bold"))
        self.decodelabel.place(x=500, y=50)
        self.decodeVar.set("Decode")


        # creating a button instance
        self.selectFileDecodeButton = Button(root, text="Select File To Decode ", command=self.selectFileDecode)
        self.selectFileDecodeButton.place(x=500, y=140)

        # file location label
        self.decodeFileVar = StringVar()
        self.decodeFileLabel = Label(root, textvariable=self.decodeFileVar)
        self.decodeFileLabel.place(x=500, y=180)

        self.decodeButton = Button(root, text="Decode", command=self.decode)
        self.decodeButton.place(x=500, y=260)

        # decoded text label
        self.decodedString = StringVar()
        self.decodedStringlabel = Label(root, textvariable=self.decodedString, font=('arial', 12))
        self.decodedStringlabel.place(x=500, y=220)


    def selectFile(self):
        # file selection
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.wav"), ("all files", "*.*")))
        self.fileSelected = root.filename
        self.var.set(root.filename)

    def selectFileDecode(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.wav"), ("all files", "*.*")))
        self.fileSelcetedForDecode = root.filename
        self.decodeFileVar.set(root.filename)

    def encode(self):
        # select algo to encode
        algo = LSBAudioStego()
        result = algo.encodeAudio(self.fileSelected, self.entryText.get())
        self.enocdedLocation.set(result)

    def decode(self):
        # select algo to decode
        algo = LSBAudioStego()
        result = algo.decodeAudio(self.fileSelcetedForDecode)
        self.decodedString.set(result)


# resolution
root.geometry("900x700")

#set background color
root.config(bg='#49A')

#add background image
bg = PhotoImage(file="C:\\Users\\Mega\\Downloads\\audiobgg.png")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# creation of an instance of window
app = Window(root)

# mainloop
root.mainloop()