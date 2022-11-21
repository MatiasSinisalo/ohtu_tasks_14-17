*** Settings ***
Resource  resource.robot
Test Setup  Create NewUser

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input  matti
    Input  matti123
    Run Application
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input  new
    Input  kalle
    Input  matti123
    Run Application
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...




*** Keywords ***
Create NewUser
    Create User  kalle  kalle123

