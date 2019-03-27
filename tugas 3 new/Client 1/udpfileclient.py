import socket
import os
import sys

# os.mkdir(save_path)
 
minta1="x"
UPLOAD="x"
#port
TARGET_IP = "127.0.0.1"
TARGET_PORT = 9000

command = sys.argv[1] 
mintafile = sys.argv[2] 
#socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TARGET_IP, TARGET_PORT)) 

#sending signals to the server if the client is ready

try:
    print(" berhasil masuk ke try")
    while True:  
        print("berhasil masuk ke try")
        sock.send(command)
        print("ini adalah data")

        if(command=="rq"):
            print("berhasil masuk ke rq")
            sock.send(mintafile)
            print(mintafile)
            while True:
                data = sock.recv(1024) 
                print("ini adalah data")
                print(data)
                if(data[0:6]=="START"):
                    print "full data ",data
                    file_name=os.path.join(save_path,data[6:])

                    print "Menerima ",data[6:]
                    fp = open(file_name,'wb+')
                    ditulis = 0
                elif(data[0:5]=="DONE"):
                    fp.close()
                elif(data[0:4]=="END"):
                    break
                else:
                    print "Blok ", len(data), data[0:10]
                    fp.write(data)      
     
     
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()



       
    
             


