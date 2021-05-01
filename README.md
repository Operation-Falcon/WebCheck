This project is a part of challenges (10 days challenge) that i took as an ethical hacker.

Day 3

Project 2

![WebCheck](https://user-images.githubusercontent.com/83413793/116781815-1abe4380-aaa3-11eb-84db-8de17d7b8352.png)

Webcheck sees whether there is an http or https service running on given subdomain.

You can pass a single subdomain or domain or can pass the file containing domains to look for http or https service

Installation :

            git clone https://github.com/operationfalcon/WebCheck.git
            
            cd WebCheck
            
            pip3 install -r requirements.txt

Usage :

![Webusage](https://user-images.githubusercontent.com/83413793/116782078-bef4ba00-aaa4-11eb-8d00-ac4ac2e95e6a.png)

            python3 webcheck.py -d <domain/subdomain name>
            
            python3 webcheck.py -f <file containing subdomains> 
            
            
Output :

            python3 webcheck.py -d <domain/subdomain name> | tee result.txt  ( Piping the output to result.txt or as you want it to be)
            
            python3 webcheck.py -f <file containing subdomains> | tee result.txt ( Piping the output to result.txt or as you want it )
