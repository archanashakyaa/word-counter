# Function to count the number of words in a given text
def count_words(text):
    words = text.strip().split()
    return len(words)

# Function to count the number of characters (excluding spaces)
def count_characters(text):
    characters = len(text.replace(" ", ""))
    return characters

# Function to count the number of sentences
def count_sentences(text):
    sentences = text.count('.') + text.count('!') + text.count('?')
    return sentences

# Function to count the number of unique words
def count_unique_words(text):
    words = text.strip().lower().split()
    unique_words = set(words)  # Convert to a set to remove duplicates
    return len(unique_words)

# Function to display a summary of text analysis
def display_summary(text):
    word_count = count_words(text)
    char_count = count_characters(text)
    sentence_count = count_sentences(text)
    unique_word_count = count_unique_words(text)
    
    print("\nText Analysis Summary:")
    print(f"Total words: {word_count}")
    print(f"Total characters (excluding spaces): {char_count}")
    print(f"Total sentences: {sentence_count}")
    print(f"Unique words: {unique_word_count}")

# Main function to handle user input and control the program's logic
def main():
    user_input = input("Please enter a sentence or paragraph: ")
    
    if user_input:
        display_summary(user_input)
    else:
        print("You didn't enter any text. Please try again.")
        main()

if __name__ == "__main__":
    main()
