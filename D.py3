import sys

snow = int(0)
for line in sys.stdin.readlines():
    input_string = line.split("\n")
    if input_string[0] == "end":
        sys.exit(0)
    if input_string[0] == "heavy snowing" or input_string[0] == "heavy snow":
        snow += 10
    elif input_string[0] == "snowing":
        snow += 5
    elif input_string[0] == "heavy rain":
        snow -= 8
    elif input_string[0] == "light rain":
        snow -= 3
    elif input_string[0] == "sunshine":
        snow -= 1
    if snow < 0:
        snow = int(0)
    sys.stdout.write(str(int(snow))+"\n")
