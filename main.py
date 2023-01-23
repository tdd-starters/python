
def capitalize(source: str) -> str:
    return " ".join(map(lambda s: s.capitalize(), source.split()))