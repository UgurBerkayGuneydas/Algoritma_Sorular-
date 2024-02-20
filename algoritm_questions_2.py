print("*********************","\t")
print("2.Soru")

INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

def fix_text(mystr):
    # Split the input string into words
    words = mystr.split()

    # Initialize an empty list to store the fixed words
    fixed_words = []

    # Iterate through each word
    for word in words:
        # If the word is wrapped in parentheses, remove them
        if word.startswith("(") and word.endswith(")"):
            fixed_words.append(word[1:-1])
        else:
            # Reverse the word and add it to the fixed list
            fixed_words.append(word[::-1])

    # Join the fixed words back into a string
    fixed_text = " ".join(fixed_words)

    return fixed_text

# Test the function
if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
