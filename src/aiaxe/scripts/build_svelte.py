import subprocess
import os
import shutil
import sys

def build_svelte_frontend():
    frontend_path = 'src/aiaxe/frontend'
    os.chdir(frontend_path)

    try:
        subprocess.run([sys.executable, '-m', 'npm', 'install'], check=True)
        subprocess.run([sys.executable, '-m', 'npm', 'run', 'build'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error building frontend: {e}")
        sys.exit(1)
    
    os.chdir('../../..')

def copy_frontend_dist():
    frontend_dist = 'src/my_package/frontend/dist'
    package_frontend_dist = 'src/my_package/frontend_dist'

    if os.path.exists(package_frontend_dist):
        shutil.rmtree(package_frontend_dist)
    
    shutil.copytree(frontend_dist, package_frontend_dist)