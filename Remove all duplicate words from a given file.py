#remove dupliate words in file in python
seen_lines = set()

with open("file_2.txt", "w") as f2:
    for line in open("file_1.txt", "r"):
        if line not in seen_lines:
            f2.write(line)
            seen_lines.add(line)
