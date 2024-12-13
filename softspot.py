import sys
from time import sleep

def print_lyrics():
    lyrics = [
        ("I don't go out, but I'll do it for you", 0.06, 2.0),
        ("You never liked it when I drink too much", 0.06, 2.5),
        ("I hate to dance, but I'd dance with you", 0.06, 2.1),
        ("'Cause I'd do anything to feel your touch", 0.05, 1.9),
        ("Don't like anybody, tell me why it's different with you", 0.04, 1.9),
        ("Don't believe in love, but no one makes me feel like you do", 0.04, 1.9),
        ("I don't say it much 'cause I just always thought That you knew", 0.05, 2.0),
        ("oh", 0.07, 3.5)
    ]

    for line, char_delay, line_delay in lyrics:
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        print()
        sleep(line_delay)

print_lyrics()
