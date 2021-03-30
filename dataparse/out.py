import sys
import os
orig = os.path.join(os.getcwd(), "..", "source", sys.argv[1])
out = sys.argv[2]

a1 = [":{\n", ":[\n", "},\n", "],\n", "\n}", "\n"]
a2 = [":{", ":[", "},", "],", "}", "\\n"]

dat = open(orig, "r").read()
for i in range(len(a1)):
    dat = a2[i].join(dat.split(a1[i]))

k = open(out, "w")
k.write(dat)
k.close()
