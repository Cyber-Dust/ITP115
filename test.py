# Running Script


list = []
movies = int(input("Enter how many times: "))

for i in range(movies):
    user = input("Enter a movie(Genre:Title): ")
    list.append(user)
# .strip() removes whitespace ??
print(list)
# put the input into a list
if 'comedy' in list:
    print("Good")
else:
    print("You need some Comedy in your life")
