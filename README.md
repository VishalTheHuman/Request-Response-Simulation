# Request Response- : Simulation
![banner](https://github.com/VishalTheHuman/Request-Response-Simulation/assets/117697246/9e6d8948-1e65-43ae-9294-0cb73b6e782d)


## **Description 📝**
The Request Response Simulation project aims to create a Python-based system for simulating HTTP operations (GET, PUT, POST, DELETE) on files. This project provides a platform to understand and experiment with the fundamentals of web-based file handling through a simulated environment. Users can interact with the system to perform various file operations, mimicking real-world scenarios commonly encountered in web development.

## **Features ✨**
- **```Simulated Server:```** Mimics a server environment for storing and managing files.
- **```File Operations:```** Supports GET, PUT, POST, and DELETE methods for file manipulation.
- **```Interactive Interface:```** Offers a user-friendly command-line interface for interacting with the server.
- **```Error Handling:```** Robust error handling to manage invalid requests and server errors.

## **How to use ⚙️**

1. Run the **server.py** in one terminal.  
**```Optional :```** If you're plan of using two devices change the IP addresses in the code accordingly. 

2. Run the **client.py** in a new terminal. And select the operation.  


## **Operations 🧑‍💻**
- **```GET :```**  Enter the name of file that you want. If the file is present in the files folder, it will send the content to the client. You'll be provided with an option to save the file or not. 

- **```POST :```**  Enter the location of the file that you locally have in your client system for uploading to the server. A new file will created. If a file with same name exists in the server, it'll not upload the new file. 

- **```PUT :```**  Enter the location of the file that you locally have in your client system for uploading to the server. It'll create a new file if no file with such name exists. Otherwise, it'll overwrite the existing one in the server. 

- **```DELETE :```**  Enter the name of file that you want to delete. It'll delete it from the server if one such file exists. 