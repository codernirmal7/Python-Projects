def word_counter(sentence):
    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
    
    # Create an empty dictionary to store word frequencies
    word_count = {}
    
    # Loop through each word in the list
    for word in words:
        if word in word_count:
            word_count[word] += 1  # Increment count if word is already in dictionary
        else:
            word_count[word] = 1  # Add word to dictionary with count 1
    
    return word_count

# Input: Take a sentence from the user
sentence = input("Enter a sentence: ")

# Get the word count dictionary
word_count = word_counter(sentence)

# Output the result
print(word_count)
