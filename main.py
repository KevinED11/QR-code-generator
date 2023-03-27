
"""
This module generates QR code 
"""
import pyqrcode

if __name__ == "__main__":
    link_qrcode: list[str] = ["https://www.twitch.tv/",
                              "https://www.python.org/"
                              ]

    for number, link in enumerate(link_qrcode):
        filename_svg = f"qrcode_{number + 1}_" + ".svg"
        filename_png = f"qrcode_{number + 1}_" + ".png"

        image_qrcode = pyqrcode.create(content=link)
        image_qrcode.svg(file=filename_svg, scale=8)
        image_qrcode.png(file=filename_png, scale=10)
