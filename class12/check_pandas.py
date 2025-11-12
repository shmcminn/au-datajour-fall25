# Classroom environment check
import importlib
import sys
import subprocess

required = ["numpy", "pandas"]

for pkg in required:
    if importlib.util.find_spec(pkg) is None:
        print(f"📦 Installing missing package: {pkg} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

print("✅ All required packages are available!")

import pandas as pd
import numpy as np

print(f"pandas {pd.__version__}, numpy {np.__version__} ready to use!")