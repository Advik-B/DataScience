s = input("Enter a string: ")
se = input("Enter a search element: ")

if se in s:
    print("The search element is in the string")
    # Find the index of the search element
    i = s.index(se)
    print("The index of the search element is", i)

else:
    print("The search element is not in the string")

