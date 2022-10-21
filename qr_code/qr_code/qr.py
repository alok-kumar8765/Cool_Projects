import qrcode
import image

qr = qrcode.QRCode(
    version=15, #15 mans the version of the qr code high the number bigger the image
    box_size=10, # size of the box where qr code displayed
    border=5,
)

data = "http://bionapp.herokuapp.com/"
# data2 = "http://bion-technology.com.sg/"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
