import sys
 
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    text = sys.argv[1]
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    text = "madam"     # default string
    print("No input given — using default value:")

 
clean_text = text.lower()

 
if clean_text == clean_text[::-1]:
    result = "It is a palindrome."
else:
    result = "It is not a palindrome."

 
print("\n--- Palindrome Check ---")
print("Script Name:", script_name)
print("Input String:", text)
print("Result:", result)