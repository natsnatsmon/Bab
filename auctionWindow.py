import http.client
import urllib.request
import json
from tkinter import *
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import tkinter.messagebox
from operator import itemgetter
import tkinter.scrolledtext as tkst

server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

def a_find_itemKey():
    global itemName, conn, server, apiKey, itemID

    if conn == None:
        connectOpenAPIServer()

    encText = urllib.parse.quote(itemName)
    conn.request("GET", "/df/items?itemName=" + encText +  "&apikey=" + apiKey)
    req = conn.getresponse()
    if int(req.status) != 200:
        return False
    response_body = req.read()
    decode_response_body = response_body.decode('utf-8')
    json_response_body = json.loads(decode_response_body)
    data = json_response_body["rows"]
    if not data:
        return False
    itemID  = data[0]["itemId"]
    return True

def a_init_falseWindow():
    global auctionWindow
    auctionWindow = Tk()
    auctionWindow.geometry("200x80")
    closeL = Label(text="해당 아이템을 찾을 수 없습니다",)
    closeL.place(x = 10, y = 18)
    closeB = Button(auctionWindow, text = "확인", command = auctionWindow.destroy)
    closeB.place(x = 80, y= 45)

def a_init_image():
    global auctionWindow, itemImage, itemImageLabel, itemID
    url = "https://img-api.neople.co.kr/df/items/" + itemID

    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((56, 56), Image.ANTIALIAS)
    itemImage = ImageTk.PhotoImage(im, master=auctionWindow)
    import gc
    gc.disable()
    itemImageLabel = Label(master=auctionWindow, image = itemImage, width= 56, height= 56)
    itemImageLabel.place(x=20 + 100 - 28, y=20 + 80 - 25 - 28)
    itemImageLabel.pack_propagate(0)

def info_item():
    global conn, server, apiKey, itemID, itemFrame

    if conn == None:
        connectOpenAPIServer()

    conn.request("GET", "/df/items/" + itemID + "?apikey=" + apiKey)
    req = conn.getresponse()
    response_body = req.read()
    decode_response_body = response_body.decode('utf-8')
    json_response_body = json.loads(decode_response_body)
    data = json_response_body

    info = Text(itemFrame,width= 25)
    info.pack(side=LEFT)
    sc = Scrollbar(itemFrame)
    sc.pack(side=RIGHT, fill=Y)
    sc.config(command=info.yview)
    info.config(yscrollcommand=sc.set)

    info.insert(INSERT, "이름:  " + data["itemName"] + " \n\n")
    info.insert(INSERT, "등급:  " + data["itemRarity"] + " \n\n")
    info.insert(INSERT, "등급:  " + data["itemType"] + " / " + data["itemTypeDetail"] + " \n\n")
    info.insert(INSERT, "착용레벨:  " + str(data["itemAvailableLevel"]) + " \n\n")
    info.insert(INSERT, "설명:\n  " + data["itemExplainDetail"] + " \n\n")
    info.insert(INSERT, "획득방법:\n" + data["itemObtainInfo"] )

    info.configure(state="disabled")

def auction_sort_byPrice():
    global ainfo, auctionFrame, adata
    adata = sorted(adata, key=itemgetter("unitPrice"))
    ainfo.delete('1.0', END)
    print_adata()

def auction_sort_byPrice_reverse():
    global ainfo, auctionFrame, adata
    adata = sorted(adata, key = itemgetter("unitPrice"), reverse=True)
    ainfo.delete('1.0', END)
    print_adata()

def auction_sort_byDate():
    global ainfo, auctionFrame, adata
    adata = sorted(adata, key=itemgetter("regDate"))
    ainfo.delete('1.0', END)
    print_adata()

def auction_sort_byDate_reverse():
    global ainfo, auctionFrame, adata
    adata = sorted(adata, key = itemgetter("regDate"), reverse=True)
    ainfo.delete('1.0', END)
    print_adata()

def print_adata():
    global adata
    for i in adata:
        ainfo.insert(INSERT, "이름:  " + i["itemName"] + "\n")
        ainfo.insert(INSERT, "수량:  " + str(i["count"]) + "\n")
        ainfo.insert(INSERT, "즉시구매가:  " + str(i["currentPrice"]) + "\n")
        ainfo.insert(INSERT, "개당즉시구매가:  " + str(i["unitPrice"]) + "\n")
        ainfo.insert(INSERT, "현재입찰가:  ")
        if i["price"] is -1:
            ainfo.insert(INSERT, "-" + "\n")
        else:
            ainfo.insert(INSERT, str(i["price"]) + "\n")
        ainfo.insert(INSERT, "평균가:  " + str(i["averagePrice"]) + "\n")
        ainfo.insert(INSERT, "등록일:  " + i["regDate"] + "\n")
        ainfo.insert(INSERT, "마감일:  " + i["expireDate"] + "\n")
        ainfo.insert(INSERT, "-------------------------" + "\n")

def refresh():
    global conn, server, apiKey, itemName, auctionFrame, ainfo, adata

    if conn == None:
        connectOpenAPIServer()

    encText = urllib.parse.quote(itemName)

    conn.request("GET", "/df/auction?itemName=" + encText + "&apikey=" + apiKey)
    req = conn.getresponse()
    response_body = req.read()
    decode_response_body = response_body.decode('utf-8')
    json_response_body = json.loads(decode_response_body)
    print(json_response_body)
    adata = json_response_body["rows"]

    ainfo.delete('1.0', END)
    print_adata()

def info_auction():
    global conn, server, apiKey, itemName, auctionFrame, ainfo, adata

    if conn == None:
        connectOpenAPIServer()

    encText = urllib.parse.quote(itemName)

    conn.request("GET", "/df/auction?itemName=" + encText + "&apikey=" + apiKey)
    req = conn.getresponse()
    response_body = req.read()
    decode_response_body = response_body.decode('utf-8')
    json_response_body = json.loads(decode_response_body)
    print(json_response_body)
    adata = json_response_body["rows"]

    ainfo = tkst.ScrolledText(auctionFrame, width=45, height = 20, wrap=WORD)
    ainfo.pack(side=BOTTOM, anchor="w")

    print_adata()

    from tkinter import font
    tmpFont = font.Font(auctionWindow, size=10, weight='bold', family='Consolas')
    b = Button(auctionFrame, text="가격별 오름차순", font=tmpFont, command=auction_sort_byPrice)
    b.place(x = 10, y= 10)
    b = Button(auctionFrame, text="가격별 내림차순", font=tmpFont, command=auction_sort_byPrice_reverse)
    b.place(x= 120, y=10)
    b = Button(auctionFrame, text="등록일 오름차순", font=tmpFont, command=auction_sort_byDate)
    b.place(x= 10, y=40)
    b = Button(auctionFrame, text="등록일 내림차순", font=tmpFont, command=auction_sort_byDate_reverse)
    b.place(x=120, y=40)

    b = Button(auctionFrame, text="새로\n고침", font=tmpFont, command=auction_sort_byDate_reverse, width= 5, height= 3)
    b.place(x=280, y=10)

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

    connectOpenAPIServer()

    if a_find_itemKey() == True:
        auctionWindow = Tk()
        auctionWindow.geometry("600x400")

        a_init_frame()

        info_item()
        info_auction()

        a_init_image()
    else:
        tkinter.messagebox.showerror("DnF in", "해당 아이템을 찾을 수 없습니다")