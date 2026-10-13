# GaiaCode Tools

Utility tools for the GaiaCode project.

## Description

**UDP_Sniffer.py** — a lightweight UDP packet listener that prints every incoming
packet with a timestamp, source IP/port, and raw payload. Packets matching the
GaiaGuard `ID,LABEL,DATA` format are parsed and displayed field-by-field; all
other payloads are shown raw. Useful for diagnosing Tau station broadcasts.

## Technology Stack

- Python 3 (standard library only: `socket`, `sys`, `datetime`) — no external dependencies.

## Hardware Dependencies

- Any host on the same network segment as the UDP broadcaster.
- No special hardware required; a Tau station (or any UDP sender) is needed to
  generate traffic to observe.

## Setup

```bash
python3 --version   # Python 3.x required; no pip installs needed
```

## Usage

```bash
python UDP_Sniffer.py          # listen on default port 5552
python UDP_Sniffer.py 9999     # listen on a custom port
```

Press `Ctrl+C` to stop; a total packet count is printed on exit.

## Data Formats

Expected payload format (GaiaGuard):

```
ID,LABEL,DATA
```

Example output:

```
[14:03:22.517] #1 FROM 203.0.113.10:5552
  RAW  : 42,TEMP,21.5
  ID   : 42
  LABEL: TEMP
  DATA : 21.5
```
