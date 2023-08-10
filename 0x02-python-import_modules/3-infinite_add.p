#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    result = 0
    
    for i in sys.argv[1:]:  # Start from index 1 to skip the script name
        result += int(i)
    
    print("{}".format(result))
