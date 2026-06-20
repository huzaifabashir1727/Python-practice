First_name = ["Huzaifa","Ali","Chuha","Bilal","Ibrahim"]
marks_set_1 = [12,24,37,41,57]

surname_name = ["Bashir","G","H","G","I"]
marks_set_2 = [63,72,88,93,100]

# Example 1
set_1 = list(map(lambda x: x + 5 , marks_set_1))
print(set_1)


# Example 2
# set_2 = set(map(lambda x : x + 2 , marks_set_2))
# print(set_2)

# Example 3
# passed = set(filter(lambda x : x > 30 , marks_set_1))
# print(passed)

# Example 4
# failed = set(filter(lambda x : x < 80 , marks_set_2))
# print(failed)

# Example 5
# def square(x) :
#     return x ** 2

# chain = set(map(square, filter(lambda x : x % 2 == 0 ,marks_set_1)))
# print(chain)