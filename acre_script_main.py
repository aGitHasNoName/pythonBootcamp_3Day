"""
For longer comments, put them inside triple quotes.
Everything inside the triple quotes will be ignored.

MAIN COMMENT

The main comment should explain what the script does and give
any information that someone would need to run the script, 
such as what type of files are required (if any).

For this script:
This script converts a list of square foot measurements to acres.

To run the script:
This script can be run from the command line. This file does 
not need to be open to run the script on the command line.
Run the script on the command line by navigating to the
folder that contains this script and
typing python acre_script.py.
"""

#IMPORT MODULES
#if you have any modules to import, import them at the top of the script,
#under the comments, so that anyone using this script can quickly
#know which modules are required - they might need to install them

#HARD-CODED VARIABLES
#assign any variables, including filenames, here, so that if you want to
#run the script with different data, it's easy to see and change
test_list = [5000, 6500, 8000, 15251]

#FUNCTION DEFINITIONS
#include any function definitions here
def sqft_to_acres(sqft):
    #this function takes square footage and returns rounded acreage
    acres = sqft / 43560
    return round(acres, 2)

#MAIN FUNCTION DEFINITION
#the rest of your code, including any function calls, goes here
def main():
    for test_value in test_list:
        answer = sqft_to_acres(test_value)
        print(str(test_value) + " square feet is " + str(answer) + " acres.")
        
#CALL MAIN FUNCTION
#calling the main function in this way allows your script to be run as a whole script
#AND allows individual functions to be called from this script in other scripts
#AND is convention for Python scripts
if __name__ == "__main__":
    main()


        
