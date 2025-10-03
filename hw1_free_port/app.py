from typing import List
from flask import Flask
import subprocess
import os
import signal

app = Flask(__name__)

def get_pids(port: int) -> List[int]:
    if not isinstance(port, int):
        raise ValueError
    result = subprocess.run(
        ["lsof", "-t", f"-i:{port}"],
        capture_output=True, text=True
    )
    return [int(pid) for pid in result.stdout.split() if pid.isdigit()]

def free_port(port: int) -> None:
    for pid in get_pids(port):
        os.kill(pid, signal.SIGTERM)

def run(port: int) -> None:
    free_port(port)
    app.run(port=port)

if __name__ == '__main__':
    run(5000)
