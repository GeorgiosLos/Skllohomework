def main():
   
    with open("/home/hp/Skillohomework/homework_5/homework9/numbers.txt", "r") as file:
        
        total = 0
        
        
        for line in file:
           
            total += int(line.strip())

    
    print("The sum of the numbers in 'numbers.txt' is:", total)

if __name__ == "__main__":
    main()
