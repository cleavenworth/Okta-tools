#!/usr/bin/env python

import csv
import requests

## Okta API Info
API_TOKEN = "OKTA_API_KEY"
OKTA_DOMAIN = "https://YOURDOMAIN.okta.com/"
GROUP_API_BASE = "api/v1/groups"

## CSV Info
CSV_FILE = "group_export.csv"
CSV_HEADERS = ['okta_id', 'email']

## Okta Group IDs
GROUP_ID = "OKTA Group ID Here"


## Request Headers
AUTH_HEADERS = {'content-type': 'application/json',
                'Authorization': 'SSWS ' + API_TOKEN}

def get_group_members(group_id):
    """Retrieves all members of the specified group in Okta"""
    search_group_id = group_id
    list_users_url = GROUP_API_BASE + "/" + search_group_id + "/users"
    group_members = requests.get(OKTA_DOMAIN + list_users_url, headers=AUTH_HEADERS).json()
    return group_members

def build_csv(group_json, csvfilepath):
    with open(csvfilepath, "w+") as csvfile:
        out = csv.writer(csvfile)
        out.writerow(CSV_HEADERS)
        for member in group_json:
            okta_id = member['id']
            email = member['profile']['email']
            out.writerow([okta_id, email])


build_csv(get_group_members(GROUP_ID), CSV_FILE)
