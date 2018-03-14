import os


# create a new project directory if one has not been created
def create_project_dir(projectname):
    if not os.path.lexists(projectname):
        print('Creating project...' + projectname)
        os.makedirs(projectname)


# check to see if queue and visited files are created, if not create them
def create_data_files(projectname, baseurl):
    queue = projectname + '/queue.txt'
    visited = projectname + '/visited.txt'
    if not os.path.isfile(queue):
        write_file(queue, baseurl)
    if not os.path.isfile(visited):
        write_file(visited, '')


# create and write to a file given name and data
def write_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()


# append to an exisiting file
def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')
        file.close()


# delete all contents in a file
def delete_file_contents(filename):
    with open(filename, 'w') as file:
        pass


# read from a file and add data into a set
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as file:
        for line in file:
            results.add(line.strip('\n'))
    return results


# convert a set to a file
def set_to_file(links, filename):
    delete_file_contents(filename)
    for link in sorted(links):
        append_to_file(filename, link)
