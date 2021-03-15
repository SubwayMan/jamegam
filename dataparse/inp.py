import sys
import os
fname = sys.argv[1]
oname = sys.argv[2]
dest = os.path.join(os.getcwd(), "..", "source", oname)

dat = open(fname, "r").read()
dat = ":{\n".join(dat.split(":{"))
dat = ":[\n".join(dat.split(":["))
dat = "\n".join(dat.split("\\n"))
dat = "},\n".join(dat.split("},"))
dat = "],\n".join(dat.split("],"))
dat = "\n}".join(dat.split("}"))
dat = "\n]".join(dat.split("]"))

k = open(dest, "w")
k.write(dat)
k.close()
