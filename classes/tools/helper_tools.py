import os



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
    # reads all excluded services and removes it from list
    if os.path.isfile('config/exclude.txt'):
        del_file = open('config/exclude.txt')
        del_service = del_file.readlines()
        for service in del_service:
            services.remove(service)

    return services
