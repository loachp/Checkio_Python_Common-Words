def checkio(string1, string2):
    common_words = []
    for word in string1.split(","):
        if word in string2.split(","):
            common_words.append(word)
    return ",".join(sorted(common_words))

print(checkio("hello,world", "hello,earth") == "hello")
print(checkio("one,two,three", "four,five,six") == "")
print(checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
