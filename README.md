# README #

### Author: Harpreet Dhillon, harpreet@uoregon.edu ###

---

### Purpose ###
* This application is for Project 7 of CIS 322 at University of Oregon.
* The purpose was to get an introduction with Google's Calendar API.
* This is a mini-project that displays all the busy times within a given date/time range.

### Application Specifics ###
* The main [index](/templates/index.html) displays all the calendar information
* Necessary files (files not included in the repository):
  * secrets/admin_secrets.py
    * `google_key_file="PATH_TO_YOUR_google_client_key.json"
    * The google_client_key.json can be obtained by following [this guide](https://auth0.com/docs/connections/social/google)

### Running the Application ###
* Test deployment to other environments including Raspberry Pi.  Deployment 
  should work "out of the box" with this command sequence:
  * `git clone <yourGitRepository> <targetDirectory>`
  * `cd <targetDirectory>`
  * `./configure`
  * `make run`
  * (control-C to stop program)
* The default port is 5000, so the webserver should be reachable at http://localhost:5000 , and also through its IP address.
 
### Testing the Application ###
* There are no tests for this application.
