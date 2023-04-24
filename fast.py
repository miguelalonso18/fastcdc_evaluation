import os
import platform
import subprocess
import numpy as np
import matplotlib.pyplot as plt

base_windows = "C:\\Users\\Miguel\\Downloads" # windows
base_linux = '/home/miguel/dev/dedup/data' # linux

# Get the operating system name
os_name = platform.system()
base_path = base_windows if os_name == "Windows" else base_linux

folders = []
obj = os.scandir(base_path)
print("Files and Directories in '% s':" % base_path)
for entry in obj :
    if entry.is_dir() or entry.is_file():
        folders.append(entry.name)

for folder in folders:
    print("Processing Folder: " + str(folder))

    command = "fastcdc scan " + base_path + "/" + str(folder + " -r -mi 16384 -s 16384 -ma 16384")

    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))

xs = np.linspace(-np.pi, np.pi, 30)
ys = np.sin(xs)
markers_on = [12, 17, 18, 19]
plt.plot(xs, ys, '-gD', markevery=markers_on, label='line with select markers')
plt.legend()
plt.show()

