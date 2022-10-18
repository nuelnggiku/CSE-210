def unique_letters(alphabet):
    """ 
 Check the provided text to see whether any letters are repeated.
A set should be used in this solution, and the performance should be O(n).
    """
    found = set()
    for letter in alphabet:
        # Check the set to see if the letter has already been seen.
        if letter in found:
            return False
        # If not, we shall include it in the set and continue.
        found.add(letter)
    # All of the letters were unique if we were able to get this far.
    return True

# Alternative course of action
def unique_letters2(alphabet):
    """ 
    Check the provided alphabet to see whether any letters are repeated.
A set should be used in this solution, and the performance should be O(n).
    """
    unique = set()
    for letter in alphabet:
        unique.add(letter)
#The three lines above can be condensed to only unique = set (alphabet)

# The unique set should be used if the text solely contains unique letters.
# equal to the length of the alphabet string.

    return len(unique) == len(alphabet)

# This function might be condensed to a single line:
# if set(alphabet) == len, return len (alphabet)


alphabet1 = "akutidaksukakamubangets" # Expect True as each letter is distinct.
print(unique_letters (alphabet1))

alphabet2 = "akutidaksukakamubangets"  # Because 'a' is repeated, anticipate False.
print(unique_letters(alphabet2))

alphabet3 = "" 
print(unique_letters(alphabet3))          # Given that it is an empty string, expect True.