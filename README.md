# dockerTesting-DDD
A (previously) simple pyhton programm to set up a local dev environment for the [
The-Microservice-Dungeon](https://github.com/The-Microservice-Dungeon)

---
#Table of content

* [Prerequisites](#prerequisites)
* [Usage](#usage)
  * [Commands](#commands)

---


<a name="prerequisites"></a>
## Prerequisites
* Python 3
* Docker
* Docker Compose 
* pyyaml 
  * `pip3 install pyyaml`


---
<a name="usage"></a>
## Usage
This tool helps to create and run a local development environment. In the default setting the tool will download the
newest images of the dungeon repos. To exclude your service please edit the [env_setup_default.yml](config/environments/env_setup_default.yml).
It will also be possible to create a custom dev environment, but since this feature is still experimental, it will
not be described. You can always display the help with `python3 dungeon-dev-env.py -h`

###Commands
<a name="command"></a>
* `python3 dungeon-dev-env.py [OPTION]`



| Option | Argument         | Effect                                    |
|--------|------------------|-------------------------------------------|
| -i     |                  | initializes the local dev environment     |
| -r     |                  | runs the environment                      |
| -s     |                  | stops the environment                     |
| -d     |                  | deletes all local images and networks     |
| -u     |                  | updates the environment                   |
| -p     | [run or include] | runs or includes the local player service |
| -u     |                  | updates all docker images                 | 
| -h     |                  | display help                              |

### Hints

* `python3 dungeon-dev-env.py -i` always needs to be run before `-r`
* Before running `-p`, you need to manually create a directory `./classes/player_configs`. It will not be 
persisted, there is an entry in .gitignore. 
* `python3 dungeon-dev-env.py -d` will display an error message like: `Error: No such image: confluentinc/cp-zookeeper`. This is caused by the deletition method and can be safely ignored. 
