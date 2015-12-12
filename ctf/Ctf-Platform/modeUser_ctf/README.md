Install

Become root, upgrade

    sudo su
    yum upgrade -y
    
Install some prerequisites

    yum install -y git
    yum install -y gcc-c++
    yum install -y python-devel
    
Install Flask and dataset

    easy_install Flask
    easy_install dataset
    exit
        
Import the tasks

    python task_import.py
    
Start the server

    python server.py



*** Restart CTF
    
   Del or Copy ctf.db
