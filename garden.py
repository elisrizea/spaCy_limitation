# Import spacy and english core
import spacy
nlp = spacy.load('en_core_web_sm')

# Declare green color to make print more readable.
GREEN = '\033[92m'
END = '\033[0m'

# Load 5 garden sentence
garden_sentences = '''We painted the wall with cracks.
The dog that I had really loved bones.
Helen is expecting tomorrow to be a bad day.
She told me a little white lie will come back to haunt me.
Fat people eat accumulates.'''.splitlines()


# Split every sentence in words and print every sentence
# followed by the spacy explanation in human-readable form
# # followed by the sentence tokens
counter=1
for garden_sentence in garden_sentences:
    print(f'''
******* {GREEN}sentence {counter} {END}*******
''')
    counter +=1
    tuples = [(w.text, w.pos_) for w in nlp(garden_sentence)]
    print(f'{"This is the sentence".upper()}:\n{garden_sentence}')
    str_displayed = ""

    # Create the human-readable explanation
    for i in range(len(tuples)):
        str_displayed += f'{GREEN}{tuples[i][0]}{END} is {spacy.explain(tuples[i][1])}, '

    print('\nThis is spacy human-readable explanation:'.upper())
    print(str_displayed)
    print(f'\n{"This is the list of tokens".upper()}:\n{tuples}\n')

print(f'''# To showcase spaCy limitation I chose: "eat" and "accumulates"
# from the sentence Fat people eat accumulates. spaCy said  "eat" is verb, "accumulates" is noun
# which usually is correct, but in the sentence context is wrong, "eat" is noun, "accumulates" is verb''')


# To showcase spaCy limitation I chose: "eat" and "accumulates"
# from the sentence Fat people eat accumulates. spaCy said  "eat" is verb, "accumulates" is noun
# which usually is correct, but in the sentence context is wrong, "eat" is noun, "accumulates" is verb.
