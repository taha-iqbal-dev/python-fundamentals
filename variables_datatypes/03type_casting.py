# Type Casting in Python

print("---TYPE CASTING---")

# Initial values
num_int = 10
num_float = 5.5
num_str = "20"
bool_val = True

# int() casting
print("\n--- int() Casting ---")
print(int(num_float))   # float → int
print(int(num_str))     # string → int
print(int(bool_val))    # bool → int (True=1, False=0)

# float() casting
print("\n--- float() Casting ---")
print(float(num_int))   # int → float
print(float(num_str))   # string → float
print(float(bool_val))  # bool → float

# str() casting
print("\n--- str() Casting ---")
print(str(num_int))     
print(str(num_float))   
print(str(bool_val))    

# bool() casting
print("\n--- bool() Casting ---")
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False (empty string)
print(bool("Hello"))    # True


''' Important Note
 Not all conversions are valid
 print(int("Hello"))  # This will cause an error'''