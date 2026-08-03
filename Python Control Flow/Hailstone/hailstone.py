def main():
    n=int(input("Enter a number:"))
    while n!=1:
        if n%2==0:
            print(f"{n} is even, so I take half: {int(n/2)}")
            n=int(n/2)
        else:
            print(f"{n} is odd, so I make 3n+1: {int(3*n+1)}")
            n=int(3*n+1)
   

if __name__ == "__main__":
    main()
