# Testing

## HTML

This [HTML Validator](https://validator.w3.org/nu/) was used to check the following pages of the website:
- Homepage
- Game pages
- Post pages
- Login
- Register

Pages that require the user to be logged in such as the logout page can unfortunately not be check with this tool. 

All warnings came from missing opening and closing tags and were resolved. 

## CSS

This [CSS Validator](https://jigsaw.w3.org/css-validator/validator) was used to check the CSS of the website via manual upload of the CSS file. No errors were found


## User Story Testing

User story testing was completed on the following completed user stories:

* As a customer I can view a list of products so that I can identify what products are available and view their images.
   - I can view all products on the shop in all device sizes using the All items button

* As a customer I can view individual products so that I can learn more about the item such as price, description, and quantity available.
   - Individual product links have been tested as well as the direct urls.
   - All products contain a price, description and quantity.

* As a customer I can quickly identify and traverse the website so that I can reach the desired part of the website.
   - Navbar is visible on all pages
   - All navbar links have been tested.

*  As a customer I can quickly identify new stock so that I can purchase before it sells out.
   - New stock filter has been tested and works correctly
   - New items are added to test whether their date added is correct
   - I have printed out this date to template to triple check

* As a customer I can always see the shopping basket total so that I can be aware of how much money I am spending.
   - Shopping bag is visible in the navbar at all time and across all screens.

* As a customer I can view information regarding the business so that I can learn more about the artist who makes the items.
   - An about me page has been created and has been tested across all viewport sizes

* As a customer I can create an account so that I can Store personal details, view purchases and view my profile.
   - Users can create profiles
   - User have the option to save details after purchase
   - Users can view their personal details and order details on their account.

* As a customer I can receive a registration confirmation email so that I can tell whether my account registration was successful.
   - Email registration confirmation email functionality has been tested and email received correctly.

* As a customer I can recover or reset my password so that I can regain access to my account.
   - Functionality tested and working as expected

* As a customer I can sign in using credentials so that I can gain access to my account whilst knowing that it is safe.
   - Password functonality working as expected

* As a customer I can log out of my account so that I can secure my account.
   - Log out functionality has been tested from each page and with different bag contents

* As a customer I can view products by category so that I can quickly view items of a particular type.
   - Category buttons have each been tested, both the tiles and the icons. All works as expected

* As a customer I can sign up for a newsletter so that I can keep up to date with stock changes.
   - Mail chimp newsletter functionality has been tested

* As a customer I can view the shopping basket so that I can identify what is to be purchased and its total cost.
   - User can navigate to the shopping basket view. Items have been added to test that the shopping bag holds items correctly. 
   - Shopping bag buttons have been tested and work correctly.

* As a customer I can add items to shopping basket so that I can purchase them.
   - Items can be added and the shopping bag total adds up correctly

* As a customer I can edit items in the shopping basket so that I can alter quantity of items in basket.
   - Items can editted and the total adds up correctly

* As a customer I can pay for items so that I can buy the item.
   - Payments are processed correctly through Stripe for the correct amount

* As a customer I can feel that my personal and payment information is safe and secure so that I can confidently provide the information needed to make a purchase.
   - Accounts are locked via password authentication.

* As a customer I can see an order summary so that I can check my order before I click "pay now".
   - Customers are able to see a view of their order before they buy

* As a customer I can receive an email receipt so that I can have evidence of my purchase.
   - Multiple purchases have been made and the emails work correctly.

* As a shop owner I can delete products through the admin site so that I can delete items.
   - Shop owner can delete through the admin site as well as through the front end as a superuser

* As a shop owner I can add products through the admin site so that I can add new items.
   - Shop owner can add new items through the admin site as well as through the front end as a superuser

* As a shop owner I can edit products through the admin site so that I can change item prices, images and descriptions.
   - Shop owner can edit items through the admin site as well as through the front end as a superuser


## Manual Testing 

I have robustly tested the deployed and local application completing the following actions and ensuring the correct outcome is received on both:

* Navigation - Repeated steps on all pages
    
    * Click on the logo across all pages to ensure that is returns to the home page
    * Clicked each link on the menu to see if it directs to the right page.
    * Log in, register and log out buttons redirect to the correct page.
    
* Input and error handling - Repeated steps on all input sections.
    * Login, Logout, Register - Attempted to leave fields blank as well as overfilling
    * Create product - Attempted to leave fields blank as well as overfilling
    * Create commission - Attempted to leave fields blank as well as overfilling

* Authentication as superuser
    * Check that I can create products whilst logged in
    * Check that I can edit products whilst logged in
    * Check that I can delete products whilst logged in
    * Check that there is no button for me to create, edit or delete products whilst not logged in
    * Check that I cannot access any of the above functionality using URLS
    
* Login/Logout/Registration
    * Tested logging in and logging out
    * Registration is working as expected

* Email
   * Email successfully received upon signing up to newsletter
   * Email successfully received after purchasing item
   * Email check successfully received after registering.

* Design and responsivity
    * All pages were visited and viewed across all different view ports.

## Bugs

TESTING

 

* On the Sign Out page, the text and Sign Out button are too close the page margin on the left.
 - Fixed by moving the text and Sign Out button to the centre of the page.

 

* On the Splash page, the text is not easily readable as it clashes with the background image.
 - Fixed by putting the text in a header at the top of the page with an opaque background.

 

* On the footer, on the Join our newsletter section the text *indicates required is not necessary when subscribing to the newsletter because this information is already shown to the users if they click the subscribe button without entering an email address.
 - Fixed by removed this line from the newsletter sections.

 

* The shopping basket icon appears in a bright blue colour.
 - Fixed by changing the colour of the icon to black to match the rest of the text. The icon will only appear in blue if the user is hovering over it.

 

* On the Basket page, when the basket is empty, the Keep Shopping button does not have any spacing under it.
 - Fixed by adding space under the Keep Shopping button.

 

* On the Shop page, the black square with text is covering the images
 - Fixed by adding more transparency so that it allows users to see the full image below in any screen size.

### "Attempting to break the website" tests

-       Tested creating an account and activating the account via the link on the confirmation email – OK

-       Login after account activation – OK

-       Login attempt with incorrect password or email address shows the expected error message – OK

-       Adding products to bag worth more than £100 removed the shipping costs – OK

-       Order summary showing correctly – OK


-       Tested declined payments with test cards – OK

-        Decline error messages show correctly according to the decline card that was being used – OK

-       Successful payment with test card – OK

-       When payment is complete an order confirmation page is shown – OK

-       Order confirmation email is sent to the email address entered – OK

-       Previous orders are visible and accessible on the user’s profile page - OK
