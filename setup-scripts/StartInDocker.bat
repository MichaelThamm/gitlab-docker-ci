:: Change dir into the project root
cd ..
:: Show the images and containers before building
docker images
docker ps -a
:: Build Docker image
docker build -t michaelthamm/github-projects:Riskine-Test .
:: Run the Docker container in detached mode to allow access to port 5000
docker run -d -p 5000:5000 michaelthamm/github-projects:Riskine-Test
:: Set the local webpage location
set url="http://localhost:5000"
:: Start webpage in Google Chrome
start chrome %url%
:: Show the images and containers created
docker images
docker ps -a

EXIT