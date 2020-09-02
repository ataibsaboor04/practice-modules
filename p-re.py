import re

"""
    USEFUL FUNCTIONS
    - re.search
    - re.findall
    - re.split
    - re.sub
"""

"""
                            www.regex101.com
"""

'^'  # Matches the beginning of the line
'$'  # Matches the end of the line
'?'  # Matches 0 or 1 appearance of the character before it
'.'  # Matches any character
'|'  # Match either expression
'\s'  # Matches whitespace
'\S'  # Matches any non-whitespace character
'\w'  # Matches letters, numbers and underscores
'\d'  # Matches digits
r'\b'  # Matches Word Boundries
'*'  # Repeates a character zero or more times
'*?'  # Repeates a character zero or more times (non-greedy)
'+'  # Repeats a character one or more times
'+?'  # Repeates a character one or more times (non-greedy)
'{n}'  # Repeates a character n times.
'{n1,n2}'  # Repeats a character ranging from n1 to n2
'{n,}'  # Repeats a character starting from n
'{,n}'  # Repeats a character to n
'[aeiou]'  # Matches a single character in the listed set
'[^XYZ]'  # Matches a single character not in the listed set
'[a-z0-9]'  # The set of characters can include a range
'('  # Indicates where string extraction is to start
')'  # Indicates where string extraction is to end
're.IGNORECASE'  # Ignore the case by passing it to the search function


match = re.search(r'^x', "xenon")
# <re.Match object; span=(0, 1), match='x'>

"""
                                WILDCARDS
"""
match = re.search(r'p.ng', "clapping")
# <re.Match object; span=(4, 8), match='ping'>

match = re.search(r'p.ng', "Penguin", re.IGNORECASE)
# <re.Match object; span=(0, 4), match='Peng'>

"""
                            CHARACTER CLASSES
"""
match = re.search(r"[pP]ython", "Python")
# <re.Match object; span=(0, 6), match='Python'>

match = re.search(r"cloud[a-zA-Z0-9]", 'cloud9')
# <re.Match object; span=(0, 6), match='cloud9'>

match = re.search(r"[^a-zA-Z]", "A sentence.")
# <re.Match object; span=(1, 2), match=' '>

match = re.search(r"[^a-zA-Z ]", "A sentence.")
# <re.Match object; span=(10, 11), match='.'>

match = re.search(r"cat|dog", "I like cats.")
# <re.Match object; span=(7, 10), match='cat'>

match = re.search(r"cat|dog", "I like both dogs and cats.")
# <re.Match object; span=(12, 15), match='dog'>

"""
                        REPETITION QUALIFIERS
"""
match = re.search(r"Py.*n", "Pygmalion")
# <re.Match object; span=(0, 9), match='Pygmalion'>

match = re.search(r"[a-zA-Z]*link", "link")
# <re.Match object; span=(0, 4), match='link'>

match = re.search(r"Py.*n", "Python Programming")
# <re.Match object; span=(0, 17), match='Python Programmin'>

match = re.search(r"Py[a-z]*n", "Python Programming")
# <re.Match object; span=(0, 6), match='Python'>

match = re.search(r"Py.*?n", "Python Programming")
# <re.Match object; span=(0, 6), match='Python'>

match = re.search(r"o+l+", "goldfish")
# <re.Match object; span=(1, 3), match='ol'>

match = re.search(r"o+l+", "woolly")
# <re.Match object; span=(1, 5), match='ooll'>

match = re.search(r"o+l+", "boil")
# None

match = re.search(r"p?each", "To each their own")
# <re.Match object; span=(3, 7), match='each'>

match = re.search(r"p?each", "I like peaches")
# <re.Match object; span=(7, 12), match='peach'>

match = re.search(r"[a-zA-Z]{5}", "a ghost")
# <re.Match object; span=(2, 7), match='ghost'>

match = re.search(r"", "")

"""
                        ESCAPING CHARACTERS
"""
match = re.search(r".com", "welcome")
# <re.Match object; span=(2, 6), match='lcom'>

match = re.search(r"\.com", "welcome")
# None

match = re.search(r"\.com", "ataibsaboork@gmail.com")
# <re.Match object; span=(18, 22), match='.com'>

match = re.search(r"\w*", "An example.")
# <re.Match object; span=(0, 2), match='An'>

match = re.search(r"\w*", "An_example3")
# <re.Match object; span=(0, 10), match='An_example'>

match = re.search(r"^A.*a$", "Argentina")
# <re.Match object; span=(0, 9), match='Argentina'>

match = re.search(r"^A.*a$", "Azerbaijan")
# None

print(match)

"""
                            CAPTURING GROUPS
"""
match = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

match.groups()
# ('Lovelace', 'Ada')

match[0]
# Lovelace, Ada

match[1]
# Lovelace

match[2]
# Ada

print(f"{match[2]} {match[1]}")


"""
                            FINDALL
"""
matches = re.findall(r"cat|dog", "I like both dogs and cats.")
# ['dog', 'cat']

matches = re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")
# ['scary', 'ghost', 'appea']

matches = re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared there.")
# ['scary', 'ghost', 'there']

matches = re.findall(r"\w{5,10}", "I really like strawberries")
# ['really', 'strawberri']

matches = re.findall(r"\w{5,}", "I really like strawberries")
# ['really', 'strawberries']

print(matches)

"""
                                SPLIT
"""
lst = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
# ['One sentence', ' Another one', ' And the last one', '']

lst = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']


print(lst)

"""
                                SUB
"""
newstr = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]",
                "Received an email for ataibsaboork@gmail.com")
# Received an email for [REDACTED]

newstr = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# Ada Lovelace

print(newstr)
