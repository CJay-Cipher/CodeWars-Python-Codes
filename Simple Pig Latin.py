"""
Move the first letter of each word to the end of it, then add "ay" to
the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') == igPay atinlay siay oolcay
pig_it('Hello world !')     == elloHay orldway !

"""

def pig_it(text):
    from string import punctuation as pt

    return " ".join([x if x in pt else (x[1:] + x[0] + "ay") for x in text.split(" ")])


print(pig_it('Hello world !') == "elloHay orldway !")

print(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
