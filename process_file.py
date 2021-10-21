def replace_symbol(content):
    text = list(content)
    for i in range(len(text)):
        if (i+1) % 5 == 0:
            text[i] = "*"
    return text
