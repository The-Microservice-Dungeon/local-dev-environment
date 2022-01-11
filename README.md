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
| -d |  stop, delete | Stops all containers or deletes all containers and images  |
| -i  |   | removes the excluding file  |
| -l  |   | Lists all services (including the excluded services) |
| -p |   | runs local Player service in Docker |
| -u |  | updates all docker images | 

### Hints

* `python3 devcreate.py -s` always needs to be run before `-r`
* Before running `-p`, you need to manually create a directory `./classes/player_configs`. It will not be 
persisted, there is an entry in .gitignore. 
* `python3 devcreate.py -d delete` will display an error message like: `Error: No such image: confluentinc/cp-zookeeper`. This is caused by the deletition method and can be safely ignored. 
