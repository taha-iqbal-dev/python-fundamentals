# for <iterator> in range(start, stop, step):
#     code block executes for each value in the sequence
# Note: range() excludes the stop value

print("---FORWARD LOOP---")
for i in range(1, 11):
    print(i)
print("END")

# reverse loop

print("\n---REVERSE LOOP---")

for j in range(10, 0, -1): # range(10, 0, -1) → start at 10, go down to 1 (step = -1)
    print(j)
print("END")