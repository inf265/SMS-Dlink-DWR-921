#!/usr/bin/python

import sys, getopt

from requests import session

def help():
    print('sendsms.py -i <ip-address> -u <username> -p <password> -n <phone-number> -m <message>')


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:u:p:n:m:",["ipaddress=","username=","password=", "number=", "message="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    ipaddress=""
    username=""
    password=""
    number=""
    message=""
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-i", "--ipaddress"):
            ipaddress = arg
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-n", "--number"):
            number = arg
        elif opt in ("-m", "--message"):
            message = arg
            
    with session() as c:
        response = c.get('http://' + ipaddress + '/log/in?un=' + username + '&pw=' + password + '&rd=%2Fuir%2Fstatus.htm&rd2=%2Fuir%2Fwanst.htm&Nrd=1')
        response = c.get('http://' + ipaddress + '/smsmsg.htm?Nsend=1&Nmsgindex=0&S801E2700=' + number + '&S801E2800=' + message )
        response = c.get('http://' + ipaddress + '/sms2.htm?Ncmd=2')

if __name__ == "__main__":
   main(sys.argv[1:])
