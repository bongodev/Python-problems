# Count Vowels: Write a function to count the number of vowels in a string.

in_string = input("Enter a string: ")
in_string = in_string.lower()
print("lowercase: ", in_string)

vowels = ["a", "e", "i", "o", "u"]

# iterate through every vowel
for vowel in vowels:
    # print('now in: ', vowel)
    count = 0
    # print(f'ekhane {count}, check korbo {vowel}')
    for letter in in_string:
        if letter == vowel:
            count = count + 1

    # print(f'{vowel} ase {count} bar')
