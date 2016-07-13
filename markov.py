from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    open_file = open(file_path)

    input_path = open_file.read()
    #print input_path

    return input_path


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi'): ['there']}
    """

    chains = {}

    words = text_string.split()

    for i in (range(len(words) - 2)):
        two_words = (words[i], words[i+1])
        value = words[i+2]
        
        if chains.get(two_words): #this means that the key does exist
            
            chains.get(two_words).append(value) 
     
        else:
            chains[two_words] = [value]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # text = ""

    # make a list of punctations that we want to stop our file at.

    first_key = choice(chains.keys())
    # first_value = choice(chains[first_key])
    while first_key[0][0].islower():
        first_key = choice(chains.keys())
    # while the first character of the first item from our tuple key is lowercase, then
    # select another first key


    words_to_add_to_string = [first_key[0], first_key[1]]



    while first_key in chains:
        # pull the value of the first tuple that we started with, from the list of values that it gives, and then set that value to a variable
        new_word = choice(chains[first_key])
        # append that random value to our words_to_add_to_string list
        words_to_add_to_string.append(new_word)
        # set our first_key to first_key[1], and the initial variable that we started off with. 
        first_key = (first_key[1], new_word)

        if first_key[1][-1] in ['.', '!', '?']:
            break
        # if we have a puncuation, we stop. If not, we continue with the loop.

    # Once out of the while loop, we will join the values in the words_to_add_to_string to the text (which will print)
    whole_string = " ".join(words_to_add_to_string)

    return whole_string


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
