import pyzabbix


zabbix_URL = "URL"
zabbix_login = "admin"
zabbix_pass = "admin"
disasters = {}
hosts= 0
gidlist = []


zabbix = pyzabbix.api.ZabbixAPI(zabbix_URL)  # set the URL for zabbix server
zabbix.login(zabbix_login,zabbix_pass) # set login and password for the server

def hostsdisaster():
    for h in zabbix.host.get(output=["name"], severities=5, selectHostGroups="extend"): #filter hosts with severities lvl 5
        for id in zabbix.problem.get(hostids=h["hostid"], severities=5):

            if h["hostid"] not in disasters :# create the dictionary with host id and names and disasters
                disasters[h["name"]] = "Não está Respondendo" if "ICMP" in id["name"] else id["name"]
                gid, gpcount, gpname = groupget(h["hostid"])       
                gidlist.append(gid)
                rept = (gidlist.count(gid)) # down ask just move on
                alldown(rept,gpcount,gpname)
                
                    
"""

   Get the group of ID , name and members of the group 

"""

def groupget(id):
    for h in zabbix.hostgroup.get(hostids=id,selectHosts="count"):
        return h["groupid"], h["hosts"], h["name"]
    

"""
check if a group is fully down

"""  
def alldown(list,count,name):
    if list == int(count):
        return print("a Torre de  ", name, " Está down ") # remove print and add the api module
    else :
        pass
    

hostsdisaster()
