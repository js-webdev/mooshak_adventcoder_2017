# Mooschack Adventcoder 2017 [mooshak.nes.aau.at](http://mooshak.nes.aau.at)

Advent Programing Contest by Student IEEE AAU Branch

## Day 1 - Hello Santa!

Congratulations! If you can read this it means you have successfully managed to register, retrieve your password, log in and find the description of problem A!

### Problem

Santa greets you, greet back! Write a program that writes "Hello Santa Claus!" (without the quotes) to the console.

### Sample Output

Hello Santa Claus!

## Day 2 - Weekdays in December

Sometimes, advent can be a terribly stressy time. One has to finish things that need to be done this year, get presents for you loved ones and organize christmas dinner. Eventually, one does not know anymore what weekday it is.

### Problem

Implement a program that tells you the current weekday based on the date in December for this year. An input line will have the format "December n" where n is an integer number between 1 and 31. Calculate the respective weekday and print it (English language, capitalized first letter) to standard output followed by a newline. If the input consists of the word "end", the program should terminate. There will be no other input types except from the ones described.

### Sample Input

December 1
December 16
December 7
end

### Sample Output

Friday
Saturday
Thursday

## Day 3 - Reusing candles

 On each of the four sundays before Christmas, Mr. MacThrifty is lighting candles. On the first Sunday it is one candle, on the second it is two candles, on the third three candles and on the fourth all four candles. Each sunday, any of four candles can be used, but it is not possible to switch between candles during the day. The candles will burn for a fixed time where Mr. MacThrifty holds a session of contemplation. The session time is the same on each sunday. Since Mr. MacThrifty is a bit... thrifty ..., he is going to reuse last years candles, that is four candles with various lengths.

### Problem

Write a program that calculates the maximum session time for a given set of four candles. Your program shall read lines with four space-separated integer values corresponding to the candle lengths in cm. For each cm a candle will burn for one hour. Calculate and print the maximum possible session length with these candles in minutes, then read the next line. When a line contains the word "end", the program shall terminate.

### Sample Input

1 2 3 4
1 1 1 1
end

### Sample Output

60
20
