from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        wifi_name = request.form["wifi_name"]
        wifi_password = request.form["wifi_password"]
        security = request.form["security"]

        wifi_data = (
            f"WIFI:T:{security};"
            f"S:{wifi_name};"
            f"P:{wifi_password};;"
        )

        qr = qrcode.make(wifi_data)

        filename = "wifi_qrcode.png"

        filepath = os.path.join(
            "static",
            "generated",
            filename
        )

        qr.save(filepath)

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