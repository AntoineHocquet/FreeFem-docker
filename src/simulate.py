# src/simulate.py
import subprocess
import os
import platform

def run_simulation():
    current_os = platform.system()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    edp_path = os.path.join(project_root, "edp")
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{edp_path}:/data",
        "antoinehocquet/freefem", "FreeFem++", "/data/heat_disk.edp"
    ]

    print("Running FreeFEM via Docker...")
    try:
        subprocess.run(docker_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Simulation failed:", e)