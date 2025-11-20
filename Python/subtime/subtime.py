from datetime import timedelta
from sys import argv

# taking a file(example.srt) as a command-line argument
if len(argv)!= 2:
    print("Usage: python subtime.py <subtitle.srt>")
    quit()

file = open(argv[1], "r")

# initializing a varible for the final time result
result = timedelta()

# calculating the sum of all the times
for i in file:
    if "-->" in i:

        first_h = float(i[0:2])
        first_m = float(i[3:5])
        first_s = float(i[6:8])
        first_ms = float(i[9:12])

        second_h = float(i[17:19])
        second_m = float(i[20:22])
        second_s = float(i[23:25])
        second_ms = float(i[26:29])

        first_time = timedelta(hours=first_h, minutes=first_m, seconds=first_s, milliseconds=first_ms)
        second_time = timedelta(hours=second_h, minutes=second_m, seconds=second_s, milliseconds=second_ms)

        final = second_time - first_time
        result = result + final

# printing the sum of visible duration time of subtitles
print(result)
file.close()