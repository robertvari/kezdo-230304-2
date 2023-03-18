def print_all_params(*args, **kwargs):
    print(args)
    print(kwargs)

print_all_params(
    1,
    2,
    3,
    name="Robert",
    address="Budapest"
)