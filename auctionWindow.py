from mainWindow import *
from PIL import ImageTk
from PIL import Image
from io import BytesIO

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
    itemImage = ImageTk.PhotoImage(im)
    itemImageLabel = Label(auctionWindow, image = itemImage, width= 56, height= 56)
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
    info.insert(INSERT, "설명:  " + data["itemExplainDetail"] + " \n")
    info.insert(INSERT, "획득방법:  " + data["itemObtainInfo"] )

    info.configure(state="disabled")

def info_auction():
    global conn, server, apiKey, itemName, auctionFrame

    if conn == None:
        connectOpenAPIServer()

    encText = urllib.parse.quote(itemName)

    conn.request("GET", "/df/auction?itemName=" + encText + "&apikey=" + apiKey)
    req = conn.getresponse()
    response_body = req.read()
    decode_response_body = response_body.decode('utf-8')
    json_response_body = json.loads(decode_response_body)
    print(json_response_body)
    data = json_response_body["rows"]

    info = Text(auctionFrame, width=45)
    info.pack(side=LEFT)
    sc = Scrollbar(auctionFrame)
    sc.pack(side=RIGHT, fill=Y)
    sc.config(command=info.yview)
    info.config(yscrollcommand=sc.set)

    for i in data:
        info.insert(INSERT, "이름:  " + i["itemName"] + "\n")
        info.insert(INSERT, "수량:  " + str(i["count"]) + "\n")
        info.insert(INSERT, "즉시구매가:  " + str(i["currentPrice"]) + "\n")
        info.insert(INSERT, "개당즉시구매가:  " + str(i["unitPrice"]) + "\n")
        info.insert(INSERT, "현재입찰가:  ")
        if i["price"] is -1:
            info.insert(INSERT, "-" + "\n")
        else:
            info.insert(INSERT, str(i["price"]) + "\n")
        info.insert(INSERT, "평균가:  " + str(i["averagePrice"]) + "\n")
        info.insert(INSERT, "등록일:  " + i["regDate"] + "\n")
        info.insert(INSERT, "마감일:  " + i["expireDate"] + "\n")
        info.insert(INSERT, "-------------------------" + "\n")


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

    if a_find_itemKey() == True:
        auctionWindow = Tk()
        auctionWindow.geometry("600x400")
        a_init_image()

        a_init_frame()

        info_item()
        info_auction()
    else:
        a_init_falseWindow()




a_init_Window("마그토늄")

a_init_Window("magtonum")

auctionWindow.mainloop()