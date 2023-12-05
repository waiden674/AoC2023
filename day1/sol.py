lines = []

with open("day1/input.txt", "r") as f:
    lines = f.readlines()

def p1():
    total = 0
    for line in lines:
        numstr = []
        for c in line:
            if c.isnumeric():
                numstr.append(c)
        total += int(f"{numstr[0]}{numstr[-1]}")

    print(total)

def p2():
    total = 0
    for line in lines:
        left = find_left_num(line)
        right = find_right_num(line)
        total += left*10 + right
        
    print(total)

vocab = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def find_left_num(line):
    leftmost_index = float("inf")
    value = 0
    for word in vocab.keys():
        idx = line.find(word)
        if idx!= -1 and idx < leftmost_index:
            leftmost_index = idx
            value = vocab[word]
    
    for idx, c in enumerate(line):
        if c.isnumeric():
            if idx < leftmost_index:
                return int(c)
            else:
                break
            
    return value

def find_right_num(line):
    rightmost_index = float("-inf")
    value = 0
    for word in vocab.keys():
        idx = line.rfind(word)
        if idx!= -1 and idx > rightmost_index:
            rightmost_index = idx
            value = vocab[word]
    
    for idx, c in reversed(list(enumerate(line))):
        if c.isnumeric():
            if idx > rightmost_index:
                return int(c)
            else:
                break
            
    return value
    

if __name__ == '__main__':
    p2()