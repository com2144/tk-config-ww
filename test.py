import shotgun_api3 as sg

sg_base_url = "https://west-intern.shotgrid.autodesk.com"
sg_script_name = "juno_api"
sg_script_key = "xuvlnvfbrhMq_mwik8tfhrhyu"

sg_conn = sg.Shotgun(sg_base_url, script_name=sg_script_name, api_key=sg_script_key)

local_storages = sg_conn.find("LocalStorage", [])

for storage in local_storages:
    print(storage)