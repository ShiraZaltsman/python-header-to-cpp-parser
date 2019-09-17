import pyperclip

import glob

for filename in glob.glob('*.h'):
    classname = ""
    cppfile = ["#include \"" + filename + "\"\n"]
    with open(filename, 'r') as heder:
        for line in heder:
            line = line.strip()
            # if its deceleration of class
            if "class" in line:
                line = line.split(" ")
                classname = line[1].strip('{')
                classname = classname.strip()
            # if its deceleration of func
            elif not (line.startswith("/*") or line.startswith("//")) and "(" in line:
                line = line.replace(";", "")
                if "operator" in line:

                    funcDetails = line.split(" ", 1)
                    newfuncLine = funcDetails[0] + " " + classname + "::" + funcDetails[1] + "{\n\n}\n"
                    cppfile.append(newfuncLine)
                else:
                    cppfile.append(classname + "::" + line + "{\n\n}\n")

    cppfilename = filename.replace(".h", ".cpp")
    cpphendl = open(cppfilename, "w")
    cpphendl.write("".join(cppfile))
