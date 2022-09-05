import collections

string = input("Enter a string: ")

d={}
def string_to_dict(string):
    for i in string:
        d[i]=0
    for i in string:
        d[i]=d[i]+1

string_to_dict(string)

print(d)
