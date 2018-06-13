from mainWindow import *
from PIL import ImageTk
from PIL import Image
from io import BytesIO

def a_find_itemKey():
    global itemName
    

def a_init_image():
    global auctionWindow, itemImage, itemImageLabel
    itemID = "c6a38ab8c7540cfc51ea2b0b8b610fa7"
    url = "https://img-api.neople.co.kr/df/items/" + itemID

    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((56, 56), Image.ANTIALIAS)
    itemImage = ImageTk.PhotoImage(im)
    itemImageLabel = Label(auctionWindow, image = itemImage, width= 56, height= 56)
    itemImageLabel.place(x=20 + 100 - 28, y=20 + 80 - 25 - 28)
    itemImageLabel.pack_propagate(0)

def a_init_frame():
    global auctionWindow, itemFrame, auctionFrame
    itemFrame = LabelFrame(auctionWindow, text="아이템", width= 200, height= 250)
    auctionFrame = LabelFrame(auctionWindow, text="경매장", width= 340, height= 360)
    itemFrame.place(x=20, y=130)
    auctionFrame.place(x=240, y=20)
    itemFrame.pack_propagate(0)
    auctionFrame.pack_propagate(0)

def a_init_Window(input_itemName):
    global auctionWindow,itemName
    itemName = input_itemName
    auctionWindow = Tk()
    auctionWindow.geometry("600x400")
    a_init_image()

    a_init_frame()



a_init_Window()
auctionWindow.mainloop()