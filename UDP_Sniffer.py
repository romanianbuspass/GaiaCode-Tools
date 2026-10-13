"""
GaiaCode UDP Sniffer
====================
Listens for incoming UDP packets on port 5552 (or custom port).
Prints every packet with timestamp, source IP, and raw payload.
Useful for diagnosing Tau station broadcasts.

Usage:
    python UDP_Sniffer.py            (listens on port 5552)
    python UDP_Sniffer.py 9999       (listens on custom port)
"""

import socket
import sys
import datetime

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5552
HOST = "0.0.0.0"  # Listen on all network interfaces

print("=" * 60)
print("  GaiaCode UDP Sniffer")
print("=" * 60)
print(f"  Listening on {HOST}:{PORT}")
print("  Press Ctrl+C to stop")
print("=" * 60)
print()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
except OSError as e:
    print(f"CRITICAL ERROR: Could not bind to port {PORT}.")
    print(f"Error: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

packet_count = 0

try:
    while True:
        data, addr = sock.recvfrom(4096)
        packet_count += 1
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        raw = data.decode("utf-8", errors="replace").strip()

        print(f"[{timestamp}] #{packet_count} FROM {addr[0]}:{addr[1]}")
        print(f"  RAW  : {raw}")

        # Try to parse as GaiaGuard format: ID,LABEL,PAYLOAD
        parts = raw.split(",")
        if len(parts) >= 3:
            print(f"  ID   : {parts[0]}")
            print(f"  LABEL: {parts[1]}")
            print(f"  DATA : {parts[2]}")
        else:
            print(f"  (does not match expected ID,LABEL,DATA format)")
        print()

except KeyboardInterrupt:
    print(f"\nStopped. {packet_count} packets received.")
    sock.close()
