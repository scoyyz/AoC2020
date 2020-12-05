#! /usr/bin/env python3

def find_2020_sums(entries):
	i = 0
	while i < len(entries)-1:
		x = i + 1
		while x < len(entries):
			if entries[i]+entries[x] == 2020:
				return [i,x]
			x+=1
		i+=1
        
def find_2020_triple_sums(entries):
    i = 0
    while i < len(entries)-1:
        x = i + 1
        while x < len(entries):
            y = x +1
            while y < len(entries):
                if entries[i] + entries[x] + entries[y] == 2020:
                    return [i,x,y]
                y += 1
            
            x+=1
        i+=1
		

with open("Day1Input.txt") as file:
    input = file.readlines()
    input = [int(i) for i in input]
    file.close()
    x,y,z = find_2020_triple_sums(input)
    result = [input[x],input[y],input[z]]
    print(result)
    