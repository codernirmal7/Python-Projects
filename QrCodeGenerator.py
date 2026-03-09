import qrcode
import qrcode.constants


# For simple qr code 
# img = qrcode.make("nirmal bam")
# img.save("name.png")

# For more control, use the QRCode class. 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data("Nirmal bam")
qr.make(fit=True)

img = qr.make_image(fill_color = "blue" , bacl_color = "white")
img.save("name.png")
