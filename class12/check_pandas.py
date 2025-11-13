import os, sys, subprocess, importlib.util, shutil

# Step 1: Check if a fake local numpy folder is shadowing the real one
home_numpy = os.path.expanduser("~/numpy")
spec = importlib.util.find_spec("numpy")

if spec and spec.origin and spec.origin.startswith(os.path.expanduser("~")):
    print(f"⚠️ Found shadowed numpy at: {spec.origin}")
    if os.path.isdir(home_numpy):
        backup = home_numpy + "_backup"
        print(f"📦 Renaming it to: {backup}")
        shutil.move(home_numpy, backup)
    elif os.path.isfile(home_numpy + ".py"):
        print("📦 Renaming stray numpy.py")
        shutil.move(home_numpy + ".py", home_numpy + "_backup.py")
else:
    print("✅ No shadowed numpy folder detected.")

# Step 2: Reinstall numpy in the correct environment
print("\n🔧 Reinstalling numpy...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "numpy"])

# Step 3: Test import
import numpy as np
print(f"\n✅ NumPy successfully imported from: {np.__file__}")
print(f"NumPy version: {np.__version__}")
