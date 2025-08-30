def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimeter = ","
    if numbers.startswith("//"):
        delimeter_line,numbers = numbers.split('\n',1)
        delimeter = delimeter_line[2:]

    normalized = numbers.replace("\n",delimeter)
    negatives = [n for n in normalized.split(delimeter) if int(n) < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {negatives}")
    parts = [int(num) for num in normalized.split(delimeter) if int(num) <= 1000 ]
    return sum(parts)