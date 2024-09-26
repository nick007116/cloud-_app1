numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
average = sum(numbers) / len(numbers) if numbers else 0
print(average)
