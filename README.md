# dtek_parser
The script checks the last message on the public channel that warns about blackouts, filters the message and sends it to your private channel or group.

1) Download this repo and create session directory inside
```
git clone https://github.com/vitich/dtek_parser.git
cd dtek_parser
mkdir session
```
3) Get your api_id and api_hash on https://my.telegram.org/apps

4) Modify ENVs in Dockerfile

5) Build the project
```
docker build -t dtek_parser .
```
6) Run it in interactive mode for the first time
```
docker run --rm -it -v $(pwd)/session:/app/session dtek_parser
```
It will ask your phone number/
Then enter the code from telegram and your password
7) Now you can run container on background with -d option) 
```
docker run -d --rm -it -v $(pwd)/session:/app/session dtek_parser
```


