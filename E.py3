import sys
import re
line = sys.stdin.readline()
SANTA = "SANTACLAUS"

words = re.findall(r"([a-zA-Z]+)",line)

#parts = " ".join(line.split("Santa Claus"))

#words = parts.split(".")
#words = "".join(words).split()
i = 0
for i, val in enumerate(words):
    for c, word in enumerate(words):
        if i != c and len(SANTA) == len("".join(words[i:c+1])) and SANTA != "".join(words[i:c+1]).upper():
            if sorted(SANTA) == sorted("".join(words[i:c+1]).upper()):
                print(" ".join(words[i:c+1]).upper())

sys.exit(0)