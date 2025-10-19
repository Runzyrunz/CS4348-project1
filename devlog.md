# Devlog for Operating Systems Project 1

# October 18, 2025  7:00 pm 
Planning

Language: Python

Initial thoughts: 

The objective of this project is to develop three different programs with will operate together to encrypt and decrypt a string. The three programs include a logger process to record this history or commands, an encryption process to perform the encryption and decryption, and a driver process to both launch and communicate between programs through pipes.

Since the language is python, the subprocess module will be used.

In the prompt given, the encryption/decryption used as an example is the vigenere cypher, so testing will proceed using this cypher.

Driver will incoperate a password to establish different users in the logger allow the option to view history

user the format
YYYY-MM-DD HH:MM [ACTION] MESSAGE

ecrypt and decrypt communcations will be sent to encryption program.

Components:

-logger.py
-encryptor.py
-driver.py
-devlog.md
-README.md

During this first session, the local git repo will be set up and commit this devlog, set up a python file for each process and in this session focus on the logger.py


# October 19, 2025 12:05 pm - 

After getting the logger implemented and testing the process. I was able to successfully record actions pertaining to the project and contained in the project.log file. Here the program will be able to log a history of actions to present to the user. 

Now that the logger functional, I can start working on the Encryption process. With the Encryption process, my plan is to 
use the algebraic decription of the vigenere cipher found in the wiki. The formula for the encryption being Ci = (Mi + Ki) mod 26 where Ci is the cipher text, Mi will be the letter of plaintext and Ki is the ith letter of the key. For decryption the formula is Mi = (Ci - Ki + 26) mod 26. The addition of 26 is to prevent the number from being negative. In order for the encryption and decryption to work, i would need to convert the letters of the message to a range of 0-25 first and then subtracting the ASCII value of 'A' so each letter can be identified and manipulated.

When testing the vigenere cipher independently, Encrypting the string HELLO gives an output of RIJVS and Decrypting RIJVS gives the result of HELLO which works seems to work as intended.

After confirming the Encryption process is working, my next session will be to focus on the Driver process since the whole project will be access through this process. Once I can confirm that each process is working independently, i will then work on having them communicate together through pipes, in python useing the Subprocess modeule.

