
import sys
from urllib import response
import requests
from http.client import responses
from time import sleep
import urllib
import validators
import csv
import socket
import dnspython as dns
import dns.resolver
from tld import get_tld


COLUMN_HEADERS = [
    "Domain Name",
    "Apex"
]

COLUMN_HEADERS_ERROR = [
	"Domain Name",
	"Error",
	"Comment"
]

data = {}
data_error = {}

with open('domains.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        apex_value = "NONE"
        domain = ' '.join([str(elem) for elem in row ])
        res = get_tld(domain, as_object=True)
        if res.fld:
            apex_value= res.fld
        data[domain] = [apex_value]


with open("response-domain-tld.csv", "w") as out_file:
        csvWriter = csv.writer(out_file, lineterminator="\n")
        csvWriter.writerow(COLUMN_HEADERS)
        for data_per_domain, value in data.items():
            csvWriter.writerow([data_per_domain, value[0]])
