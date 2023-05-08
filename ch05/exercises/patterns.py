def star_pyramid():
    for i in range (1, rows+1):
        print("*" * i)


def rstar_pyramid():
    for i in range (rows, 0, -1):
        print("*" * i)

rows=int(input("Enter the number of rows: "))
star_pyramid()
rstar_pyramid()

    
  