import subprocess

try:
    subprocess.run("pip install ttkbootstrap",shell=True)
except:
    print("error")
    
from PIL import Image
Image.CUBIC = Image.BICUBIC


try:
    subprocess.run("python -m ttkcreator",shell=True)
except(AttributeError):
    print("attributeerror: module 'pil.image' has no attribute 'cubic'. did you mean: 'bicubic'? ")
    print("ακολουθηστε τα βηματα στην οδηγια εγκαταστασης")
except:
    subprocess.run("python3 -m ttkcreator",shell=True)