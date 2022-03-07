import json

bt = (False, True)

with open('config.json', 'r') as file:
    config_file = json.load(file)
    
try:
    config_file["dry_run"] = bt[config_file["dry_run"]]
except TypeError:
    config_file["dry_run"] = True

try:
    config_file["telegram"]["enabled"] = bt[config_file["telegram"]["enabled"]]
except TypeError:
    config_file["telegram"]["enabled"] = False
    
try:
    config_file["telegram"]["chat_id"] = str(config_file["telegram"]["chat_id"])
except TypeError:
    config_file["telegram"]["chat_id"] = ""
    
with open('config.json', 'w') as file:
    json.dump(config_file, file)
