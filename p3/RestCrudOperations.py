#! /usr/bin/env python

"""
Description: Module which performs the REST Operations like Get, Post, Delete, Put
"""

from requests.auth import HTTPBasicAuth

import requests
import urllib3


class RestAPIClient:
    """
    Description: This class Initializes the restclient Object
    """

    def __init__(self, username=None, password=None):
        """
        Description: Initialization of RestAPIClient class
        Parameters: username - User name to use when connecting to host (STRING)
                    password - Password to use when connecting to host (STRING)
        """
        # setting the basic authentication
        self.auth = HTTPBasicAuth(username, password)
        self.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get(self, url, headers=None, auth=None, **kwargs):
        """
        Description: This method contains handler for RestAPIClient GET call.
        Parameters: url         - Complete location url path for running for REST call(STRING)
                    headers     - (OPTIONAL) Content-Type: application/(json/xml)
                    kwargs      - (OPTIONAL) parameters used in REST request.
        Returns: Response object
        """
        # get api call of requests module
        responseData = requests.get(url=url, headers=headers, auth=auth, verify=self.verify, **kwargs)
        return responseData

    def post(self, url, headers=None, auth=None, **kwargs):
        """
        Description : This method contains handler for RestAPIClient POST call.
        Parameters  : url         - Complete location url path for running for REST call (STRING)
                      headers     - (OPTIONAL) Content-Type
                      kwargs      - (OPTIONAL) parameters used in REST request like Payload data
        Returns     : Response object
        """
        # post api call of requests module
        responseData = requests.post(url=url, headers=headers, auth=auth, verify=self.verify, **kwargs)
        return responseData

    def put(self, url, headers=None, **kwargs):
        """
        Description : This method contains handler for RestAPIClient PUT call.
        Parameters  : url         - Complete location url path for running for REST call (STRING)
                      headers     - (OPTIONAL) Content-Type
                      kwargs      - (OPTIONAL) parameters used in REST request.
        Returns     : Response object
        """
        # put api call of requests module
        responseData = requests.put(url=url, headers=headers, verify=self.verify, **kwargs)
        return responseData

    def delete(self, url, headers=None, **kwargs):
        """
        Description : This method contains handler for RestAPIClient DELETE call.
        Parameters  : url       - Complete location url path for running for REST call (STRING)
                      headers   - (OPTIONAL) Content-Type
                      kwargs    - (OPTIONAL) parameters used in REST request.
        Returns     : Response object
        """
        # delete api call of requests module
        responseData = requests.delete(url=url, headers=headers, verify=self.verify, **kwargs)
        return responseData


print('This file is written in Python 2 for migration')
