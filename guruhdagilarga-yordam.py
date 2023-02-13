def example():
    rotations = 0
    text = input("Text kiriting: ")
    new_text = text.split()
    for n in new_text: rotations += 1 
    if rotations != 1:
        return f"natija: {rotations} ta so'z"
    else:
        text = text.lower()
        new_text = list(text)
        new_text[0] = new_text[0].upper()
        new_text[-1] = new_text[-1].upper()
        new_text = ''.join(new_text)
        
        return f"natija: {new_text}"
        
print(example())
