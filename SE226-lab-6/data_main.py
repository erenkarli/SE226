from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)


def main():
    raw = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8, 21): ")

    try:
        parts = raw.split(",")
        clean_parts = strip_whitespaces(parts)
        nums = [float(x) for x in clean_parts if x != ""]
        unique_nums = remove_duplicates(nums)

        print(f"Cleaned and unique data: {unique_nums}")
        print(f"Mean: {calculate_mean(unique_nums):.2f}")
        print(f"Maximum: {find_maximum(unique_nums)}")
        print(f"Minimum: {find_minimum(unique_nums)}")

    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")


if __name__ == "__main__":
    main()