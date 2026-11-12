#!/usr/bin/env python3
"""
Server & Terminal QR Code Launcher
Serves the current folder over HTTP and prints a scannable QR code in the terminal
so mobile phones, iPads, and other devices on the same Wi-Fi can open it instantly.
"""

import sys
import os
import socket
import http.server
import socketserver
import subprocess

DEFAULT_PORT = 8080

def get_lan_ip():
    """Detect local network IP address."""
    # Method 1: route socket check (does not send packets outside)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        if ip and not ip.startswith("127."):
            return ip
    except Exception:
        pass

    # Method 2: macOS ipconfig getifaddr en0/en1
    for iface in ["en0", "en1", "wlan0", "eth0"]:
        try:
            res = subprocess.check_output(["ipconfig", "getifaddr", iface], text=True, stderr=subprocess.DEVNULL).strip()
            if res:
                return res
        except Exception:
            pass

    return "127.0.0.1"

def find_available_port(start_port=8080):
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', port))
                return port
            except OSError:
                continue
    return start_port

def print_qr_code(url):
    """Generate and display scannable ASCII QR code in the terminal."""
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=1,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        print("\n" + "=" * 54)
        print("  📱 SCAN THIS QR CODE WITH YOUR PHONE OR IPAD CAMERA")
        print("=" * 54 + "\n")
        qr.print_ascii(invert=True)
        print("\n" + "=" * 54)
    except Exception as e:
        print(f"Note: Could not render terminal QR code: {e}")

def main():
    # Make sure we serve from the project root
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(workspace_dir)

    # Optional port argument
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass

    port = find_available_port(port)
    lan_ip = get_lan_ip()
    local_url = f"http://localhost:{port}/"
    mobile_url = f"http://{lan_ip}:{port}/"
    guide_url = f"http://{lan_ip}:{port}/digital/reading-order.html"

    # Display Terminal Banner & QR Code
    print_qr_code(mobile_url)
    print(f"\n🚀 Server running in: {workspace_dir}")
    print(f"💻 On this Mac/PC:          {local_url}")
    print(f"📱 On Mobile/iPad (Wi-Fi):   {mobile_url}")
    print(f"📖 Direct Reading Guide:    {guide_url}")
    print("\nPress Ctrl+C to stop the server anytime.\n")

    handler = http.server.SimpleHTTPRequestHandler
    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped gracefully.")

if __name__ == "__main__":
    main()
