
import sys, getopt,os
from classes.player_service import Player_Service
import json


def strip_new_lines(mylist):
    """Strips all newlines

   
    """
    converted_list = []
    for item in mylist:
        converted_list.append(item.strip())

    return converted_list


def remove_service_from_list(services):
    """removes a service from a list

    Args:
        services (List): List of services
    """
     #reads all excluded services and removes it from list
    if os.path.isfile('config/exclude.txt'):
        del_file = open('config/exclude.txt')
        del_service = del_file.readlines()
        for service in del_service:           
            services.remove(service)
    
    return services


def set_up_environment():
    """Setup Method
        pulls all needed containers and creates all networks
    """

   

    #Reads all service names 
    with open('config/services.txt') as fp:
        lines = fp.readlines()

    lines = strip_new_lines(lines)
    lines = remove_service_from_list(lines)
    
    
    #pulls all needed images from github
    for line in lines:
        line = line.rstrip("\n")
       # os.system(f"mkdir player_service && cd player_service/{line} && docker-compose -f service-compose.yml pull ")
        
    #Creates all networks
    with open('config/networks.txt') as fp:
        lines = fp.readlines()

    lines = strip_new_lines(lines)

    print("Creating networs:")
    for line in lines:
        line = line.rstrip("\n")
        print(f"Creating {line} network:")
        os.system(f"docker network create {line} || true")
    

    


def run_environment():
    
    """Runs all containers
    """

    with open('config/services.txt') as fp:
        lines = fp.readlines()

    lines = strip_new_lines(lines)
    lines = remove_service_from_list(lines)

    for line in lines:
        line = line.rstrip("\n")
        os.system(f"cd deployment/{line} &&  docker-compose -f service-compose.yml up -d  --remove-orphans " )
        

def stop_environment():

    """Stops all containers
    """

    with open('config/services.txt') as fp:
        lines = fp.readlines()

    for line in lines:
        line = line.rstrip("\n")
        os.system(f"cd deployment/{line} &&  docker-compose -f service-compose.yml down" )

    os.system("docker network prune -f")


def exclude_services(file):
    """Excludes a service from the environment

    Args:
        file (String): filename
    """
    if os.path.isfile('config/exclude.txt'):
        print ("Adding another Service to exclude list ")
        f= open("config/exclude.txt","a+")
        f.write(file)
        f.close()
        print(f"The Service {file} has been excluded")
    else:
        f= open("config/exclude.txt","w+")
        f.write(file)
        f.close()
        print(f"The Service {file} has been excluded")



def include_services():
    """Includes all services and deletes exlude file
    """

    os.remove("config/exclude.txt")
    print("Removed exclude.txt")


def list_all_services():
    """Lists all services
    """
    with open('config/services.txt') as fp:
        lines = fp.readlines()
    print("Printing all Services")
    for line in lines:
        print(line)


def update_all_service_images():
    """Updates all service images
    """
    with open('config/services.txt') as fp:
        lines = fp.readlines()

    lines = strip_new_lines(lines)
    lines = remove_service_from_list(lines)

    for line in lines:
        line = line.rstrip("\n")
        os.system(f"cd deployment/{line} &&  docker-compose -f service-compose.yml pull" )


def player_service_creation():
    
    if os.path.isfile('classes/player_configs/config.json'):
        
        player = Player_Service('classes/player_configs/config.json')
    else:
        player = Player_Service()
    
    return player

def delete_containers_networks():
    
    stop_environment()
  
    with open('config/images.txt') as fp:
        lines = fp.readlines()
        lines = strip_new_lines(lines)
        for line in lines:
            os.system(f"docker rmi {line}")




def main(argv):
    
    #reading arguments and options from the commandline
    opts, args = getopt.getopt(argv,"ilrsue:p:d:", ["player" ,"delete", "stop"])



    for opt, arg in opts:
        
        
        if opt == '-r':
            run_environment()
        elif opt == '-s':
            set_up_environment()
        elif opt == '-d':
            if arg == "stop":
                stop_environment()
            elif arg == "delete":
                delete_containers_networks()
        elif opt == '-e':
            exclude_services(arg)
        elif opt == '-i':
            include_services()
        elif opt == '-l':
            list_all_services()
        elif opt == '-u':
            update_all_service_images()
        elif (opt == '-p') or (opt == "--player"):
            player = player_service_creation()
            player.run_player()






if __name__ == '__main__':
    main(sys.argv[1:])


