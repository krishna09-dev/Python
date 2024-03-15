original_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
unique_list = list(set(original_list))

print(f"Original list: {original_list}")
print(f"Unique elements: {unique_list}")


'''
unique_list = []
seen = []  # List to keep track of seen elements

for num in original_list:
    if num not in seen:
    unique_list.append(num)
    seen.append(num)
      '''
