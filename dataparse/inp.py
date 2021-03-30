import sys
import os
fname = sys.argv[1]
oname = sys.argv[2]
dest = os.path.join(os.getcwd(), "..", "source", oname)

dat = open(fname, "r").read()
a1 = [":{\n", ":[\n", "\n", "},\n", "],\n", "\n}"]
a2 = [":{", ":[", "\\n", "},", "],", "}"]
for i in range(len(a1)):
    dat = a1[i].join(dat.split(a2[i]))

k = open(dest, "w")
k.write(dat)
k.close()
