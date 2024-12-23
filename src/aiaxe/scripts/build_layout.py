import subprocess
import os
import shutil
import sys

def build_frontend():
    frontend_path = 'src/aiaxe/ui'
    os.chdir(frontend_path)

    try:
        subprocess.run(['npm', 'install'], shell=True)
        subprocess.run(['npm', 'run', 'build'], shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error building frontend: {e}")
        sys.exit(1)
        