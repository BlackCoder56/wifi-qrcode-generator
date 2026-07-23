# Wi-Fi QR Code Generator

A simple Flask web application that generates QR codes for Wi-Fi networks.

Users can enter their Wi-Fi network details and generate a QR code that can be scanned by a smartphone to connect to the network without manually entering the password.

The generated QR code can also include a logo placed in the center.

## Features

* Generate Wi-Fi QR codes
* Enter Wi-Fi network name (SSID)
* Enter Wi-Fi password
* Select Wi-Fi security type
* Support for:

  * WPA / WPA2 / WPA3
  * WEP
  * No Password
* Add a logo to the center of the QR code
* High QR code error correction for better reliability with logos
* View the generated QR code in a result page
* Download the generated QR code as a PNG image
* Print the QR code using the browser's print dialog
* A4-friendly QR code poster design
* Responsive interface using Tailwind CSS

## Technologies Used

* Python
* Flask
* qrcode
* Pillow
* HTML
* Tailwind CSS

## Project Structure

```text
wifi-qrcode-generator/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    │
    ├── generated/
    │   └── wifi_qrcode.png
    │
    └── uploads/
        └── wifi.png
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/BlackCoder56/wifi-qrcode-generator.git

Navigate into the project:

```bash
cd wifi-qrcode-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask qrcode[pil] pillow
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

The application collects three pieces of information:

1. Wi-Fi network name
2. Wi-Fi password
3. Security type

The information is converted into the standard Wi-Fi QR code format:

```text
WIFI:T:WPA;S:MyWiFi;P:MyPassword;;
```

The application then generates a QR code using the `qrcode` Python library.

A logo is placed in the center of the QR code using Pillow.

The QR code uses high error correction:

```python
error_correction=qrcode.constants.ERROR_CORRECT_H
```

This helps the QR code remain readable even after placing a logo over part of the code.

## Logo

The current version uses a logo stored at:

```text
static/uploads/wifi.png
```

The logo is resized and placed in the center of the QR code.

For best results, use a PNG image with a transparent background.

## Printing

The result page includes a **Print A4** button.

When clicked, the browser's print dialog opens:

```javascript
window.print()
```

The user can then:

* Select an available printer
* Print the Wi-Fi poster
* Save the poster as a PDF

The printed design is formatted for A4 paper.

## Downloading

The generated QR code can also be downloaded directly as:

```text
wifi_qrcode.png
```

## Future Improvements

Planned improvements include:

* Allow users to upload their own logo
* Automatically remove white backgrounds from uploaded logos
* Add logo preview before generating
* Allow users to customize QR code colors
* Add different A4 poster templates
* Add a custom Wi-Fi poster title
* Add a business or organization name
* Add a custom footer
* Add QR code size controls
* Add downloadable A4 PDF generation
* Improve mobile responsiveness
* Add QR code validation
* Deploy the application to a server

## License

This project is open-source and available under the MIT License.