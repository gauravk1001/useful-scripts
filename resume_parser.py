import re
import json

with open("<path to resume text file>", 'r') as file:
    resume_raw = file.read()

# Remove new line, comma, colon, hiphen, parentheses
resume_parsed = resume_raw.replace('\n', ' ').replace(',', ' ').replace(':', ' ').replace('-', ' ').replace('(', ' ').replace(')', ' ')
resume_parsed = re.sub(r'\s+', ' ', resume_parsed)
resume_words = resume_parsed.split(' ')

word_dict = {}
for word in resume_words:
    word = word.lower()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

sorted_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}

print("Sorted dictionary of words \n" + json.dumps(sorted_dict, sort_keys=False, indent=4))