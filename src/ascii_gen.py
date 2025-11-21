from art import text2art

chars = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','a','s','d','f','g','z','x','c','v','b','y','u','i','o','p','h','j','k','l',';','n','m',',','.','/',]

ascii_chars = {}
for i in range(len(chars)):
    ascii_chars[chars[i]] = text2art[chars[i]]

with open("type-it/ascii/ascii_characters.py", "w") as f:
    print(ascii_chars, file=f)

