# opens file and returns list of lines
def readFile(filename):

    source = []

    try:
        source = open(filename).read().splitlines()
    except:
        print 'ERROR: {} does not exist'.format(filename)

    # return non-empty lines
    return filter(None, source)



# Write function to open file and preprocess.
def preprocess(filename):
    source = readFile(filename)

    # Remove comments.

    # Find any import statements and replace with relevant files.
    for line in source:
        if "import" in line:
            line = line.replace('.' , '')


    # Remove unnecessary whitespace.


