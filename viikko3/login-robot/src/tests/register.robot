*** Settings ***
Resource  resource.robot
Test Setup  Create NewUser

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input  matti
    Input  mat123ti
    Run Application
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input  new
    Input  kalle
    Input  matti123
    Run Application
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input  new
    Input  k
    Input  matti123
    Run Application
    Output Should Contain  Username should be at least 3 characters long


Register With Valid Username And Too Short Password 
    Input  new
    Input  matti
    Input  m2
    Run Application
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  new
    Input  matti
    Input  testitesti
    Run Application
    Output Should Contain  Password should contain at least 1 number





*** Keywords ***
Create NewUser
    Create User  kalle  kalle123

