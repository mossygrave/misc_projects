
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"Original: {fruit_list}")

    fruit_list.reverse()
    print(f"Reversed: {fruit_list}")

    fruit_list.append("orange")
    print(f"Append orange: {fruit_list}")

    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print(f"Insert cherry: {fruit_list}")

    b_index = fruit_list.index("banana")
    fruit_list.pop(b_index)
    print(f"Pop banana: {fruit_list}")

    popped = fruit_list.pop()
    print(f"Last removed: {popped}")

    fruit_list.sort()
    print(f"Sorted: {fruit_list}")

    fruit_list.clear()
    print(f"Cleared: {fruit_list}")


if __name__ == "__main__":
    main()