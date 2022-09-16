#!/usr/bin/python3

import os

torrent_base_dir=''
dest_base_dir=''

print('start scipt in: ' + torrent_base_dir)

for _, tor_types, _ in os.walk(torrent_base_dir):
    for tor_type in tor_types:

        type_path=torrent_base_dir + tor_type
        print('find torrent in: ' + type_path)
    
        for _, _, tor_files in os.walk(type_path):
            for file_name in tor_files:

                tor_path = '\'' + type_path + '/' + file_name + '\''
                dest_path = dest_base_dir + tor_type
                
                scp_command='scp ' + tor_path + ' ' + dest_path
                clear_command='rm -f ' + tor_path
                
                print('run: ' + scp_command)
                result = os.system(scp_command)

                if(result == 0):
                    print('run: ' + clear_command)
                    os.system(clear_command)

print('end scipt')