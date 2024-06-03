import qrcode
import image
import qrcode.constants
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_sixe = 20, border =4)
qr.add_data('youtube.com')
qr.make(fit=True)
img = qr.make_image(fill_color = 'white', back_color = 'black')
img.save('Youtube.png')