import re

# What is the most frequent word in the following paragraph?
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
words = re.findall(r"\b\w+\b", paragraph.lower())

words_counter = {}
for word in words:
    words_counter[word] = words_counter.get(word, 0) + 1

sorted_words = sorted(words_counter.items(), key = lambda x: x[1], reverse = True)

print(sorted_words)

# The position of some particles on the horizontal x-axis are -12, 
# -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in 
# the positive direction. Extract these numbers from this whole text 
# and find the distance between the two furthest particles.

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
numbers = [int(n) for n in re.findall(r"-?\d+", text)]

diff = max(numbers) - min(numbers)

print(numbers)
print(diff)

# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(txt):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, txt))

# Clean the following text. After cleaning, count three most frequent words in the string.
def clean_text(txt):
    return re.sub(r'[%$#@;&!?]', "", txt)

def most_3_frequent (txt):
    words = re.findall(r"\b\w+\b", txt.lower())
    words_counter = {}
    for word in words:
        words_counter[word] = words_counter.get(word, 0) + 1
    sorted_words = sorted(words_counter.items(), key = lambda x: x[1], reverse = True)[:3]
    return sorted_words

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_sentence = clean_text(sentence)
print(most_3_frequent(clean_sentence))