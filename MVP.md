

# The MVP

The name of my crowdfunding site is The Honeymooners. The honeymooners is a honeymoon crowdfunding site.

![img](images/Yellow%20and%20Blue%20Beach%20Resort%20Logo.png)

## Purpose

A crowdfunding site where newlyweds graciously ask their friends, family and generous pledgers to assist in saving for a honeymoon to the their dream destination. 


## Key Features

Features

- Create a user account
- To RSVP to means you make a pledge and to decline is if don’t want to RSVP to the event
- Delete user account and pledge
- Ability to pledge money to the couple's honeymoon
- Ability to track the number of pledges and who they came from

API  features

-	Information on all the pledges
-	Information on all the projects
-	Find user information and details on their bio
-	Login URL for all new users to login 
-  Create User account

Additional feature

-	If you want to invite a guest and them leaving a note via the invitation 
-	User being able to like projects 


| Endpoint URL | Action         | HTTP Method | Authorisation     |
| ------------ | -------------- | ----------- | ----------------- |
| /users/      | List all users | GET         | Must be logged in |
| /users/      | Create user    | POST        | N/A               |
| /users/      | Get user info  | GET         | Must be logged in |
| /users/      |Delete user info| Delete      | Must be logged in |
| /users/      | Update existing instance|PUT | Must be logged in |
| /project/    | Create project | POST        | Must be logged in |
| /project/    | Create project | GET         | Must be logged in |
| 

## Database Schema

The database schema features 3 classes that we will be working with the User, the pledges and the projects as seen below.

![Alt text](images/UML%20class%20diagram.png)


## Wireframes

Please see below a wire frame of what the The HoneyMooners

![Alt text](images/Wireframe.png)

## Colour Scheme

Chose color scheme accents of yellow, blue and navy as seen below.

![img](images/Colour%20scheme.png)

## Heading and body font's

Font: Roboto Mono

Regular 400 at 21px

https://fonts.google.com/specimen/Roboto