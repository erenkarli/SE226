num_users = int(input("enter a number of users: "))

user_data = {}

for i in range(num_users):
    username = input("\nEnter username: ")
    num_items =int(input("how many items?"))

    user_items = []
    for j in range (1, num_items + 1):
        item = input(f"Item {j}: ")
        user_items.append(item)

    user_data[username] = user_items
    print("\nUSER DATA: ")
    for user, items in user_data.items():
        print(f"{user} -> {items}")
    all_items = []
    for items in user_data.values():
        all_items.extend(items)

    counts = {}
    for item in all_items:
        counts[item] = counts.get(item,0)+1

    common_items = [item for item, count in counts.items() if count > 1]

    unique_items = [item for item, count in counts.items() if count == 1]

    most_popular = max(counts, key=counts.get)

    print("\nCOMMON ITEMS: ")
    for item in common_items:
        print(item)
    print("UNIQUE ITEMS: ")
    for item in unique_items:
        print(item)
    print("MOST POPULAR ITEM: ")
    print(most_popular)