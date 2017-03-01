# Write function to open file and preprocess.
def preprocess(filename):
  source = open(filename, "r")
  
  # Remove comments.
  
  # Find any import statements and replace with relevant files.
  for line in source :
     if "import" in line:
        line = line.replace('.' , '')
  
  # Remove comments.
  
  # Remove unnecessary whitespace.
