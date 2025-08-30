def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimeter = ","
    if numbers.startswith("//"):
        delimeter_line,numbers = numbers.split('\n',1)
        delimeter = delimeter_line[2:]

    normalized = numbers.replace("\n",delimeter)
    parts = [int(num) for num in normalized.split(delimeter)]
    return sum(parts)