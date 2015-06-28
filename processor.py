# TODO remove os later as we already import it in bot
import os

def file_ext(file_name):
    ext = os.path.splitext(file_name)[-1].lower()

    # Now we can simply use == to check for equality, no need for wildcards.
    if ext == ".py":
        return "python"
    elif ext == ".js":
        return "javascript"
    elif ext == ".java":
        return "java"
    elif ext == ".c":
        return "C"
    elif ext == ".cpp":
        return "c++"
    elif ext == ".rb":
        return "ruby"
    else:
        return " "

def process_file(arg_file):
    log = open(arg_file,'r')
    FILE = log.readlines()
    log.close()

    # TODO append filenames
    ext = file_ext(arg_file)

    in_mem_copy=[]
    markers=[]
    counter=0

    for line in FILE:
        # print line
        counter+=1
        if (key_global in line):
            #  marker now knows where a given TODO is
            markers.append(counter)

            # here you may want to do some splitting/concatenation/formatting to your string
        in_mem_copy.append(line)

    issues = []
    # read in memory copy of markers and print them out.
    for marker in markers:
        # marker is the position of the current TODO
        title = "'{0}' found on line {1} of {2}".format(key_global, marker, arg_file)
        # grab the next 5 lines of it and make that the description
        # formatted ```python for example
        description = '```'+ext

        # grab the next 5 lines.
        for line in in_mem_copy[marker:marker+5]:
            description += line

        # we now have an issue tuple
        current_issue = (title, description)
        # append the tuple to an array of all issue tuples in the file
        issues.append(current_issue)
    
    return issues

process_file('test/file.js', 'python')
