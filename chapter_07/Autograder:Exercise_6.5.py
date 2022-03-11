text = "X-DSPAM-Confidence:    0.8475"
print(float(text[text.find(":")+1:]))

# Let's separate all the statements.
# text.find(":") give us the position where ":" is.

# If whe embed the lat statement inside of a slice we get "text[text.find(":")+1:]"
# this allows to use the result of text.find(":") to slice the string.

# Finally, float parse de number and we directly print the result. 