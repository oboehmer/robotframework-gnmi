# Robotframework Keywords for GNMI Client

Simple robotkeywords wrapper for [pygnmi]( https://github.com/akarneliuk/pygnmi) GNMI library. At the moment, only GNMI client is supported.

At the moment, we just expose the attributes of `gNMIclient.__init__`, `gNMIclient.get` and `gNMIclient.set` as robot keywords

## Installation

```
pip install -U pip wheel
pip install git+https://github.com/oboehmer/robotframework-gnmi.git
```

## Example ##

Example robot file 

```
*** Settings ***
Library   GNMI

*** Variables ***
@{target_host}    192.168.1.1   5400   

*** Test Cases ***
Connect and Get

    GNMI connect session   MySession    target=@{target_host}    username=admin    password=password    insecure=True
    @{path}=   Create List   openconfig-interfaces:interfaces
    ${result}=   GNMI get    MySession  path=@{path}   encoding=ascii
