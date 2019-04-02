##Pycdemo

How can anyone run any of these script(s) ?
 
   #### Using in your windows/mac/ubuntu env :
   
    - git clone <repo_git_url>
    - cd /pycdemo/
    - Now follow instructions from common sections.    
    
   #### Using docker env :
   
    - git clone <repo_git_url>
    - cd /pycdemo/
    - docker build -t sughosneo/pycdemo .
    - docker run -it sughosneo/pycdemo /bin/bash
    - Once you are in the docker, follow common section.
   
    
   #### Common Steps :
   
    - Run "python3 compile.py"
    - It would generate one InfoSvc.pyc file under src folder.
    - Now you can delete actual InfoSvc.py file and keep only .pyc file.
    - python3 InfoSvc.pyc    
    - Do "curl http://0.0.0.0:8000/info"
    - You should see success response.
    - If you want to decompile it run "bash ./decompile.sh"
    - It would generate actual source file as "InfoSvc.py" under decompiled dir.
   