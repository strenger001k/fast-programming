def replace_symbol(content):
    text = list(content)
    for i in range(4, len(text), 5):
            text[i] = "*"
    return text
