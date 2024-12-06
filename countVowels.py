def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


text = "Hello World"
print(count_vowels(text))  
