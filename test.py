#!/usr/bin/env python3
lines = open("README.md", "r").readlines()

for line in lines:
    print(line, end="")

print("\nEverything is OK")
