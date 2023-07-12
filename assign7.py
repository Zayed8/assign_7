def f7(file = "a7file.txt"):
    try:
        f = open(file,"+a")
    except FileNotFoundError:
        print(" Entered File Not Found plz check the file again!")
    except FileExistsError:
        print(" Entered File does not Exits plz check the file again!")
    finally:
        print("File Operation Successfull!")
    f.writelines(["rollno : 65 \n"," name : Zayed Shaikh \n"," class : SYCOA|TYCO|COB2STATIC"])
    f.seek(0)
    print(f.readlines())
    f.close()
f7()