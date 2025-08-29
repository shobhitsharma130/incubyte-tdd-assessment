def add(numbers: str) -> int:
    if numbers == "":
        return 0
    normalized = numbers.replace("\n",",")
    parts = [int(num) for num in normalized.split(",")]
    return sum(parts)