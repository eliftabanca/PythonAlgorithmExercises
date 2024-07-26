
name = "Programming"
#first character of the string
m = name[0]
print(f"First character: {m}")

# length (length of the string)
name_length = len(name)
print(f"Length of the string: {name_length}")

# toUpperCase (convert to uppercase)
name_upper = name.upper()
print(f"Uppercase: {name_upper}")

# toLowerCase (convert to lowercase)
name_lower = name.lower()
print(f"Lowercase: {name_lower}")

# substring (substring from index 0 to 6)!
name_substring = name[:6]
print(f"Substring (0 to 6): {name_substring}")

# indexOf (index of the first occurrence of 'g')
word_index = name.find('g')
print(f"Index of 'g': {word_index}")

# replace (replace 'P' with 'p')
name_replaced = name.replace('P', 'x')
print(f"Replaced 'P' with 'p': {name_replaced}")

# equals (check if two strings are equal)
name2 = "PROGRAMMING"
same_name = (name == name2)
print(f"Is the same as 'PROGRAMMING': {same_name}")

# startsWith (check if the string starts with 'P')
starts_with_p = name.startswith('P')
print(f"Starts with 'P': {starts_with_p}")

# endsWith (check if the string ends with 'g')
ends_with_g = name.endswith('g')
print(f"Ends with 'g': {ends_with_g}")

# trim (remove leading and trailing spaces)
name_with_spaces = " P r o g r a m m i n g "
name_trimmed = name_with_spaces.strip()
print(f"Trimmed: '{name_trimmed}'")

# contains (check if the string contains 'Pro')
contains_pro = 'Pro' in name
print(f"Contains 'Pro': {contains_pro}")

# reverse (reverse the string)
name_reversed = name[::-1]
print(f"Reversed: {name_reversed}")

# every second character (every second character in the string)
every_second_char = name[::2]
print(f"Every second character: {every_second_char}")

# from index 1 to 5 with step 2 (characters from index 1 to 5 with step 2)
step_example = name[1:5:2]
print(f"From index 1 to 5 with step 2: {step_example}")
