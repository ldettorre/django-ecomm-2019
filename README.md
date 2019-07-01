# Obaju  E-Commerce Store
[![Build Status](https://travis-ci.org/ldettorre/django-ecomm-2019.svg?branch=master)](https://travis-ci.org/ldettorre/django-ecomm-2019)

## Fullstack Frameworks with Django Project - Code Institute  
###### This project is intended for educational purposes only.


Obaju is an fictional e-commerce site built as part of my course work with Code Institute. This site in particular is our Fullstack Frameworks project which gives us the opportunity to utilize everything we have learned on the course from the foundation of HTML, the implementation of a frameworks and databases, and everything in between. To help with styling, I decided to use a template. I chose [Obaju - ecommerce template](https://bootstraptemple.com/p/obaju-e-commerce-template) as it was very comprehensive and fit my needs.

To view the live version of this site, click [here!](https://e-comm-2019.herokuapp.com/)

## UX and UI

My original intention behind this e-commerce project was to create it in such a fashion where any indiviual needing an e-commerce site could take it as a template and add their own imagery, style and settings as needed. It was also my intention to have this as a base application to build upon over time and have as a product to sell for small businesses. Before beginning the project I imagined the User Interface being light and simple and the User Experience being quite vanilla. The trade off I was aiming for was that by following my initial idea, the site would be easily useable on all smart devices and style of computer as well as extremely reliable by not having a ton of unnecessary flashy features that may not work across different browsers. Ultimately there would be less maintenance across the entire app by having a limited set of technologies being used in conjuction with each other.

As the site developed and I passed the 'walking skeleton' stage, I realised that even a template should have some styling or a theme. So to help with giving the project more life I took inspiration from the layout of my favourite clothing sites [Superdry](https://www.superdry.ie/) and [Diesel](https://www.diesel.ie/) and married that with the template from [Obaju - ecommerce template](https://bootstraptemple.com/p/obaju-e-commerce-template).  The result ended up being a basic but functional layout that isn't filled with distracting features but has plenty of space to grow into. From the UX perspective it is still missing some information you'd find standard on other e-commerce sites could do with more information presented in the current layout, this is to benefit the user



### Technologies Used For This Project
* HTML
* CSS
* Bootstrap Version 3.3.7
* Javascript and Jquery
* Font-Awesome
* Google Fonts
* Python 3.4.3
* Django 1.11 Framework
* Heroku - Deployment
* SQLite Database
* Stripe
    * For processing payments.
* Balsamiq 
    * For creating wireframes. These can be found in the Wireframes folder.

## Features

### Existing Features

###### Site Specific:
* The site is responsive through it's use of Bootstrap.
* The site automatically adds a delivery charge of €15 on orders above €50
* The site has the core feature implemented already for sending emails. Currently this is done for the password reset feature.
* The site requires that users be logged in before making purchases.

###### As the Site Admin:
* You can create products with a name, description, price, image, category and 'new in' field.
* You can mark products as "new in" which renders them to the customer collectively regardless of category.
* You can view contact forms submitted by the customer which contains their name, phone number, email, and the time/date of their submission.
* You can search for contact form submission by name, phone number and email.
* You can view current registered user information as well as the date they signed up.
* You can search for current registered users by username and email.
* You can create categories with ease which will be automatically rendered to the app navbar.
* You can view order information of users and search for orders by name, contact number and date.
* You can take payments through Stripe.


###### As a customer:
* You can browse products by category.
* You can submit a contact form asking for further information without needing to be registered.
* You can create a profile account.
* You have access to a standard 'Forgot My Password' feature.
* You can create a shopping cart of items without needing to be registered.
* I can see a breakdown of my order on quantity, unit price and any extra delivery charges if applicable.

### Features Left to Implement
In the Accounts app, with users being able to easily create an account, log in and log out,  I could work on saving a users previous purchase history and contact form submission for their own reference.

In the Products app would also like to further develop the category and product models to implement more fields such as gender, size options and added images for an improved UX.

In future, I would like to implement a Blog app which would add more value to the user when visiting the site for a browse. The Blog app could benefit from the Accounts app by identifying users and granting them certain permissions with posts such as commenting on all but only editing their own comments to name a few.

With regards to the existing emailing functionality, this would be a good base to add in an email confirmation/invoice feature to notify users of further details.

In the Checkout app I would like to develop the delivery logic more allowing the user to choose a range of different delivery options and whatever is chosen would be representing on their order model.


## Deployment and Hosting
Deployment of this site was done by creating a free Heroku account and creating a new app. Once this was done, I navigated the Heroku app tabs at the top of the page and performed the following:
* Deploy > Deployment method > GitHub.
* App connected to GitHub > Connected to my chosen project app.
* Resources > Addon > Selecting Heroku Postgres FREE TIER.
* Settings > Config Vars > Reveal Config Vars > Set up appropriate environment variables based on the prod.py file in the settings folder of the app.

The static files are hosted on AWS S3 using a bucket with custom user and permissions.

### Running Locally
To get this project running locally, you will need to clone the repository and install the requirements.txt file. Following that, you must ensure all secret keys within the ecommerce.settings.base are set up either in an env.py file or using the .bashrc. For the likes of the Email feature and Stripe payments, you will need to obtain your own keys and place them in the app. Also be sure to have your allowed hosts updated with the address returned in the error message upon first running the app.



## Testing
To test this project I did a mixture of manual testing and incorporated Travis C.I. When it came to manually testing, I checked that:

* All the links on the site redirected as expected.
* The contact form correctly submitted it's information to the admin dashboard.
* Users who 'purchased' products had their information submitted to the admin dashboard.
* Users could successfully register new accounts and once created they could easily log in and out with ease.
* The Admin could create new categories with ease and create new products. These products were filtered and rendered to their template as expected.
* The password reset feature correctly emailed the address I registered with and I was able to successfully reset my password. Although this did bring 
    me to the django template it still functioned as expected.

For synthetic testing, I used Chrome Dev Tools for responsiveness. I found that the deployed site was responsive across it's entirety. It is worth mentioning that the cart view and order summary do have a horizontal scroll but only on the items and not on the page. This is acceptable given the information being displayed is important but also it doesn't break the site or impact it negatively.

For testing with Travis, I created 19 tests across the Accounts and Products app. These tests passed giving me some 90~% coverage for Products App and 76% coverage for Accounts App. You can check out the current build [here](https://travis-ci.org/ldettorre/django-ecomm-2019). The reason for the high build log is due to dealing with a bug in the manage.py file that turned out to be nothing more than a space between the ! and # in line one.


## Remaining Issues
At the moment the site has alot of unnecessary CSS and scripts due to it being taken from a template which will need to be cleaned up.  Also the confirmation message is only functioning upon successfully paying for your items and not for the contact form submission. 

Where datetime is used with regards to the models, it is an hour ahead of Irish Time. This is not major at the moment but something to look at for future revisions.

For an unknown reason when I set DEBUG to False it still returns error messages. I currently have the config vars set up as expected so this will require more attention as it is a security issue.


### Credits

## Acknowledgements
I want to thank [Michael Park](https://github.com/mparkcode) for introducing me to context processors and helping me with creating categories for the Products app. 
I also want to thank [Haley Schafer](https://github.com/hschafer2017) for helping me debug my database migration issues and Travis errors.

## Content
The second carousel on the landing page are images of a YouTuber named [Alex Costa](https://www.youtube.com/user/xMadeInBrazil). I do not own these images.

The template used is from [Bootstrap Temple](https://bootstraptemple.com/p/obaju-e-commerce-template)

All product images and information was taken from [Superdry](https://www.superdry.ie/).


