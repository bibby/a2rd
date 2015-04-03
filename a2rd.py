"""
Generates a rundeck resources yaml file from a
directory of ansible-fact json files.

Without using the a2rd bash script, you can do the same thing by:
    ansible all -i hosts.ini -m setup --tree /tmp/some-temp
    python a2rd.py /tmp/some-temp > rundeck-resources.yml
"""
import sys
import json
import os
import pyaml

facts_dir = sys.argv[1]
resources = []
for node in os.listdir(facts_dir):
    node_file = os.path.join(facts_dir, node)
    j = json.load(open(node_file)).get("ansible_facts")
    
    resources.append({
        "osArch": j["ansible_architecture"],
        "hostname": j["ansible_hostname"],
        "nodename": j["ansible_nodename"],
        "osFamily": 'unix',
        "osName": j['ansible_system'],
        "username": j['ansible_user_id']
    })

print pyaml.dump(resources)