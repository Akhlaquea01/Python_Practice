# Append
beta_list = ["apple", "banana", "orange"]
beta_list.append("grape")
print(beta_list)
# insert
beta_list = ["apple", "banana", "orange"]
beta_list.insert(2, "grape")
print(beta_list)
# remove
beta_list = ["apple", "banana", "orange"]
beta_list.remove("apple")
print(beta_list)
# pop
beta_list = ["apple", "banana", "orange"]
beta_list.pop()
print(beta_list)
# del
beta_list = ["apple", "banana", "orange"]
del beta_list[1]
print("del", beta_list)
# add 2 list
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
combo_list = my_list + my_list2
print(combo_list)
# sort
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list)
# range
x = alpha_list[0:4]
print(x)
#
beta_list = ["apple", "banana", "orange"]
beta_list[1] = "pear"
print(beta_list)
for x in range(1, 4):
    beta_list += ['fuit']
    print(beta_list)
# copy
beta_list = ["apple", "banana", "orange"]
beta_list = beta_list.copy()
print(beta_list)
# list-comprehensions
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)
