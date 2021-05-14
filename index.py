import pyqrcode
import png
from pyqrcode import QRCode

#link para o qrcode
qrstring = ''

#monta o qrcode
url = pyqrcode.create(qrstring)

#salva o qrcode gerado no local desejado, nesse caso, na pasta do projeto
url.png(r'QRcode.png', scale=8)