# <div align="center">The Halal Butcher</div>

## Project Overview

The Halal Butcher is a full-stack Django website built using Python, JavaScript, HTML and CSS. This web application is a full B2C e-commerce website for a fictional online Halal meat supplier based in the North West of England. The Halal Butcher specialises in selling and delivering the finest quality of meats such as beef, chicken, lamb, sheep & more to users who want to enjoy these cuts with their family and friends. The site provides users with different functionalities that eases the process of purchasing a product. Users of the site can browse all products, filter products by diverse categories and also search for specific products by keyword search. From the list of products, users can select them to display each product in detail, giving users the option to add the product to their basket or return to the product list page to browse other meats. Users are also able to view the website blog to view all the latest & updated information on on The Halal Butcher. Registered users can add the product to their wishlist or a leave a review for other users to view. Authenticated users can also checkout securely inputting their personal & payment details to purchase the product and also store these details on their profile for easier future purchases. On the other hand, The Halal Butcher provides the store owner with functionalities such as product management (add, edit & delete products) without accessing the admin interface and blog post management (add, edit & delete blogs).

This website application includes CRUD functionality, user authentication (using Django's allauth library), email validation and database interaction.

[View the live website on Heroku](https://halal-butcher.herokuapp.com/)

## Table of Contents

## UX & Planning

### The Strategy Plane

#### Overall Project Goals
    - To provide a B2C e-commerce platform, selling meat products to consumers.
    - To provide users different functionalities such as user authentication, product purchase, reviewing products and wishlist/basket management. 
    - To provide the store owner the ability to manage the site to update products and information via the blog feature.

#### Target Audience
    - Users who love enjoy consuming diverse meat products.
    - An audience that consume Halal meats.
    - Users that prefer to purchase their meats online rather than visiting the butchers shop.

#### Site Owner Goals
    - Build a platform that has an intuitive user interface to provide users to easily navigate the website.
    - To promote products that are listed on the e-commerce website.
    - To provide users with a platform to purchase quality Halal meats.
    - To provide competition in the meat supplier market.

### The Scope Plane

#### Agile Methodology

#### Epics

13 Epics were created as basis to further make 42 User Stories. The project kanban board that was created to list these Epics & User Stories can be visited on this link [here](https://github.com/legenduzair/the-halal-butcher/projects/2). These Epics are detailed below:

1. Initial Django Setup [#1](https://github.com/legenduzair/the-halal-butcher/issues/1) - As a **developer**, I can **setup the Django environment** so that **I can begin development of my Django project**.
    
    **Potential User Stories Included:**
    - Create Django Project
    - Install Django Libraries required
    - Create admin superuser
    - Create first app
    - Initial Deployment

2. Creating Base Template & Configuring Home App [#2](https://github.com/legenduzair/the-halal-butcher/issues/2) - As a **developer**, I can **create templates & stylesheets for the base and configure the home app** so that **the user can navigate around the website with ease**.

    **Potential User Stories Included:**
    - Creating base template and stylesheets
    - Configuring the Home app
    - Creating the navigation templates

3. Allauth setup [#3](https://github.com/legenduzair/the-halal-butcher/issues/3) - As a **developer**, I would **like to setup the Django authentication library - allauth** so that **my user audience has the option to register, sign in and sign out of their accounts for advanced permissions**.

    **Potential User Stories Included:**
    - Register a user account
    - Sign in to user account
    - Sign out from user account

4. Configuring Products App [#4](https://github.com/legenduzair/the-halal-butcher/issues/4) - As a **developer**, I would **like to create and configure the products app** so that **the user audience can view, search for and click on**.

    **Potential User Stories Included:**
    - View product list
    - View products in detail with summary information
    - Search for a specific product
    - Filter through to acquire a specific product

5. Configure Wishlist App [#5](https://github.com/legenduzair/the-halal-butcher/issues/5) - As a **developer**, I would **like to incorporate a wishlist app** so that **the user audience can add & remove products to & from their wishlist**.

    **Potential User Stories Included:**
    - Add product to wishlist
    - View product detail from wishlist
    - Remove product from wishlist

6. Configure Shopping Bag App [#6](https://github.com/legenduzair/the-halal-butcher/issues/6) - As a **developer**, I would **like to create a shopping bag app** so that **the user audience can control the products that they want to purchase**.

    **Potential User Stories Included:**
    - Add product to cart
    - View product in cart
    - Edit product in cart
    - Remove product from cart
    - Proceed to checkout

7. Configure Checkout App [#8](https://github.com/legenduzair/the-halal-butcher/issues/8) - As a **developer**, I would **like to create and configure a checkout app** so that **the user audience can place their order and successfully pay with their payment details**.

    **Potential User Stories Included:**
    - Add delivery & billing details
    - Save details to profile
    - Add payment details when going through checkout
    - Authorise payment details
    - Order confirmation with order details

8. Configure Profile App [#9](https://github.com/legenduzair/the-halal-butcher/issues/9) - As a **developer**, I would like **to create a profile app** so that **the user audience can view their order history and have saved delivery & personal details so that they can order quickly again**.

    **Potential User Stories Included:**
    - Create user profile
    - Edit and save personal information on user profile
    - View order history

9. Product Management [#10](https://github.com/legenduzair/the-halal-butcher/issues/10) - As a **developer**, I would **like to integrate product management to my project** so that **as a site owner, I am able to manage the products on the site easily and keeping the site up to date**.

    **Potential User Stories Included:**
    - Add products
    - Edit products
    - Delete products

10. Final Deployment [#11](https://github.com/legenduzair/the-halal-butcher/issues/11) - As a **developer**, I can **setup the final deployment** so that **my project is deployed properly**.

    **Potential User Stories Included:**
    - Creating and Configuring Heroku App
    - AWS setup
    - Final caching or code refactoring

11. Product Reviews - [#12](https://github.com/legenduzair/the-halal-butcher/issues/12) - As a **developer**, I would **like to incorporate product reviews** so that **the user audience can post reviews of products on the website which will be detailed on product detail page**.

    **Potential User Stories Included:**
    - Add product review
    - Read product review
    - Edit product review
    - Delete product review

12. Web Marketing - [#13](https://github.com/legenduzair/the-halal-butcher/issues/13) - As a **developer**, I would **like to incorporate web marketing to my project** so that **I stay up to date with the company easily**.

    **Potential User Stories Included:**
    - Create an email newsletter signup using Mail Chimp
    - Create a Facebook page for the company

13. Configure Blog App - [#51](https://github.com/legenduzair/the-halal-butcher/issues/51) - As a **developer**, I would **like to create & configure a blog app** so that **the user audience can browse through the latest information & news supplied by the company**.

    **Potential User Stories Included:**
    - View blog entries list
    - View blog entries in detail
    - Add blog entry
    - Update blog entry
    - Delete blog entry

#### User Stories

Each Epic has individual potential User Stories that have been created and followed when developing the code of the web application. From the 13 Epics, 42 User Stories were created. Each one was assigned story points based on the estimation of difficulty & time taken to create the feature and a category of either 'Must Have', 'Should Have', 'Could Have', 'Won't Have'. There were a total of 180 story points from all of the User Stories from which 168 story points were completed and 12 were incompleted. Due to personal reasons & time restraints, these unfinished story points will be completed and added into the project as future implementations, improving the web application for users. All of the User Stories along with their categories can be found [here](https://github.com/legenduzair/the-halal-butcher/projects/2).

Below are the User Stories that were completed within the project's first release:

1. Initial Django Setup:
    - [#14](https://github.com/legenduzair/the-halal-butcher/issues/14) - As a **Developer**, I can **setup Django by installing the appropriate libraries, creating the admin superuser and create my first app** so that **I can initiate development**.
    - [#15](https://github.com/legenduzair/the-halal-butcher/issues/15) - As a **developer**, I want **to setup the Django environment secret keys in an env.py file/Gitpod settings** so that **I do not expose the keys in an insecure fashion**.

2. Creating Base Template & Configuring Home App:
    - [#20](https://github.com/legenduzair/the-halal-butcher/issues/20) - As a **developer**, I want **to create base & home templates and stylesheets** so that **the user audience can navigate around the website intuitively on all viewport sizes**.
    - [#21](https://github.com/legenduzair/the-halal-butcher/issues/21) - As a **user**, I can **navigate around the main home page of the site** so that **I can begin my online shopping with happiness and ease**.
    
3. Allauth Setup:
    - [#16](https://github.com/legenduzair/the-halal-butcher/issues/16) - As a **developer**, I want **to setup the Allauth Django library** so that **the target audience can access authentication capabilities of the project**.
    - [#17](https://github.com/legenduzair/the-halal-butcher/issues/17) - As a **user**, I can **create an account on the website** so that **I can access features that require authenticated permissions such as posting a product review, ordering & paying for a product and more**.
    - [#18](https://github.com/legenduzair/the-halal-butcher/issues/18) - As a **user**, I can **sign in to my registered account** so that **I can access the advanced permissions required of some features on the website**.
    - [#19](https://github.com/legenduzair/the-halal-butcher/issues/19) - As a **user**, I can **sign out of my registered account** so that **I can keep my account safe and secure**.

4. Configuring Products App:
    - [#22](https://github.com/legenduzair/the-halal-butcher/issues/22) - As a **user**, I can **view the list of products that available on the website** so that **I am aware of what products are for sale, so I can potentially click into them for more detailed information**.
    - [#23](https://github.com/legenduzair/the-halal-butcher/issues/23) - As a **user**, I can **view each product from the product list in details** so that **I can view more information about the specific product which may potentially lead to a purchase**.
    - [#24](https://github.com/legenduzair/the-halal-butcher/issues/24) - As a **user**, I can **search for a product of my liking** so that **I can easily find the product I am looking for**.
    - [#25](https://github.com/legenduzair/the-halal-butcher/issues/25) - As a **user**, I can **filter the products list I want by price/category** so that **I can compare the products easily with other products**.

5. Configure Wishlist App:
    - [#26](https://github.com/legenduzair/the-halal-butcher/issues/26) - As a **user**, I can **add products to a wishlist** so that **I can quickly access the products at a later date**.
    - [#27](https://github.com/legenduzair/the-halal-butcher/issues/27) - As a **user**, I can **able to view products from my wishlist** so that **purchase them when required**.
    - [#28](https://github.com/legenduzair/the-halal-butcher/issues/28) - As a **user**, I can **remove products from my wishlist** so that **I can remove products that I no longer require for the future**.

6. Configure Shopping Bag App:
    - [#29](https://github.com/legenduzair/the-halal-butcher/issues/29) - As a **user**, I can **add products to my shopping cart** so that **proceed to purchase them**.
    - [#30](https://github.com/legenduzair/the-halal-butcher/issues/30) - As a **user**, I can **view the products I have added to the cart** so that **I can confirm before proceeding to checkout**.
    - [#31](https://github.com/legenduzair/the-halal-butcher/issues/31) - As a **user**, I can **edit products in my shopping cart** so that **I can proceed with the correct products to checkout**.
    - [#32](https://github.com/legenduzair/the-halal-butcher/issues/32) - As a **user**, I can **remove a product from the shopping cart** so that **I can proceed with checkout or if I no longer need the item**.
    - [#33](https://github.com/legenduzair/the-halal-butcher/issues/33) - As a **user**, I can **proceed to checkout with the added items from the shopping cart** so that **I can quickly purchase the items added**.

7. Configure Checkout App:
    - [#34](https://github.com/legenduzair/the-halal-butcher/issues/34) - As a **user**, I can **add my delivery and billing details when processing an order** so that **I can complete my order**.
    - [#35](https://github.com/legenduzair/the-halal-butcher/issues/35) - As a **user**, I can **add my payment details during checkout** so that **I can pay for the purchase**.
    - [#36](https://github.com/legenduzair/the-halal-butcher/issues/36) - As a **user**, I can **view the order confirmation page after it has been processed** so that **I am aware that my order and payment have gone through**.

8. Configure Profile App:
    - [#37](https://github.com/legenduzair/the-halal-butcher/issues/37) - As a **user**, I can **create my user profile** so that **I can view my order details of processed orders and input saved delivery information so I can process future orders easily**.
    - [#38](https://github.com/legenduzair/the-halal-butcher/issues/38) - As a **user**, I can **edit personal information on my user profile** so that **I can use the correct details when processing future potential orders**.

9. Product Management:
    - [#39](https://github.com/legenduzair/the-halal-butcher/issues/39) - As a **store owner**, I can **add any new products to the store product list** so that **the site can be up to date with new products**.
    - [#40](https://github.com/legenduzair/the-halal-butcher/issues/40) - As a **store owner**, I can **edit products through product management** so that **I can keep the existing products up to date on the website**.
    - [#41](https://github.com/legenduzair/the-halal-butcher/issues/41) - As a **store owner**, I can **delete products via product management** so that **I can remove any unwanted products from the site**.

10. Final Deployment:
    - [#42](https://github.com/legenduzair/the-halal-butcher/issues/42) - As a **developer**, I want to **create and deploy my project on Heroku** so that **my project is deployed properly live**.
    - [#43](https://github.com/legenduzair/the-halal-butcher/issues/43) - As a **developer**, I want to **setup AWS including access to S3 buckets** so that **my media and static files are stored and have loaded up properly**.
    - [#44](https://github.com/legenduzair/the-halal-butcher/issues/44) - As a **developer**, I want to **input any final code and cache changes** so that **my project is deployed with all of the correct code and variables**.

11. Product Reviews:
    - [#45](https://github.com/legenduzair/the-halal-butcher/issues/45) - As a **user**, I can **add a product review** so that **I can share my review with other users who are also interested in purchasing the products**.
    - [#46](https://github.com/legenduzair/the-halal-butcher/issues/46) - As a **user**, I can **read other people's reviews** so that **I can view other people's opinions of the product I wish to purchase**.
    - [#47](https://github.com/legenduzair/the-halal-butcher/issues/47) - As a **user**, I can **edit product reviews** so that **I am able to make corrections to the review and update it**.
    - [#48](https://github.com/legenduzair/the-halal-butcher/issues/48) - As a **user**, I can **delete product reviews** that **I have written so that it is no longer on the website for others to view**.

12. Web Marketing:
    - [#49](https://github.com/legenduzair/the-halal-butcher/issues/49) - As a **store owner**, I want **to add the option for users to sign up to an email newsletter** so that **I can use it for marketing new products**.
    - [#50](https://github.com/legenduzair/the-halal-butcher/issues/50) - As a **store owner**, I want **to create a Facebook page for the company** so that **I can promote marketing of new products and advertise the company to Facebook users**.

13. Configure Blog App:
    - [#52](https://github.com/legenduzair/the-halal-butcher/issues/52) - As a **user**, I can **view a list of one or multiple blog entries** so that **I can click onto them to read the blog information in more detail**.
    - [#53](https://github.com/legenduzair/the-halal-butcher/issues/53) - As a **user**, I can **view a chosen blog entry in detail** so that **I can read the full content of the blog**.
    - [#54](https://github.com/legenduzair/the-halal-butcher/issues/54) - As a **store owner**, I can **add a blog to the list of blog entries** so that **the site can be setup with blog entries for users to read**.
    - [#55](https://github.com/legenduzair/the-halal-butcher/issues/55) - As a **store owner**, I can **update a blog entry** so that **the site can be updated with the correct & latest information**.
    - [#56](https://github.com/legenduzair/the-halal-butcher/issues/56) - As a **store owner**, I can **delete any blog entries from the website** so that **I can remove any unwanted blogs on the site**.

### The Structure Plane

#### Entity Relationship Diagram

As this project utilises Django which is a MVT(Model, View & Template) framework, a connection to database tables or 'Models' is required. An entity relationship diagram was created to visually map out the structure of the databases & models. The entity relationship diagram was creating using [DrawSQL](https://drawsql.app/) and is shown below:

![screenshot of ERD on DrawSQL](/readme/screenshots/erd.png)

#### User Stories - Acceptance Criterias'

As part of the Strategy Plane, I also incorporated Acceptance Criterias' within each User Story, to help plan and structure the development of my project and be more organised about the whole workflow & process.

<details>
    <summary>User Story #14 - As a Developer, I can setup Django by installing the appropriate libraries, creating the admin superuser and create my first app so that I can initiate development.</summary>

    Acceptance Criterias:
        None     
</details>
<br>
<details>
    <summary>User Story #15 - As a developer, I want to setup the Django environment secret keys in an env.py file/Gitpod settings so that I do not expose the keys in an insecure fashion.</summary>

    Acceptance Criterias:
        None     
</details>
<br>
<details>
    <summary>User Story #16 - As a developer, I want to setup the Allauth Django library so that the target audience can access authentication capabilities of the project.</summary>

    Acceptance Criterias:
        None     
</details>
<br>
<details>
    <summary>User Story #17 - As a user, I can create an account on the website so that I can access features that require authenticated permissions such as posting a product review, ordering & paying for a product and more.</summary>

    Acceptance Criterias:
        1. Given that I am not unauthenticated on the website, when I click on the register navigation link, then it will take me to a registration form where I can register using my email address, username and password.
        2. Given that I am authenticated on the website, when I click on the register after inputting the same credentials I used to sign up originally, then the website will in form me that an account has already been made with these credentials.    
</details>
<br>
<details>
    <summary>User Story #18 - As a user, I can sign in to my registered account so that I can access the advanced permissions required of some features on the website.</summary>

    Acceptance Criterias:
        1. Given that I am authenticated on the website, when I click on the sign in navigation link, then the website will take me to the login form where I can input my registered credentials.
        2. Given that I am authenticated on the website, when I click on sign in after inputting my registered credentials, then the website will sign me in, providing me with visual confirmation.
        3. Given that I am authenticated on the website, when I try to input wrong credentials in the login form, then the website will inform me that my details are incorrect, preventing login.    
</details>
<br>
<details>
    <summary>User Story #19 - As a user, I can sign out of my registered account so that I can keep my account safe and secure.</summary>

    Acceptance Criterias:
        1. Given that I am logged into my account on the website, when I click on the sign out navigation link, then it will provide me with confirmation, if i want to sign out or not.
        2. Given that I press logout on the confirmation sign out pagewhen I click on the sign out button then it will successfully sign me out of my registered account, prevent access of advanced permissions of the site.  
</details>
<br>
<details>
    <summary>User Story #20 - As a developer, I want to create base & home templates and stylesheets so that the user audience can navigate around the website intuitively on all viewport sizes.</summary>

    Acceptance Criterias:
        None  
</details>
<br>
<details>
    <summary>User Story #21 - As a user, I can navigate around the main home page of the site so that I can begin my online shopping with happiness and ease.</summary>

    Acceptance Criterias:
       1. Given that I am on the home page of the website when I click on any navigation links in the navbar, then it will redirect me to the appropriate HTML page.
       2. Given that I am on the home page of the website when I view the home page at first glance and on different viewports then it will be appealing to my eyes, wanting me to stay on the website longer to possibly purchase products.  
</details>
<br>
<details>
    <summary>User Story #22 - As a user, I can view the list of products that available on the website so that I am aware of what products are for sale, so I can potentially click into them for more detailed information.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the site when I navigate to the product list, then I will be able to view all the products with their corresponding product cards available for sale. 
</details>
<br>
<details>
    <summary>User Story #23 - As a user, I can view each product from the product list in details so that I can view more information about the specific product which may potentially lead to a purchase.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I click on any product in the product list then I will be able to access the product I have chosen, in detail. 
</details>
<br>
<details>
    <summary>User Story #24 - As a user, I can search for a product of my liking so that I can easily find the product I am looking for.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the websitewhen I enter the product name in the search bar then the corresponding product will be displayed. 
</details>
<br>
<details>
    <summary>User Story #25 - As a user, I can filter the products list I want by price/category so that I can compare the products easily with other products.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the websitewhen I am on the product list and I filter the list via price/category then the list will be filtered successfully via the category choice.
</details>
<br>
<details>
    <summary>User Story #26 - As a user, I can add products to a wishlist so that I can quickly access the products at a later date.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the websitewhen I add a product to my wishlistthen the corresponding product will be added successfully to my wishlist.
       2. Given that I am an unregistered user on the websitewhen I add a product to my wishlistthen the website will advise me to sign in before adding to wishlist.
</details>
<br>
<details>
    <summary>User Story #27 - As a user, I can able to view products from my wishlist so that purchase them when required.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the websitewhen I click on a product in my wishlistthen the it will redirect me to the product detail page of that corresponding product that is in my wishlist.
</details>
<br>
<details>
    <summary>User Story #28 - As a user, I can remove products from my wishlist so that I can remove products that I no longer require for the future.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the websitewhen I remove a product from my wishlistthen the corresponding product will be removed successfully from my wishlist.
</details>
<br>
<details>
    <summary>User Story #29 - As a user, I can add products to my shopping cart so that proceed to purchase them.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the websitewhen I add a product to the shopping cartthen the corresponding product will be added successfully to the shopping cart.
       2. Given that I am a user on the websitewhen I add a product to the shopping cart that has already been addedthen the corresponding product's quantity will increase by 1.
</details>
<br>
<details>
    <summary>User Story #30 - As a user, I can view the products I have added to the cart so that I can confirm before proceeding to checkout.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the websitewhen I view my shopping cartthen I will be able to see all the products I have added to the shopping cart, ready for me to purchase.
</details>
<br>
<details>
    <summary>User Story #31 - As a user, I can edit products in my shopping cart so that I can proceed with the correct products to checkout.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the websitewhen I view my shopping cart to edit cart contentsthen I will be able to adjust the quantity of products before I proceed with purchasing.
</details>
<br>
<details>
    <summary>User Story #32 - As a user, I can remove a product from the shopping cart so that I can proceed with checkout or if I no longer need the item.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the websitewhen I remove a product from the shopping cartthen the corresponding product will be removed successfully from the cart.
</details>
<br>
<details>
    <summary>User Story #33 - As a user, I can proceed to checkout with the added items from the shopping cart so that I can quickly purchase the items added.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the websitewhen I click the checkout button on the shopping cart pagethen I will be able to proceed with payment of the products in the cart.
       2. Given that I am a unregistered user on the websitewhen I click the checkout button on the shopping cart pagethen I will not be able to access checkout unless I am authenticated.
</details>
<br>
<details>
    <summary>User Story #34 - As a user, I can add my delivery and billing details when processing an order so that I can complete my order.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the checkout page, when I proceed to checkout, then I can add my delivery and billing address.
       2. Given that I am a registered user on the checkout page, when I enter my address details, then I can click the option to save my details so I don't have to fill it out on the next order.
       3. Given that I am an unregistered user but I am logged out, when I progress to enter my address information, then It will tell me to login before proceeding to checkout.
</details>
<br>
<details>
    <summary>User Story #35 - As a user, I can add my payment details during checkout so that I can pay for the purchase.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the checkout page, when I am on the payment page then I can add my credit card/debit card details to proceed with payment.
       2. Given that I am a registered user on the checkout page, when I process the payment using my card details then the system will process the payment.
       3. Given that I am a registered user on the checkout page, when my payment fails then I will be returned to the checkout page without losing all of my inputted information.
       4. Given that I am a registered user on the checkout page, when my payment is successfulthen I will be returned to the confirmation page of my order along with the details of it.
</details>
<br>
<details>
    <summary>User Story #36 - As a user, I can view the order confirmation page after it has been processed so that I am aware that my order and payment have gone through.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user when my the order and payment have processed successfully, then I will be taken to the order confirmation page where the order details will be listed.
       2. Given that I am a registered user when my the order and payment have processed successfully, then I will receive an email containing my order confirmation details.
       3. Given that I am a registered user when my the order and payment have processed successfully, then I can view the details of the order on my profile.
</details>
<br>
<details>
    <summary>User Story #37 - As a user, I can create my user profile so that I can view my order details of processed orders and input saved delivery information so I can process future orders easily.</summary>

    Acceptance Criterias:
       1. Given that I am am logged in and view my profile, when I view my profile, then I can see my preferred saved address details.
       2. Given that I am am logged in and view my profile, when I view my profile, then I can see any successful processed order history.
       3. Given that I am am logged in when I proceed to checkout, then I can see my preferred saved address details ready to be used for checkout.
</details>
<br>
<details>
    <summary>User Story #38 - As a user, I can edit personal information on my user profile so that I can use the correct details when processing future potential orders.</summary>

    Acceptance Criterias:
       1. Given that I am am logged in and view my profile, when I want to edit my profile, then I can input new personal information of my liking.
       2. Given that I am am logged in and view my profile, when I want to edit my profile, then I can delete any personal information of my liking.
</details>
<br>
<details>
    <summary>User Story #39 - As a store owner, I can add any new products to the store product list so that the site can be up to date with new products.</summary>

    Acceptance Criterias:
       1. Given that I am the store owner when I select product management and then add product, then I will be redirected to a form that allows me to add a new product.
       2. Given that I am the store owner when I complete the form and click add product, then I will be redirected to the product list, with the newly added product displaying on the list.
</details>
<br>
<details>
    <summary>User Story #40 - As a store owner, I can edit products through product management so that I can keep the existing products up to date on the website.</summary>

    Acceptance Criterias:
       1. Given that I am the store owner when I navigate to the product list, then I should be displayed with the option to edit a product under the product card.
       2. Given that I am the store owner when I navigate to the product list and click on edit product, then I should be redirected to the product form where I can edit details of the product.
       3. Given that I am the store owner when I complete the form and click edit product, then I should be redirected to the product list with the updated product displayed.
</details>
<br>
<details>
    <summary>User Story #41 - As a store owner, I can delete products via product management so that I can remove any unwanted products from the site.</summary>

    Acceptance Criterias:
       1. Given that I am the store owner when I navigate to the product list, then I should have an option to delete the product.
       2. Given that I am the store owner when I navigate to the product list and click delete, then it should redirect me to a deletion confirmation page.
       3. Given that I am the store owner when I confirm deletion of the product, then it should delete the product from the product list.
</details>
<br>
<details>
    <summary>User Story #42 - As a developer, I want to create and deploy my project on Heroku so that my project is deployed properly live.</summary>

    Acceptance Criterias:
       None
</details>
<br>
<details>
    <summary>User Story #43 - As a developer, I want to setup AWS including access to S3 buckets so that my media and static files are stored and have loaded up properly.</summary>

    Acceptance Criterias:
       None
</details>
<br>
<details>
    <summary>User Story #44 - As a developer, I want to input any final code and cache changes so that my project is deployed with all of the correct code and variables.</summary>

    Acceptance Criterias:
       None
</details>
<br>
<details>
    <summary>User Story #45 - As a user, I can add a product review so that I can share my review with other users who are also interested in purchasing the products.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user when I have purchased a product then I can leave a product review for the purchased product.
</details>
<br>
<details>
    <summary>User Story #46 - As a user, I can read other people's reviews so that I can view other people's opinions of the product I wish to purchase.</summary>

    Acceptance Criterias:
       1. Given that I am a userwhen I navigate to a product page, then I will be able to view reviews of the product below.
</details>
<br>
<details>
    <summary>User Story #47 - As a user, I can edit product reviews so that I am able to make corrections to the review and update it.</summary>

    Acceptance Criterias:
       1. Given that I am a user who has left a review I am trying to edit, when I navigate to the product page, then it should give me an option to edit a review.
       2. Given that I am a user who has not left a review I am trying to edit, when I navigate to the product page, then it should not give me an option to edit that review.
</details>
<br>
<details>
    <summary>User Story #48 - As a user, I can delete product reviews that I have written so that it is no longer on the website for others to view.</summary>

    Acceptance Criterias:
       1. Given that I am a user who has left a review that I am trying to delete, when I navigate to the product page, then it should give me an option to delete a review.
       2. Given that I am a user who has left a review that I am trying to delete, when I navigate to the product page and click on delete review, then it should remove the review from the product page.
       3. Given that I am a user who has not left a review that I am trying to delete, when I navigate to the product page then it should not give me an option to delete that review.
</details>
<br>
<details>
    <summary>User Story #49 - As a store owner, I want to add the option for users to sign up to an email newsletter so that I can use it for marketing new products.</summary>

    Acceptance Criterias:
       1. Given that I am a user who wants to sign up to the email newsletter, when I enter my email address, then my email address is added to the newsletter list.
</details>
<br>
<details>
    <summary>User Story #50 - As a store owner, I want to create a Facebook page for the company so that I can promote marketing of new products and advertise the company to Facebook users.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the home page, when I navigate to the footer, then I should be seeing a hyperlink which takes me to the promoted Facebook page of the company.
</details>
<br>
<details>
    <summary>User Story #52 - As a user, I can view a list of one or multiple blog entries so that I can click onto them to read the blog information in more detail.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the site when I navigate to the blog list, then I will be able to view all the blog entries created by the company owner.
</details>
<br>
<details>
    <summary>User Story #53 - As a user, I can view a chosen blog entry in detail so that I can read the full content of the blog.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the site when I click on any blog entry from the list, then I will be navigated to the blog content in detail.
</details>
<br>
<details>
    <summary>User Story #54 - As a store owner, I can add a blog to the list of blog entries so that the site can be setup with blog entries for users to read.</summary>

    Acceptance Criterias:
       1. Given that I am a store owner when I click on 'the meat blog.' from the navigation links then I will be able to access the add blog entry form.
       2. Given that I am a store owner when I complete the form and add the blog entry then I will be able to view the newly added blog entry in the list of blogs.
</details>
<br>
<details>
    <summary>User Story #55 - As a store owner, I can update a blog entry so that the site can be updated with the correct & latest information.</summary>

    Acceptance Criterias:
       1. Given that I am a store owner when I click on edit on a blog entry on a blog detailthen I will be able to access the edit blog entry form.
       2. Given that I am a store owner when I complete the form and update the blog entry then I will be able to view the updated information of the corresponding blog entry I updated.
</details>
<br>
<details>
    <summary>User Story #56 - As a store owner, I can delete any blog entries from the website so that I can remove any unwanted blogs on the site.</summary>

    Acceptance Criterias:
       1. Given that I am a store owner when I click on the delete button on a blog detail page then I will be able to access the blog deletion confirmation modal.
       2. Given that I am a store owner when I confirm deletion of a blog entry via the modal then the corresponding blog entry will be removed from the list of blog entries.
</details>
<br>

### The Skeleton Plane
#### Wireframes

Before initiating the project, I planned the general layout and structure of the main content for each page of the website across various screen sizes; desktop, tablet and mobile. The wireframes below were designed using Balsamiq Wireframes:

- (Home Page(Desktop))[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/homepage-wf-ss.png]
- (Home Page(Tablet & Mobile))[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/homepage-wf-ss-mob.png]
- (Authentication Pages)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/auth-wf-ss.png]
- (Product List Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/productlist-wf-ss.png]
- (Product Detail Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/productdetail-wf-ss.png]
- (User Profile Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/profile-wf-ss.png]
- (Product Management Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/prodmanage-wf-ss.png]
- (Shopping Basket Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/trolley-wf-ss.png]
- (Wishlist Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/wishlist-wf-ss.png]
- (Checkout Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/checkout-wf-ss.png]
- (Order Confirmation Page)[https://github.com/legenduzair/the-halal-butcher/blob/main/readme/screenshots/order-confirm-wf-ss.png]

### The Surface Plane
#### Colour Scheme

After completing the layout of the wireframes to create a skeleton for the project, I selected the colour scheme by generating a colour palette on Coolors. The colours from the palette were used as they had high level of colour contrast to maximise user accessibility. The colour palette is shown below.

![colour scheme of project](/readme/screenshots/color-scheme.png)

#### Typography

When designing the website, I had carefully chosen two complimentary fonts; 'News Cycle' that is the primary font used throughout the Bootstrap theme: [Bootswatch Journal](https://bootswatch.com/journal/) and 'OpenSans' from Google Fonts. It is important that the text on the website is clear & easy for users to read and is not too unappealing to the human eye. The letters are spaced out correctly and the style of the font fits the scheme of the website; Meat Butcher Store.

#### Images

All images used for developing the website were acquired from [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/images/stock/royalty-free) and [Vecteezy](https://www.vecteezy.com/free-photos). These images were uploaded into my S3 bucket on [AWS](https://aws.amazon.com/).

## Features

## Future Improvements

There are several improvements to functionality that I would like to implement in the future. Some of these improvements have been gathered from the user stories on the project Kanban board [here](https://github.com/legenduzair/the-halal-butcher/projects/2). These user stories have not been completed and would be implemented as future enhancement opportunities. These include:

- The ability to recover a user's password if it has been stolen/forgotten/corrupted. This functionality is part of the allauth library which has already been installed in this project but only needs to be setup to make this functional
- The ability for a user to login their account via social media sign in.
- The ability for the store owner to add, edit and delete blog entries without having to access the admin.

## Web Marketing

## Testing

A full detailed breakdown of all testing strategies and code validation techniques is documented in a separate file called TESTING.md.

## Technologies Used
### Languages & Frameworks

The follow programming languages & frameworks were used in the development of this project:
- Python:
    - The following python packages were installed and used for this project:
    ![python requirements.txt file](/readme/screenshots/python-libraries.png)
- Django:
    - Django was used as the primary Python framework for this project.
    - Django's authentication library; allauth, was used to implement user account authentication.
- Heroku:
    - Heroku is the cloud based platform used to deploy this website and make it public.
- Heroku PostgreSQL:
    - Heroku PostgreSQL was used as the database choice for this project during development.
- JavaScript & JQuery:
    - Vanilla JS & JQuery code was added to implement the stripe elements in payment forms, edit the country field in forms, displaying toasts across the website and handling payment forms.
- Bootstrap & Bootswatch 4.6.0:
    - Bootstrap framework and Bootswatch theme was used to implement the navbar, footer and structure the general content across the project.
- Font Awesome 5.15.4:
    - Font Awesome icons were used in different sections of the project where appropriate.
- CSS:
    - Custom CSS was written to implement my own styling into the project. It was also used to add media queries to provide responsive across different viewport sizes.
- Jinja/Django Templating:
    - Jinja templating was used to insert information from the database into the website. This includes transferring the logic from the app models.py & views.py to the template HTML pages.
- HTML:
    - HTML was the base language used to code the templates for the project.

### Packages Used

The following packages were used during development of my project:

- GitPod - IDE used for the development of the project.
- VS Code - IDE used for the development of the project.
- Git - Used for version control and transferring files from VS Code to the repository.
- GitHub - Used to create repository to store files for this project.

### Resources

The following resources were used during development of my project:

- Balsamiq Wireframes - Used to design the wireframes for the website
- DrawSQL.app - Used to sketch entity relationship diagram.
- Amazon Web Services S3 Bucket - Used for hosting project media images and static files.
- Summernote - Library used to create the WYSIWYG form editor.
- Django AllAuth - Used to implement authentication of users to website.
- StackOverflow - Very helpful reference to research specific content.
- Stripe - Used to implement payment in the website and test webhooks on endpoint URL's frequently.
- Mailchimp - Used to implement email newsletter sign up form.
- Facebook Pages - Used to create The Halal Butcher Facebook page.

## Deployment

The Halal Butcher was deployed via Heroku. The deployed website can be found here - [The Halal Butcher](https://halal-butcher.herokuapp.com/).

## Credits
All references that assisted me in developing The Halal Butcher have been mentioned throughout the README file. However I would like to thank:

- Richard Wells - The coding extraordinaire who is my project mentor. Richard was a huge help when developing this project.
- The Slack community - Reviewing my project and observing if any changes needed making.
- Code Institute tutors - Assisted with fixing my Stripe webhooks.