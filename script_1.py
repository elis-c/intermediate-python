from webbrowser import get


def get_unique_list(list):

    new_list = [];

    for number in list:

        if number not in new_list:
            
            new_list.append(number)
        
    return new_list


my_list = [1,1,2,3,5,5,7]

print(get_unique_list(my_list))