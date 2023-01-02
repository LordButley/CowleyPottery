# Testing

## HTML

This [HTML Validator](https://validator.w3.org/nu/) was used to check the following pages of the website:
- Homepage
- Game pages
- Post pages
- Login
- Register

Pages that require the user to be logged in such as the logout page can unfortunately not be check with this tool. 

All warnings came from missing opening and closing tags and were resolved. The following warning was left

![htmlvalidatorwarning](media/readme/htmlvalidator.JPG)

This arrises from using Font Awesome within an element and nothing else and so can safely be left.

## CSS

This [CSS Validator](https://jigsaw.w3.org/css-validator/validator) was used to check the CSS of the website via manual upload of the CSS file. No errors were found

## Python

The [Code Institute Python Validator](https://pep8ci.herokuapp.com/) was used to manually input each python file.

All errors except 1 type were removed. These errors were in the form "Class 'Classname' has no 'objects' member". These have been left as it is due to pylint not being capable of picking up the inheritance of objects in models.

## User Story Testing

User story testing was completed on the following completed user stories:

* As an unregistered user I can view each post on the website so that I can select one to read and decide whether to sign up
   - In incognito mode, I travelled to each Game page and then each post page to verify that you could access without logining in

* As a user I can navigate intuitively so that I can view the desired content
   - The navigation bar at the top was viewed across different screen sizes to ensure that all parts were still visible
   - The links were all used to see if they worked correctly
   - There is feedback on every navigation button when hovered over

* As an admin I can create, remove, update or delete posts so that I can ensure site content is relevant and inoffensive
   - CRUD functionality tested and all works.
   - Attempts to by pass the need to be logged in were made by using URLs and incognito mode. Create post was still possible whereas others were not. This has been patched.

* As an Admin I can log out of the admin panel so that I can disconnect from the website
   - Login and logout tested and fully functional.

* As an admin I can log in so that I can access the sites backend
   - Login and logout tested and fully functional. The backend is also viewable and organised.

* As a user I can access social media accounts connected to the website so that I may learn more about the company
   - Social media links tested and all open the necesssary external page.
   - All links open on a new page

* As a user I can quickly identify the purpose of the website from the landing page so that determine if the website is relevant to me
   - Website is in keeping with industry norms for similar sites.
   - Upon seeing the landing page, there is sufficient and easy to read information available to quickly determine the sites content.

* As a registered user I can login and logout of my account so that I can access and keep secure my data
   - Login and logout tested and fully functional. The backend is also viewable and organised.

* As an unregistered user I can create an account so that I can interact fully with the website
   - User is able to register which gives them access to posting and commenting functionality 

* As an unregistered user I can easily find the sign up page so that I can register and interact with the website
   - The sign up page is constantly visible in the top right hand side of the page
   - The sign in status is also constantly visible in the top right hand side of the page

* As a registered user I can comment on posts so that I can connect with other gamers
   - Users are able to comment on posts
   - Unregistered users are unable to comment on posts

* As a registered user I can delete my posts so that my post are no longer visible and I will receive no further messages
   - Users are able to delete their owns posts
   - Users are not able to delete the posts of others
   - Unregistered users are unable to delete posts

* As a registered user I can update my posts so that I can keep my posts relevant and up to date with information
   - Users can update posts that they created
   - Users cannot update the post of others
   - Unregistered users cannot access this functionality
   - When updating a post, the original post is presented to the user in the text box.

* As a registered user I can create posts so that I can find other gamers who want to achieve the same things
   - Users can create posts
   - Unregistered users are able to access this functionality

* As a user I can easily see if I am logged in or not so that I can choose to login or logout depending on what I want to do
   - Login status can be found in the top right of the screen at all times.

## Manual Testing 

I have robustly tested the deployed and local application completing the following actions and ensuring the correct outcome is received on both:

* Navigation - Repeated steps on all pages
    
    * Click on the logo across all pages to ensure that is returns to the home page
    * Clicked each game on the menu to see if it directs to the right page.
    * Complete the above check on each page of the game to see if their are any glitches that are page specific.
    * Log in, register and log out buttons redirect to the correct page.
    
* Input and error handling - Repeated steps on all input sections.
    * Login, Logout, Register - Attempted to leave fields blank as well as overfilling
    * Create post - Attempted to leave fields blank as well as overfilling
    * Create comment - Attempted to leave fields blank as well as overfilling

* Authentication
    * Check that I can create post whilst logged in
    * Check that I can edit post whilst logged in
    * Check that I can delete post whilst logged in
    * Check that I can comment whilst logged in
    * Check that I can delete comment whilst logged in
    * Check that there is no button for me to create, edit or delete posts whilst not logged in
    * Check that there is no button for me to create or delete comments whilst not logged in
    * Check that there is no button for me to edit or delete posts or comments that other users made whilst I am logged in.
    * Check that I cannot access any of the above functionality using URLS
    
* Login/Logout/Registration
    * Tested logging in and logging out
    * Registration is working as expected

* Design and responsivity
    * All pages were visited and viewed across all different view ports.
