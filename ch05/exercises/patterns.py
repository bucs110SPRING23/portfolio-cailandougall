def star_pyramid():
    rows=int(input("Enter the number of rows: "))
    for i in range (1, rows+1):
        print("*" * i)
star_pyramid()

def rstar_pyramid():
    rows=int(input("Enter the number of rows: "))
    for i in range (rows, 0, -1):
        print("*" * i)
rstar_pyramid()

    
  