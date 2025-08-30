import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        if delimiter_line.startswith("//["):
            delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
            delimiter_pattern = "|".join(map(re.escape, delimiters))
        else:
            # single custom delimiter, e.g. //;
            delimiter_pattern = re.escape(delimiter_line[2:])
    else:
        delimiter_pattern = delimiter
    tokens = re.split(delimiter_pattern + "|\n", numbers)
    parts = [int(num) for num in tokens if num]

    negatives = [n for n in parts if int(n) < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {negatives}")
    parts = [n for n in parts if n <= 1000]
    return sum(parts)