def escape_comma(some_str):
    return_str = ""
    for char in some_str:
        if char == ",":
            continue
        return_str += char
    return return_str
