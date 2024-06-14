def q25():
    try :
        with open('C:/Users/muska/OneDrive/Desktop/demo.txt','r') as source_file :
            contents = source_file.read() 
        with open('C:/Users/muska/OneDrive/Desktop/demo1.txt','w') as des_file :
            des_file.write(contents)
        
        print("File copied successfully")
    except FileNotFoundError :
        print("source file doesn't exist")
    except IOError :
        print(f"An error occured while copying the file {IOError}")

q25()