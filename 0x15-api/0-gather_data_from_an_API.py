#!/usr/bin/python3
''' python script that returns information about employee TODO list progress '''

import sys
import requests

#def employee_progress(employee_id):
#    '''  '''
#    base_url =0

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = requests.get(url + 'user/{}'.format(sys.argv[1])).json()
        to_do = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]

