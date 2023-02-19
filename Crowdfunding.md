#  The Honeymooners

![img](images/Yellow%20and%20Blue%20Beach%20Resort%20Logo.png)

​
### The honeymooners is crowdfunding site where newlyweds graciously ask their friends, family and generous pledgers to assist in saving for a honeymoon to the their dream destination. On the site users are able to create register as users of The Honeymooners and create crowd funding projects and pledge. Users are also able to delete their projects if the choose to, only registered users of the specific project can close a crowdfunding project.
​
## Features
​
### User Accounts
​
- [X] Username
- [X] Email Address
- [X] Password
- [X] Bio
- [X] Image
- [X] Date created
​
### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fund raise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
  - [X] Ability to pledge to a project
  

### Pledge
  
  - [X] An amount
  - [X] A comment to go with the pledge
  - [X] Whether the pledge is anonymous
  - [X] The project the pledge is for
  - [X] The project supporter
  


​
- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
  
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy (Once a project is destroyed the pledge associated with that project is cancelled)
  
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [x] Limit who can create
  - [x] Limit who can retrieve
  - [x] Limit who can update
  - [x] Limit who can delete
- Pledge
  - [x] Limit who can create
  - [x] Limit who can retrieve
  - [x] Limit who can update
  - [x] Limit who can delete
- Users
  - [x] Limit who can retrieve
  - [x] Limit who can update
  - [x] Limit who can delete
​
### Implement relevant status codes
​
- [x] Get returns 200
- [x] Create returns 201
- [x] Not found returns 404
​
### Handle failed requests gracefully 
​
- [x] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] implement /api-token-auth/

### Implement suitable update delete

![img](images/del%20function.png)
​
## Additional features
​
- [ ] Ability to search and filter by Project title
​
- [ ] Like functionality
​
​
​
### External libraries used
​
- [ ] django-filter
  This would be an additional functionality
​
​
## Part A Submission
​
- [ ] A link to the deployed project.

  https://twilight-glade-9528.fly.dev/users/
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.

![img](images/Get%20function.png)

- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
  
![img](images/Put%20function.png)
- [ ] A screenshot of Insomnia, demonstrating a token being returned.

![img](images/token.png)
- [ ] Your refined API specification and Database Schema.
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "Rea",
	"email": "Rea@myemail.com",
	"password": "not-my-password",
  "bio": "Hi Im Rea",
  "image": ""https://via.placeholder.com/300.jpg",
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "Rea",
	"password": "not-my-password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate to our Dream wedding",
	"description": "We had a hard time saving up for our wedding since covid because of health issues.We decided to sign and getting married in court. Please help us have our dream honeymoon to celebrate our love",
	"goal": 1,
	"image": ""https://via.placeholder.com/300.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
```

### Refined API specification and Database Schema!

![img](images/refined%20DB%20schema.png)


## Part B Submission

- Link to GitHub repository
  
  https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-ReaNtumba.git

- Link to deployed project

  http://127.0.0.1:8000/users/

- A screenshot of the homepage
 
  ![img](images/Deployed_project.png)

- A screenshot of a project with pledges
  ![img](images/Deployed_pledge.png)

- A screenshot of the resulting page when an unauthorized user attempts to edit a project
  

