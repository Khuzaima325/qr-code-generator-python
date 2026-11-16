# QR Code Generator (Python)

Generate QR codes from the command line — for URLs, plain text, Wi-Fi
passwords, anything. Outputs a PNG image.

## Features

- Encode any text or URL
- Custom output file, size, border and colors
- Medium error correction, so codes still scan if slightly damaged

## How to run

```bash
pip install -r requirements.txt
python qr_gen.py "https://example.com"
python qr_gen.py "Hello, world!" --output hello.png --size 12
python qr_gen.py "https://github.com/Khuzaima325" --dark "#0f172a"
```

Built by @khuzaima.tech
