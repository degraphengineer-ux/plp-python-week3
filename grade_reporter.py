scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

for score in scores:
    # Add to total score for later average calculation
    total_score += score
    
    # Grade evaluation
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Score: {score} - Grade: {grade}")
    
    # Count passes and fails (passing is 50 or more)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

average_score = total_score / len(scores)

print(f"\nNumber of learners passed: {passed_count}")
print(f"Number of learners failed: {failed_count}")
print(f"Class Average: {round(average_score, 1)}")