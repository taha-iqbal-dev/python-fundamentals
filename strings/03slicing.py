# Slicing - Accessing parts of String

str1 = "Taha Iqbal"
# Slicing syntax: [start:end]
# Includes start index, excludes end index

print(str1[0:5]) 
print(str1[5:len(str1)]) # slices from index 5 to end (len gives length)

str2 = "Software Engineer"
print(str2[9:]) # Missing ending_index indicates last index
print(str2[:8]) # Missing starting_index indicates first index

# Negative index slicing
# Negative indices count from the end (-1 is last character)
str3 = "National University"
print(str3[-19:-11])