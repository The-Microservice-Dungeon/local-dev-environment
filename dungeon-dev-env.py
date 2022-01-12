import sys, getopt, os
from classes.player_service import Player_Service
from classes.dev_environment import Dev_Environment
from classes.dungeon_services import Dungeon_Service
from classes.dev_env_factory import Dev_Env_Factory
import argparse
import json


def player_service_creation():
    """
    Creates a player object
    Returns: Player Object

    """
    if os.path.isfile('classes/player_configs/config.json'):

        player = Player_Service('classes/player_configs/config.json')
    else:
        player = Player_Service()

    return player


def main(args):
    """
    Main Function
    """

    factory = Dev_Env_Factory()
    if args.init:
        factory.create_environment(args.init)
    elif args.run:
        env = factory.create_from_available_version(args.run)
        env.run_environment()
    elif args.stop:
        factory.create_from_available_version(args.stop).stop_environment()
    elif args.delete:
        factory.create_from_available_version(args.delete).delete_containers_networks()
    elif args.update:
        factory.create_from_available_version(args.update).update_all_containers()
    elif args.player:
        if args.player == 'include':
            player_service_creation()
        elif args.player == 'run':
            player_service_creation().run_player()


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(prog="dungeon-dev-env.py",
                                        description='Tool for creating a local dev environment for the dungeon ')
    my_parser.add_argument('-i', '--init',
                           help='Optional Argument: Initializes a new dev environment. If no option is submitted, '
                                'a default environment '
                                'will be created.', const="default", nargs='?')
    my_parser.add_argument('-r', '--run',
                           help='Optional Argument: Runs the environment. if no option is submitted the default '
                                'environment will be run '
                                'will be created.', const="default", nargs='?')

    my_parser.add_argument('-s', '--stop',
                           help='Optional Argument: Stops the environment. if no option is submitted the default '
                                'environment will be run '
                                'will be created.', const="default", nargs='?')
    my_parser.add_argument('-d', '--delete',
                           help='Optional Argument: deletes the images of the environment. if no option is submitted '
                                'the default '
                                'environment will be deleted '
                                'will be created.', const="default", nargs='?')

    my_parser.add_argument('-u', '--update',
                           help='Optional Argument: updates the images of the environment. if no option is submitted '
                                'the default '
                                'environment will be updated '
                                'will be created.', const="default", nargs='?')
    my_parser.add_argument('-p', '--player',
                           choices=['include', 'run'],
                           help='Includes or runs the local player service')
    main(my_parser.parse_args())
