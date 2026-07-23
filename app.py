from flask import Flask, render_template, request
import qrcode
from PIL import Image
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        wifi_name = request.form["wifi_name"]
        wifi_password = request.form["wifi_password"]
        security = request.form["security"]


        # Wi-Fi QR Code Data

        wifi_data = (
            f"WIFI:T:{security};"
            f"S:{wifi_name};"
            f"P:{wifi_password};;"
        )


        # Generate QR Code

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )

        qr.add_data(wifi_data)

        qr.make(fit=True)


        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        ).convert("RGB")


        # Open Logo

        logo_path = os.path.join(
            "static",
            "uploads",
            "wifi.png"
        )

        logo = Image.open(logo_path).convert("RGBA")


        # Resize Logo

        qr_width, qr_height = qr_image.size

        logo_size = qr_width // 5

        logo.thumbnail(
            (logo_size, logo_size),
            Image.Resampling.LANCZOS
        )


        # Calculate Center Position

        logo_width, logo_height = logo.size

        position = (
            (qr_width - logo_width) // 2,
            (qr_height - logo_height) // 2
        )


        # Add Logo Directly to QR Code

        qr_image.paste(
            logo,
            position,
            logo
        )


        # Save QR Code

        filename = "wifi_qrcode.png"

        filepath = os.path.join(
            "static",
            "generated",
            filename
        )

        qr_image.save(filepath)


        # Show Result Page

        return render_template(
            "result.html",
            wifi_name=wifi_name,
            wifi_password=wifi_password,
            security=security,
            qr_code=filename
        )


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
