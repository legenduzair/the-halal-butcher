# <div align="center">Testing</div>

During and after the development of The Halal Butcher, the project went through rigorous testing to ensure a fully functional and responsive website was created. I have documented all the testing techniques used in the following sections. If you would like to traverse back to the README file, please click here - [README](https://github.com/legenduzair/the-halal-butcher/blob/main/README.md)

## Manual Testing

### User Stories

All user stories and their respective acceptance criterias were tested during and after development of this project. It is important to achieve these criterias as it is from a users perspective when navigating & using the website. Below is a summary of the results acquired. The user stories & acceptance criterias that have not been achieved/completed have already been documented in the [Future Improvements](https://github.com/legenduzair/the-halal-butcher#future-improvements) section.

<details>
    <summary>User Story #14 - As a Developer, I can setup Django by installing the appropriate libraries, creating the admin superuser and create my first app so that I can initiate development.</summary>

    Acceptance Criterias:
        None

    Achieved:
        Yes      
</details>
<br>
<details>
    <summary>User Story #15 - As a developer, I want to setup the Django environment secret keys in an env.py file/Gitpod settings so that I do not expose the keys in an insecure fashion.</summary>

    Acceptance Criterias:
        None

    Achieved:
        Yes     
</details>
<br>
<details>
    <summary>User Story #16 - As a developer, I want to setup the Allauth Django library so that the target audience can access authentication capabilities of the project.</summary>

    Acceptance Criterias:
        None 

    Achieved:
        Yes    
</details>
<br>
<details>
    <summary>User Story #17 - As a user, I can create an account on the website so that I can access features that require authenticated permissions such as posting a product review, ordering & paying for a product and more.</summary>

    Acceptance Criterias:
        1. Given that I am not unauthenticated on the website, when I click on the register navigation link, then it will take me to a registration form where I can register using my email address, username and password.
        2. Given that I am authenticated on the website, when I click on the register after inputting the same credentials I used to sign up originally, then the website will in form me that an account has already been made with these credentials.

    Acceptance Criterias' achieved:
        Yes    
</details>
<br>
<details>
    <summary>User Story #18 - As a user, I can sign in to my registered account so that I can access the advanced permissions required of some features on the website.</summary>

    Acceptance Criterias:
        1. Given that I am authenticated on the website, when I click on the sign in navigation link, then the website will take me to the login form where I can input my registered credentials.
        2. Given that I am authenticated on the website, when I click on sign in after inputting my registered credentials, then the website will sign me in, providing me with visual confirmation.
        3. Given that I am authenticated on the website, when I try to input wrong credentials in the login form, then the website will inform me that my details are incorrect, preventing login.

    Acceptance Criterias' achieved:
        Yes    
</details>
<br>
<details>
    <summary>User Story #19 - As a user, I can sign out of my registered account so that I can keep my account safe and secure.</summary>

    Acceptance Criterias:
        1. Given that I am logged into my account on the website, when I click on the sign out navigation link, then it will provide me with confirmation, if i want to sign out or not.
        2. Given that I press logout on the confirmation sign out page when I click on the sign out button then it will successfully sign me out of my registered account, prevent access of advanced permissions of the site.

    Acceptance Criterias' achieved:
        Yes   
</details>
<br>
<details>
    <summary>User Story #20 - As a developer, I want to create base & home templates and stylesheets so that the user audience can navigate around the website intuitively on all viewport sizes.</summary>

    Acceptance Criterias:
        None

    Achieved:
        Yes   
</details>
<br>
<details>
    <summary>User Story #21 - As a user, I can navigate around the main home page of the site so that I can begin my online shopping with happiness and ease.</summary>

    Acceptance Criterias:
       1. Given that I am on the home page of the website when I click on any navigation links in the navbar, then it will redirect me to the appropriate HTML page.
       2. Given that I am on the home page of the website when I view the home page at first glance and on different viewports then it will be appealing to my eyes, wanting me to stay on the website longer to possibly purchase products.

    Acceptance Criterias' achieved:
        Yes   
</details>
<br>
<details>
    <summary>User Story #22 - As a user, I can view the list of products that available on the website so that I am aware of what products are for sale, so I can potentially click into them for more detailed information.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the site when I navigate to the product list, then I will be able to view all the products with their corresponding product cards available for sale.

    Acceptance Criterias' achieved:
        Yes  
</details>
<br>
<details>
    <summary>User Story #23 - As a user, I can view each product from the product list in details so that I can view more information about the specific product which may potentially lead to a purchase.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I click on any product in the product list then I will be able to access the product I have chosen, in detail. 
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #24 - As a user, I can search for a product of my liking so that I can easily find the product I am looking for.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I enter the product name in the search bar then the corresponding product will be displayed. 
       
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #25 - As a user, I can filter the products list I want by price/category so that I can compare the products easily with other products.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I am on the product list and I filter the list via price/category then the list will be filtered successfully via the category choice.

    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #26 - As a user, I can add products to a wishlist so that I can quickly access the products at a later date.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the website when I add a product to my wishlist then the corresponding product will be added successfully to my wishlist.
       2. Given that I am an unregistered user on the website when I add a product to my wishlist then the website will advise me to sign in before adding to wishlist.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #27 - As a user, I can able to view products from my wishlist so that purchase them when required.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the website when I click on a product in my wishlist then the it will redirect me to the product detail page of that corresponding product that is in my wishlist.
    
    Acceptance Criterias' achieved:
        No 
</details>
<br>
<details>
    <summary>User Story #28 - As a user, I can remove products from my wishlist so that I can remove products that I no longer require for the future.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the website when I remove a product from my wishlist then the corresponding product will be removed successfully from my wishlist.
    
    Acceptance Criterias' achieved:
        Yes
</details>
<br>
<details>
    <summary>User Story #29 - As a user, I can add products to my shopping cart so that proceed to purchase them.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I add a product to the shopping cart then the corresponding product will be added successfully to the shopping cart.
       2. Given that I am a user on the website when I add a product to the shopping cart that has already been addedthen the corresponding product's quantity will increase by 1.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #30 - As a user, I can view the products I have added to the cart so that I can confirm before proceeding to checkout.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I view my shopping cart then I will be able to see all the products I have added to the shopping cart, ready for me to purchase.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #31 - As a user, I can edit products in my shopping cart so that I can proceed with the correct products to checkout.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I view my shopping cart to edit cart contents then I will be able to adjust the quantity of products before I proceed with purchasing.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #32 - As a user, I can remove a product from the shopping cart so that I can proceed with checkout or if I no longer need the item.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the website when I remove a product from the shopping cart then the corresponding product will be removed successfully from the cart.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #33 - As a user, I can proceed to checkout with the added items from the shopping cart so that I can quickly purchase the items added.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the website when I click the checkout button on the shopping cart page then I will be able to proceed with payment of the products in the cart.
       2. Given that I am a unregistered user on the website when I click the checkout button on the shopping cart page then I will not be able to access checkout unless I am authenticated.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #34 - As a user, I can add my delivery and billing details when processing an order so that I can complete my order.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the checkout page, when I proceed to checkout, then I can add my delivery and billing address.
       2. Given that I am a registered user on the checkout page, when I enter my address details, then I can click the option to save my details so I don't have to fill it out on the next order.
       3. Given that I am an unregistered user but I am logged out, when I progress to enter my address information, then It will tell me to login before proceeding to checkout.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #35 - As a user, I can add my payment details during checkout so that I can pay for the purchase.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user on the checkout page, when I am on the payment page then I can add my credit card/debit card details to proceed with payment.
       2. Given that I am a registered user on the checkout page, when I process the payment using my card details then the system will process the payment.
       3. Given that I am a registered user on the checkout page, when my payment fails then I will be returned to the checkout page without losing all of my inputted information.
       4. Given that I am a registered user on the checkout page, when my payment is successfulthen I will be returned to the confirmation page of my order along with the details of it.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #36 - As a user, I can view the order confirmation page after it has been processed so that I am aware that my order and payment have gone through.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user when my the order and payment have processed successfully, then I will be taken to the order confirmation page where the order details will be listed.
       2. Given that I am a registered user when my the order and payment have processed successfully, then I will receive an email containing my order confirmation details.
       3. Given that I am a registered user when my the order and payment have processed successfully, then I can view the details of the order on my profile.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #37 - As a user, I can create my user profile so that I can view my order details of processed orders and input saved delivery information so I can process future orders easily.</summary>

    Acceptance Criterias:
       1. Given that I am am logged in and view my profile, when I view my profile, then I can see my preferred saved address details.
       2. Given that I am am logged in and view my profile, when I view my profile, then I can see any successful processed order history.
       3. Given that I am am logged in when I proceed to checkout, then I can see my preferred saved address details ready to be used for checkout.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #38 - As a user, I can edit personal information on my user profile so that I can use the correct details when processing future potential orders.</summary>

    Acceptance Criterias:
       1. Given that I am am logged in and view my profile, when I want to edit my profile, then I can input new personal information of my liking.
       2. Given that I am am logged in and view my profile, when I want to edit my profile, then I can delete any personal information of my liking.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #39 - As a store owner, I can add any new products to the store product list so that the site can be up to date with new products.</summary>

    Acceptance Criterias:
       1. Given that I am the store owner when I select product management and then add product, then I will be redirected to a form that allows me to add a new product.
       2. Given that I am the store owner when I complete the form and click add product, then I will be redirected to the product list, with the newly added product displaying on the list.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #40 - As a store owner, I can edit products through product management so that I can keep the existing products up to date on the website.</summary>

    Acceptance Criterias:
       1. Given that I am the store owner when I navigate to the product list, then I should be displayed with the option to edit a product under the product card.
       2. Given that I am the store owner when I navigate to the product list and click on edit product, then I should be redirected to the product form where I can edit details of the product.
       3. Given that I am the store owner when I complete the form and click edit product, then I should be redirected to the product list with the updated product displayed.

    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #41 - As a store owner, I can delete products via product management so that I can remove any unwanted products from the site.</summary>

    Acceptance Criterias:
       1. Given that I am the store owner when I navigate to the product list, then I should have an option to delete the product.
       2. Given that I am the store owner when I navigate to the product list and click delete, then it should redirect me to a deletion confirmation page.
       3. Given that I am the store owner when I confirm deletion of the product, then it should delete the product from the product list.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #42 - As a developer, I want to create and deploy my project on Heroku so that my project is deployed properly live.</summary>

    Acceptance Criterias:
       None
    
    Achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #43 - As a developer, I want to setup AWS including access to S3 buckets so that my media and static files are stored and have loaded up properly.</summary>

    Acceptance Criterias:
       None
    
    Achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #44 - As a developer, I want to input any final code and cache changes so that my project is deployed with all of the correct code and variables.</summary>

    Acceptance Criterias:
       None
    
    Achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #45 - As a user, I can add a product review so that I can share my review with other users who are also interested in purchasing the products.</summary>

    Acceptance Criterias:
       1. Given that I am a registered user when I have purchased a product then I can leave a product review for the purchased product.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #46 - As a user, I can read other people's reviews so that I can view other people's opinions of the product I wish to purchase.</summary>

    Acceptance Criterias:
       1. Given that I am a userwhen I navigate to a product page, then I will be able to view reviews of the product below.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #47 - As a user, I can edit product reviews so that I am able to make corrections to the review and update it.</summary>

    Acceptance Criterias:
       1. Given that I am a user who has left a review I am trying to edit, when I navigate to the product page, then it should give me an option to edit a review.
       2. Given that I am a user who has not left a review I am trying to edit, when I navigate to the product page, then it should not give me an option to edit that review.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #48 - As a user, I can delete product reviews that I have written so that it is no longer on the website for others to view.</summary>

    Acceptance Criterias:
       1. Given that I am a user who has left a review that I am trying to delete, when I navigate to the product page, then it should give me an option to delete a review.
       2. Given that I am a user who has left a review that I am trying to delete, when I navigate to the product page and click on delete review, then it should remove the review from the product page.
       3. Given that I am a user who has not left a review that I am trying to delete, when I navigate to the product page then it should not give me an option to delete that review.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #49 - As a store owner, I want to add the option for users to sign up to an email newsletter so that I can use it for marketing new products.</summary>

    Acceptance Criterias:
       1. Given that I am a user who wants to sign up to the email newsletter, when I enter my email address, then my email address is added to the newsletter list.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #50 - As a store owner, I want to create a Facebook page for the company so that I can promote marketing of new products and advertise the company to Facebook users.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the home page, when I navigate to the footer, then I should be seeing a hyperlink which takes me to the promoted Facebook page of the company.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #52 - As a user, I can view a list of one or multiple blog entries so that I can click onto them to read the blog information in more detail.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the site when I navigate to the blog list, then I will be able to view all the blog entries created by the company owner.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #53 - As a user, I can view a chosen blog entry in detail so that I can read the full content of the blog.</summary>

    Acceptance Criterias:
       1. Given that I am a user on the site when I click on any blog entry from the list, then I will be navigated to the blog content in detail.
    
    Acceptance Criterias' achieved:
        Yes 
</details>
<br>
<details>
    <summary>User Story #54 - As a store owner, I can add a blog to the list of blog entries so that the site can be setup with blog entries for users to read.</summary>

    Acceptance Criterias:
       1. Given that I am a store owner when I click on 'the meat blog.' from the navigation links then I will be able to access the add blog entry form.
       2. Given that I am a store owner when I complete the form and add the blog entry then I will be able to view the newly added blog entry in the list of blogs.
    
    Acceptance Criterias' achieved:
        No
</details>
<br>
<details>
    <summary>User Story #55 - As a store owner, I can update a blog entry so that the site can be updated with the correct & latest information.</summary>

    Acceptance Criterias:
       1. Given that I am a store owner when I click on edit on a blog entry on a blog detailthen I will be able to access the edit blog entry form.
       2. Given that I am a store owner when I complete the form and update the blog entry then I will be able to view the updated information of the corresponding blog entry I updated.
    
    Acceptance Criterias' achieved:
        No
</details>
<br>
<details>
    <summary>User Story #56 - As a store owner, I can delete any blog entries from the website so that I can remove any unwanted blogs on the site.</summary>

    Acceptance Criterias:
       1. Given that I am a store owner when I click on the delete button on a blog detail page then I will be able to access the blog deletion confirmation modal.
       2. Given that I am a store owner when I confirm deletion of a blog entry via the modal then the corresponding blog entry will be removed from the list of blog entries.
    
    Acceptance Criterias' achieved:
        No
</details>
<br>

## Validation Testing

### HTML Validation

To validate the templates written in HTML for this project, I had to copy the code rendered on Google Chrome's page source option and paste it into the validator. This is because Django templates contain Jinja syntax in them which means it is not possible to directly copy the code from the templates. Any following screenshots are of HTML templates validated via [Nu HTML Checker](https://validator.w3.org/nu/), which contained any errors/warnings.