print()

# https://docs.python.org/3/library/pathlib.html?highlight=pathlib

from pathlib import Path 

path = Path('/git/sunny/python/python_course_1')
print(path.exists())  # Returns boolean value

# path.mkdir() # You can use this to make a DIR

# Print files in a directory
for file in path.glob('*.py'):
    print(file)
