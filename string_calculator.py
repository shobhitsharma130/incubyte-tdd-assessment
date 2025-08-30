import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line,numbers = numbers.split('\n',1)
        if delimiter_line.startswith("//["):
            delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
            delimiter = "|".join(delimiters)
        else:
            delimiter = delimiter_line[2:]

    normalized = numbers.replace("\n",delimiter)
    negatives = [n for n in normalized.split(delimiter) if int(n) < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {negatives}")
    parts = [int(num) for num in normalized.split(delimiter) if int(num) <= 1000 ]
    return sum(parts)