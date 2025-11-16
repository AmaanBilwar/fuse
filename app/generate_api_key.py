import subprocess

pre_command = input("enter pre api key word here?: ")
generation = subprocess.run("openssl rand -hex 32", shell=True, capture_output=True, text=True).stdout.strip()

final_api_key = f"{pre_command}-{generation}"

print(final_api_key)