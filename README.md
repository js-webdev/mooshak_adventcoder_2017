# Mooschack Adventcoder 2017 [mooshak.nes.aau.at](http://mooshak.nes.aau.at)

Advent Programing Contest by Student IEEE AAU Branch

## Day 1 - Hello Santa!

Congratulations! If you can read this it means you have successfully managed to register, retrieve your password, log in and find the description of problem A!

### Problem

Santa greets you, greet back! Write a program that writes "Hello Santa Claus!" (without the quotes) to the console.

### Sample Output

`Hello Santa Claus!`

## Day 2 - Weekdays in December

Sometimes, advent can be a terribly stressy time. One has to finish things that need to be done this year, get presents for you loved ones and organize christmas dinner. Eventually, one does not know anymore what weekday it is.

### Problem

Implement a program that tells you the current weekday based on the date in December for this year. An input line will have the format "December n" where n is an integer number between 1 and 31. Calculate the respective weekday and print it (English language, capitalized first letter) to standard output followed by a newline. If the input consists of the word "end", the program should terminate. There will be no other input types except from the ones described.

### Sample Input

```
December 1
December 16
December 7
end
```

### Sample Output

```
Friday
Saturday
Thursday
```

## Day 3 - Reusing candles

On each of the four sundays before Christmas, Mr. MacThrifty is lighting candles. On the first Sunday it is one candle, on the second it is two candles, on the third three candles and on the fourth all four candles. Each sunday, any of four candles can be used, but it is not possible to switch between candles during the day. The candles will burn for a fixed time where Mr. MacThrifty holds a session of contemplation. The session time is the same on each sunday. Since Mr. MacThrifty is a bit... thrifty ..., he is going to reuse last years candles, that is four candles with various lengths.

### Problem

Write a program that calculates the maximum session time for a given set of four candles. Your program shall read lines with four space-separated integer values corresponding to the candle lengths in cm. For each cm a candle will burn for one hour. Calculate and print the maximum possible session length with these candles in minutes, then read the next line. When a line contains the word "end", the program shall terminate.

### Sample Input

```
1 2 3 4
1 1 1 1
end
```
### Sample Output

```
60
20
```

## Day 4 - There's snow outside

 Alice lives in an area with quite unstable weather. Sometimes it snows heavily, then the next day is sunshine, followed by rain. Alice often gets confused if there is snow outside (which means she has to get up earlier and shovel snow) or not (which means Alice can sleep in).

### Problem

Implement a program that tells Alice the estimated snow height based on the metereological history. Read several lines with the weather, which can be (their effects are given in brackets):

```
heavy snowing (snow +10 cm)
snowing (snow +5 cm)
light rain (snow -3 cm)
heavy rain (snow -8 cm)
cloudy (+- 0 cm)
sunshine (snow melts down by 1cm)
```

The initial snow height is 0 cm. Your program shall output the snow height in cm after each day. When reading the word "end" the program shall terminate.

### Sample Input

```
heavy snowing
heavy rain
snowing
light rain
cloudy
sunshine
end
```

### Sample Output

```
10
2
7
4
4
3
```

## Day 5 - Santagram Finder

Santa is a big fan of anagrams. An anagram is a word or phrase that exactly reproduces the letters of a given phrase or word in another order. Santa even invented his own version of anagrams, the so called Santagrams, which are build by rearranging the letters of "SANTA CLAUS", for example into "LUCAS SATAN".

### Problem

Implement a program that finds Santagrams in a line of text. Whenever a sequence of words forms a Santagram, a line containing these words shall be written to the console in uppercase letters separated by spaces. Spaces, periods or commas separate words to be analyzed but should be ignored in the Santagram. Also the case should be ignored. In order to be a Santagram, the order of the letters must change, so the original "SANTA CLAUS" is not a Santagram. After processing one line of input, the programm shall terminate.

### Input

```
Santa Claus thinks Satan Lucas is a class aunt.
```

### Output

```
SATAN LUCAS
A CLASS AUNT
```