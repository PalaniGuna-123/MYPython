def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))  

def star(n):
    seq=[0,1]
    for _ in range (2,n):
        seq.append(seq[-1]+seq[-2])
    return seq[:n]
print(star(4))