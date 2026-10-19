count = 1
total = 0

# BUG: Added missing colon at the end of the while loop statement.
while count <= 5: # BUG: Changed '< 5' to '<= 5' so the loop includes the number 5.
    total = total + count
    count = count + 1

# BUG: Converted integer 'total' to a string using str() so it can concatenate properly.
print("Sum of 1 to 5 is: " + str(total))