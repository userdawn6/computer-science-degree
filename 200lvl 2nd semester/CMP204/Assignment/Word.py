# Create and write to a text file
file_name = 'Count.txt'
content = '''This is a sample text file.
This file contains multiple lines of text.
The goal is to count the number of times a particular word or phrase appears in this file.'''

# Writing content to the text file
with open(file_name, 'w') as file:
    file.write(content)

# Function to count occurrences of a word or phrase in a file
def count_occurrences_in_file(file_name, phrase):
    with open(file_name, 'r') as file:
        text = file.read()
        count = text.lower().count(phrase.lower())  # Case-insensitive count
    return count

# Specify the word or phrase to count
phrase_to_count = "this"

# Counting the occurrences and printing the result
occurrence_count = count_occurrences_in_file(file_name, phrase_to_count)
print(f"The number of times the phrase '{phrase_to_count}' appears in the file '{file_name}' is: {occurrence_count}")
