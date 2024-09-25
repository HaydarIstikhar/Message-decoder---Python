def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Dictionary to store the words with their corresponding numbers
    word_dict = {}
    
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            continue  # Skip lines that don't have exactly two parts
        try:
            number = int(parts[0])
            word = parts[1]
            word_dict[number] = word
        except ValueError:
            continue  # Skip lines where the first part is not a valid integer
    
    # Determine the last number in each line of the pyramid
    last_number = 1
    step = 2
    pyramid_indices = []
    
    while last_number in word_dict:
        pyramid_indices.append(last_number)
        last_number += step
        step += 1
    
    # Collect the words corresponding to the pyramid indices
    decoded_message = [word_dict[index] for index in pyramid_indices]
    
    # Join the words to form the final message
    return ' '.join(decoded_message)

# Decode the message from the provided file
file_path = 'encoded_message.txt'  # Make sure this path matches your saved file location
print(decode(file_path))
