"""Reusing candles"""
import sys
import re

for input_string in sys.stdin.readlines():
    if input_string == "end":
        sys.exit(0)
    if re.match(r"\d+ ?", input_string):
        values = input_string.split(' ')
        if len(values) == 4:
            candles = [0, 0, 0, 0]
            for i, value in enumerate(values):
                values[i] = int(value)
                candles[i] = int(value)*60
            candles = sorted(candles)
            time = [[0], [0, 0], [0, 0, 0],[0, 0, 0, 0]]
            for i in range(4):
                if i == 0:
                    time[0][0] = candles[3] / 4

                    candles[3] = candles[3] - candles[3] / 4
                elif i == 1:
                    time[1][0] = candles[3] / 3
                    time[1][1] = candles[2] / 3

                    candles[3] = candles[3] - candles[3] / 3
                    candles[2] = candles[2] - candles[2] / 3
                elif i == 2:
                    time[2][0] = candles[3] / 2
                    time[2][1] = candles[2] / 2
                    time[2][2] = candles[1] / 2

                    candles[3] = candles[3] - candles[3] / 2
                    candles[2] = candles[2] - candles[2] / 2
                    candles[1] = candles[1] - candles[1] / 2
                else:
                    time[3][0] = candles[3]
                    time[3][1] = candles[2]
                    time[3][2] = candles[1]
                    time[3][3] = candles[0]

                    candles[3] = candles[3] - candles[3]
                    candles[2] = candles[2] - candles[2]
                    candles[1] = candles[1] - candles[1]
                    candles[0] = candles[0] - candles[0]
                candles = sorted(candles)
            print(int(min(time[3])))
