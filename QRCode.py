#GENERATING QR CODE 
#importing qrcode module to generate QR Code
import qrcode 

#importing image module
import image

#for error correction levels, importing qrcode constants
import qrcode.constants

#creating qr object with parameter as version (control the size of the qrcode), error correction as high level, box size and border)
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_sixe = 20, border =4)

#adding link 
qr.add_data('youtube.com')
qr.make(fit=True)

#colour of the qrcode
img = qr.make_image(fill_color = 'white', back_color = 'black')

#saving image as png format in local pc
img.save('Youtube.png')
