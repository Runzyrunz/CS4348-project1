# Devlog for Operating Systems Project 1

# October 18, 2025  7:00 pm - planning

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
