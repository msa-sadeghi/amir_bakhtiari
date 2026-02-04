# while True:
#     print("ok")
#     if input("do you want to quit (y | n): ").lower().startswith("y"):
#         break

# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(f"number {i}")


# for i in range(1, 10):
#     print(i)
#     if i % 2 == 0:
#         break
# else:
#     print("end")


# names = ["nikan", "amir", "sara"]
# new_name = input("enter the name: ")
# if new_name in names:
#     names.remove(new_name)
# names.append(new_name)
# names.insert(0, new_name)
# print(names)

# print("salam".upper())

# name = "arash"
# name[0] = "m"


# for i in range(len(names)):
#     print(names[i])


# print(type(names))
# print(len(names))

# for n in names:
#     print(n)


# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1


def find_index(target, numbers):
    for index, item in enumerate(numbers):
        if item == target:
            print(f"عدد {target} در اندیس {index} پیدا شد")
            return index
    else:
        print(f"عدد {target} پیدا نشد")
        return "nothing"


# مثال استفاده
numbers = [10, 25, 30, 45, 60]

print(find_index(30, numbers))  # خروجی: عدد 30 در اندیس 2 پیدا شد
print(find_index(100, numbers))  # خروجی: عدد 100 پیدا نشد
