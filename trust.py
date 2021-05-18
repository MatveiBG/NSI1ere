import os
g = open("trust.sh","w")
g.write("#!/bin/bash\n")
fichiers = []

for root, dirs, files in os.walk(os.getcwd()): 
    for i in files: 
        fichiers.append(os.path.join(root, i))

for f in fichiers:
    if f[-6:] == ".ipynb":
        g.write("jupyter trust {}\n".format(f))

g.close()
