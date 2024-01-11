def find_short(s):
    lst1 = s.split(' ')
    shortest = []
    for i in lst1:
        if i:
            length = len(i)
            shortest.append(length)
    shortest.sort()
    return shortest[0]


print(find_short("bitcoin take over the world maybe who knows perhaps"))# --> 3
print(find_short("i want to travel the world writing code one day"))# --> 1
print(find_short("turns out random test cases are easier than writing out basic ones"))# --> 3
print(find_short("Lets all go on holiday somewhere very cold"))# --> 2
print(find_short("Let's travel abroad shall we"))# --> 2