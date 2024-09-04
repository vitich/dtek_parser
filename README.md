# dtek_parser
The script checks the last message on the public channel that warns about blackouts, filters the message and sends it to your private channel or group.

1) Download this repo and create session directory indide
git clone https://github.com/vitich/dtek_parser.git
cd dtek_parser
mkdir session

2) Get your api_id and api_hash on https://my.telegram.org/apps

3) Modify Dockerfile

4) Build the project
docker build -t dtek_parser .

5) Run it in interactive mode
docker run --rm -it -v $(pwd)/session:/app/session dtek_parser
It will ask your phone number/
Then enter the code from telegram and your password



