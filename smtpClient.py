from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    #mailserver = "smtp.gmail.com"

    msg = (f"From:mercedes.ozuna@gmail.com\r\n" 
           f"To:mo489@nyu.edu\r\n" 
           f"Subject:This is a SMTP Client Test Mail Message\r\n"
           f"\r\n"
           f"Hellllllllllllllllo!!!!!\r\n"
           f"This eamil was sent using a socket.\r\n"
           )
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end
    recv = clientSocket.recv(1024).decode()
    #comment before sub--------------------------
    print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')
    #Comment before sub---------------------------

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # comment before sub--------------------------
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # comment before sub--------------------------

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # fromCommand = 'FROM ' + mailserver + '\r\n'
    fromCommand = 'MAIL FROM:<mercedes.ozuna@gmail.com>\r\n'
    clientSocket.send(fromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # comment before sub--------------------------
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')
    # comment before sub--------------------------
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptCommand = 'RCPT TO:<mo489@nyu.edu\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    # comment before sub--------------------------
    print(recv3)
    if recv3[:3] != '250':
        print('250 reply not received from server.')
    # comment before sub--------------------------
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    # comment before sub----------------------
    print(recv4)
    if recv4[:3] != '354':
        print('354 reply not received from server.')
    # comment before sub----------------------
    # Fill in end
    #send combined
    clientSocket.sendall((msg + endmsg).encode())
    recv5 = clientSocket.recv(1024).decode()
    print(recv5)
    if recv5[:3] != '250':
        print('250 reply not received from server.')


    # # Send message data.
    # print("i made it after data")
    # clientSocket.send(msg.encode())
    # recv5 = clientSocket.recv(1024).decode()
    # # comment before sub----------------------
    # # comment before sub----------------------
    # print(recv5)
    # if recv5[:3] != '250':
    #     print('250 reply not received from server.')
    # # comment before sub----------------------
    # # Fill in end
    # print("i made it after msg")
    # # Message ends with a single period, send message end and handle server response.
    # # Fill in start
    # clientSocket.send(endmsg.encode())
    # recv6 = clientSocket.recv(1024).decode()
    # # comment before sub----------------------
    # # comment before sub----------------------
    # print("i made it to after endmsg")
    # print(recv6)
    # if recv6[:3] != '250':
    #     print('250 reply not received from server.')
    # # comment before sub----------------------
    # # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    # comment before sub----------------------
    print(recv7)
    if (recv7[:3] !=
            '221'):
        print('221 reply not received from server.')
    # comment before sub----------------------

    clientSocket.close()
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')