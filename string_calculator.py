def add(numbers: str) -> int:
    if numbers == "":
        return 0
    parts = [int(num) for num in numbers.split(",")]
    return sum(parts)