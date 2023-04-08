# A program to take a string and reverse all the words inside it and not the entire string.

into = input("Enter in a string of any length:")

q = len(into)
if into[q - 1] != "." or "?" or "!":
    into +="."
i = 0
k = 0
p = 0
r_words = []

while i < into.__len__():
    if into[i] == " ":
        j = i - 1
        while j >= k:
            r_words.append(into[j])
            j -= 1
        if p < 1:
                r_words.append(" ")
                p += 1
        k = i
    elif into[i] == ".":
        j = i - 1
        while j >= k:
            r_words.append(into[j])
            j -= 1
        if p < 1:
                r_words.append(" ")
                p += 1
        r_words.append(" ")
        k = i
    elif into[i] == "!":
        j = i - 1
        while j >= k:
            r_words.append(into[j])
            j -= 1
        if p < 1:
                r_words.append(" ")
                p += 1
        r_words.append(" ")
        k = i
    elif into[i] == "?":
        j = i - 1
        while j >= k:
            r_words.append(into[j])
            j -= 1
        if p < 1:
                r_words.append(" ")
                p += 1
        r_words.append(" ")
        k = i
        print()
    i += 1

print("The final output is...")

for i in r_words:
    print(i ,end="")