
import sys, getopt,os



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
        os.system(f"cd deployment/{line} && docker-compose -f service-compose.yml pull ")
        
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


def main(argv):
    
    #reading arguments and options from the commandline
    opts, args = getopt.getopt(argv,"ildrse: ")



    for opt, arg in opts:
        
        
        if opt == '-r':
            run_environment()
        if opt == '-s':
            set_up_environment()
        if opt == '-d':
            stop_environment()
        if opt == '-e':
            exclude_services(arg)
        if opt == '-i':
            include_services()
        if opt == '-l':
            list_all_services()






if __name__ == '__main__':
    main(sys.argv[1:])


