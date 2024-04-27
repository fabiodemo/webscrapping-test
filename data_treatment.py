import glob

print(glob.glob(r"Downloads/*.csv"))
for filename in glob.glob(r"Downloads/*.csv"):
    print(filename)
for filename in (glob.glob(r"Downloads/Zip/*")):
    print(filename)