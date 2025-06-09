# time.py
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"
