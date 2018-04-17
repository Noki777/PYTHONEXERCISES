from collections import Counter

def remov_duplicates(input):

    
    input = input.split(" ")

    for i in range(0, len(input)):
        input[i] = "".join(input[i])

    UniqW = Counter(input)

    
    s = " ".join(UniqW.keys())
    print (s)

# Driver program
if __name__ == "__main__":
    input = 'Klienth is great but noki is great also '
    remov_duplicates(input)
