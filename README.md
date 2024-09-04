# dtek_parser
The script checks the last message on the public channel that warns about blackouts, filters the message and sends it to your private channel or group.<br />

1) Download this repo and create session directory inside.<br />
```
git clone https://github.com/vitich/dtek_parser.git
cd dtek_parser
mkdir session
```
3) Get your api_id and api_hash on https://my.telegram.org/apps<br />

4) Modify ENVs in Dockerfile.<br />

5) Build the project.<br />
```
docker build -t dtek_parser .
```
6) Run it in interactive mode for the first time.<br />
```
docker run -it -v $(pwd)/session:/app/session --restart always --name dtek_parser dtek_parser
```
It will ask your telegram account phone number.<br />
Then enter the code from telegram and your password.<br />

7) Next time you can start/stop the container <br />
```
docker start dtek_parser
```
8) You can look in the log like this
```
docker logs -f dtek_parser
```
