#!/usr/bin/env python3
"""qr-code-generator-python — generate QR codes from the command line.

Usage:
    python qr_gen.py "https://example.com"
    python qr_gen.py "Hello, world!" --output hello.png --size 12
    python qr_gen.py "WiFi password" --output wifi.png --dark "#0f172a"

Requires: qrcode[pil]  (pip install -r requirements.txt)
"""

import argparse
import sys
from pathlib import Path

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_M
except ImportError:
    print("Missing dependency: run  pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


def make_qr(text, output, box_size=10, border=4, dark="#000000", light="#ffffff"):
    qr = qrcode.QRCode(
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=dark, back_color=light)
    img.save(output)
    return output


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code image.")
    parser.add_argument("text", help="Text or URL to encode")
    parser.add_argument("--output", default="qrcode.png", help="Output file (default: qrcode.png)")
    parser.add_argument("--size", type=int, default=10, help="Pixels per QR module (default: 10)")
    parser.add_argument("--border", type=int, default=4, help="Quiet-zone width in modules (default: 4)")
    parser.add_argument("--dark", default="#000000", help="Foreground color (default: #000000)")
    parser.add_argument("--light", default="#ffffff", help="Background color (default: #ffffff)")
    args = parser.parse_args()

    if args.size < 1 or args.border < 0:
        print("Error: --size must be >= 1 and --border >= 0.", file=sys.stderr)
        sys.exit(1)
    out = Path(args.output)
    if out.suffix.lower() not in {".png", ".jpg", ".jpeg", ".bmp"}:
        print("Error: output must be a .png, .jpg or .bmp file.", file=sys.stderr)
        sys.exit(1)
    make_qr(args.text, out, box_size=args.size, border=args.border,
            dark=args.dark, light=args.light)
    print(f"Saved QR code to {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
