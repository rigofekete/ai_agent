from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content
from functions.write_file_content import write_file

class test():

    # result = get_files_info("calculator", ".") 
    # print("Result for current directory:")
    # print(result)
    #
    #
    # result = get_files_info("calculator", "pkg") 
    # print("Result for 'pkg' directory:")
    # print(result)
    #
    # result = get_files_info("calculator", "/bin") 
    # print("Result for '/bin' directory:")
    # print(result)
    #
    # result = get_files_info("calculator", "../") 
    # print("Result for '../' directory:")
    # print(result)

    # Lorem ipsum test 
    # result = get_files_content("calculator", "lorem.txt")
    # print("Result for 'lorem.txt' file:")
    # print(result)

    # result = get_files_content("calculator", "main.py") 
    # print("Result for 'main.py' file:")
    # print(result)
    #
    # result = get_files_content("calculator", "pkg/calculator.py") 
    # print("Result for 'calculator.py' file:")
    # print(result)
    #
    # result = get_files_content("calculator", "/bin/cat") 
    # print("Result for '/bin/cat' directory:")
    # print(result)
    #

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for 'lorem.txt' content write file")
    print(result)
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for 'pkg/morelorem.txt' content write file")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for '/tmp/temp.txt' content write file")
    print(result)

if __name__ == "__main__":
    test()
