def to_camel_case(text):
    if '-' in text:
        # If the text contains dashes, split the text using dashes
        words = text.split('-')
    else:
        # If the text contains underscores, split the text using underscores
        words = text.split('_')
    
    # Convert the words to camel case
    camel_case_words = [words[0]]
    for word in words[1:]:
        camel_case_words.append(word.capitalize())
    camel_case_text = ''.join(camel_case_words)
    
    return camel_case_text

# Example usage
print(to_camel_case('hello-world')) # Output: helloWorld
print(to_camel_case('the_quick_brown_fox')) # Output: theQuickBrownFox
print(to_camel_case('Capital-case')) # Output: CapitalCase
print(to_camel_case('snake_case_example')) # Output: snakeCaseExample
