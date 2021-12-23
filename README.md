# dockerTesting-DDD
A simple pyhton programm to set up a local dev environment for the [
The-Microservice-Dungeon](https://github.com/The-Microservice-Dungeon)


## Prerequisites
* Python 3
* Docker
* Docker Compose 


---

## Usage

python3 devcreate.py [OPTION]

|  Option | Argument   |  Effect |
|---|---|---|
|  -s |   | Creates the dev environment  |
| -r  |   | Runs all containers  |
| -e  |  [servicename] | Excludes a service from the environment and creates an excluding file  |
| -d |   | Stops all containers  |
| -i  |   | removes the excluding file  |
| -l  |   | Lists all services (including the excluded services) |
| -p |   | runs local Player service in Docker |
