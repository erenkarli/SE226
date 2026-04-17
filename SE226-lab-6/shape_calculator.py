import geometry_utils


def run_calculator():
    funcs = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: area, perimeter (e.g., circle_area)")

    op = input("Enter the operation you want to perform: ").strip().lower()

    if op not in funcs:
        return

    try:
        if "circle" in op:
            val = float(input("Enter radius: "))
            res = funcs[op](val)
        elif "rectangle" in op:
            v1 = float(input("Enter width: "))
            v2 = float(input("Enter height: "))
            res = funcs[op](v1, v2)
        elif "triangle" in op:
            v1 = float(input("Enter base: "))
            v2 = float(input("Enter height: "))
            res = funcs[op](v1, v2)

        print(f"Result: {res:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")


if __name__ == "__main__":
    run_calculator()