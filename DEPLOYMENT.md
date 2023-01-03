# Deployment

This walkthrough presumes you are using GitPod but the steps still apply for VS code

## Walkthrough:

1. Create an ElephantSQL.com account. (Sign up with GitHub if using that)
2. Log in to ElephantSQL.com to access your dashboard
3. Click **“Create New Instance”**
4. Set up your plan
   - give your plan a **Name** (this is commonly the name of the project)
   - select the **Tiny Turtle (Free)** plan
   - you can leave the **Tags** field blank
5. Select **“Select Region”**
6. Select a data center near you
   - ❗ If you receive a message saying *"Error: No cluster available in your-chosen-data-center yet"*, choose another region.
   - Note: You're free to use any of the available free data centers, be it AWS, Azure or any of the other providers.
7. Then click **“Review”**
8. Check your details are correct and then click **“Create instance”**
9. Return to the ElephantSQL dashboard and click on the **database instance name** for this project
10. In the URL section, clicking the copy icon will copy the database URL to your clipboard

### Create a new Heroku app

1. Create Heroku account and sign in.
2. Click **New** to create a new app
3. Give your app a name and select the region closest to you. When you’re done, click **Create app** to confirm
4. Open the **Settings** tab
5. Add the config var **DATABASE_URL** and copy in your database url from ElephantSQL.

### Project preparation in Gitpod

Open up your Gitpod tab and follow the steps below:

1. Install **dj_database_url** and **psycopg2**

        Terminal command : pip3 install dj_database_url==0.5.0 psycopg2

2. Update your **requirements.txt** file with the newly installed packages

        Terminal command : pip freeze > requirements.txt

3. In your **settings.py** file, import dj_database_url

        import os
        import dj_database_url

4. In the **DATABASES** section change the code to the following:

        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.sqlite3',
        #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #     }
        # }
        
        DATABASES = {
            'default': dj_database_url.parse('your-database-url-here')
        }
   - ❗ DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations. We will remove it in a moment.

5. Migrate your database models to your new database

        Terminal command : python3 manage.py migrate
6. If you have objects to load into your database in json format, add them now. Be careful of the order.

        Terminal command : python3 manage.py loaddata "objects"

7. Create a superuser for your new database

        Terminal command : python3 manage.py createsuperuser
    

### Deploying to Heroku

1. Go back to **settings.py** and update DATABASES section as follows:

        if 'DATABASE_URL' in os.environ:
        DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
        else:
        DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
                }
        }

2. Install package called **gunicorn**, which will act as our web server:

       Terminal command : pip3 install gunicorn
3. And **freeze** that into our requirements file.

       Terminal command : pip3 freeze > requirements.txt
4. Now we can create our **Procfile** to tell Heroku to create a web dyno. In our root directory lets create a file named 'Procfile' and inside insert the code: 

        web: gunicorn **project_name_here**.wsgi:application
5. Then, in heroku, navigate to **settings / config vars** and 'Add' new entry: **DISABLE_COLLECTSTATIC** with the value of **1**.
This is to stop heroku from collecting any static files when we deploy.
6. We'll need to add the **hostname** of our Heroku app to ALLOWED_HOSTS in **settings.py**. We'll also add **localhost** in here so that Gitpod can work too.


        ALLOWED_HOSTS = ['project-name.herokuapp.com', 'localhost']
7. Enable automatic deploys on Heroku and then push to your GitHub repository.

8. Lastly, generate new Django SECRET_KEY and add it to **Config Vars** in Heroku.

   And then in **settings.py** replace the secret key setting with the call to get it from the enviroment and use an empty string as a default.

        SECRET_KEY = os.environ.get('SECRET_KEY', '')

### Creating an AWS Account

1. Create account and login
2. All Services > Storage menu > S3.
3. To do this click the orange button that says 'Create Bucket'.
4. Name the bucket and select the closest region to you. 
5. Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred. 
6. Uncheck the 'Block all public access' checkbox and check the warning box to acknowledge that the bucket will be made public, then click create bucket. 
7. Once created, click the bucket's name and navigate to the properties tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
8. Now navigate to the permissions tab, scroll down to the Cross-origin resource sharing (CORS) section, click edit and paste in the following code:

        [
          {
              "AllowedHeaders": [
                  "Authorization"
              ],
              "AllowedMethods": [
                  "GET"
              ],
              "AllowedOrigins": [
                  "*"
              ],
              "ExposeHeaders": []
          }
        ]
9. Then scroll back up to the 'Bucket Policy' section. Click 'edit' and then 'Policy generator'. This should open the AWS policy generator page.
10. From here under the 'select type of policy' dropdown menu, select 'S3 Bucket Policy'. Then inside 'Principle' allow all principals by typing a *.
11. From the 'Actions dropdown menu select 'Get object'. Then head back to the previous tab and locate the Bucket ARN number. Copy that, return to the policy generator and paste it in the field labelled Amazon Resource Name (ARN).
12. Once that's completed click 'Add statement', then 'Generate Policy'. Copy the policy that's been generated and paste it into the bucket policy editor.
13. Before you click save, add a '/*' at the end of your resource key. This is to allow access to all resources in this bucket.
14. Once those changes are saved, scroll down to the Access control list (ACL) section and click 'edit'.
15. Next to 'Everyone (public access)', check the 'list' checkbox. This will pop up a warning box that you will also have to check. Once that's done click 'save'.

### Creating AWS Groups, Policies and Users

1. Navigate to the IAM page.
2. Click 'User Groups' from the side bar, then click 'Create group'.
3. Name the group 'manage-*your-project-name*' and click 'Create group'. 
4. Then from the sidebar click 'Policies', then 'Create policy'.
5. Go to the JSON tab and click 'import managed policy'. Search for 'S3' and select 'AmazonS3FullAccess' and click import.
6. Return to your bucket and copy your ARN number. Head back to this policy and update the Resource key to include your ARN, and another line with your ARN followed by a /* as below: 
 
        {
                "Version": "2012-10-17",
                "Statement": [
                {
                        "Effect": "Allow",
                        "Action": [
                        "s3:*",
                        "s3-object-lambda:*"
                        ],
                        "Resource": [
                        "YOUR-ARN-NO-HERE",
                        "YOUR-ARN-NO-HERE/*"
                        ]
                }
                ]
        }

7. Click 'Next: Tags', 'Next: Review', and on this page give the policy a name. Then click 'Create policy'. 
8. Click 'User groups', and click the group you previously created. Go to the permissions tab and click 'Add permission' and from the dropdown click 'Attach policies'. 
9. Find the policy you just created, select it and click 'Add permissions'.
10. Finally you need to create a user to put in the group. Select users from the sidebar and click 'Add user'.  
11. Give your user a user name, check 'Programmatic Access', then click 'Next: Permissions'. 
12. Select your group that has the policy attached and click 'Next: Tags', 'Next: Review', then 'Create user'.
13. On the next page, download the CSV file.

### Connecting Django to S3

1. Install Boto3 and Django storages. Do this by running these commands:  

        Terminal command : pip3 install boto3
        Terminal command : pip3 install django-storages
        Terminal command : pip3 freeze > requirements.txt

2. Add 'storages' to your installed apps section inside your settings.py file. 
3. At the bottom of settings.py write:

        if 'USE_AWS' in os.environ:
                AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
                AWS_S3_REGION_NAME = 'insert-your-region-here'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'

                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

4. On Heroku go to config vars.
5. Add the keys AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The values can be found in the CSV file you downloaded. Once they have both been added, add the key USE_AWS, and set the value to True.
6. Remove the DISABLE_COLLECTSTAIC variable, since django should now collect static files automatically and upload them to S3.
7. In the root directory of your project create a file called 'custom_storages.py'. Write the following:

        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION

### Caching, Media Files & Stripe

1. In S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'. 
2. Inside the new media folder you just created, click 'Upload', 'Add files', and then select all the images that you are using on your site.
3. Then under 'Permissions' select the option 'Grant public-read access' and click upload. 

**Stripe** is needed to handle the checkout process when a payment is made. You can sign up for account [here](https://stripe.com/en-gb). To set up stripe payments you can follow their guide [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

6. Now, we will set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
7. Then in the side-nav under the Developers title, click on 'Webhooks', then 'Add endpoint'.
8. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:  

        https://your-app-name.herokuapp.com/checkout/wh/

9. Then click '+ Select events' and check the 'Select all events' checkbox at the top before clicking 'Add events' at the bottom. Once this is done finish the form by clicking 'Add endpoint'.
10. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
11. Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
12. Add these values under these keys:  

        STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
        STRIPE_SECRET_KEY = 'insert your secret key'
        STRIPE_WH_SECRET = 'insert your webhooks secret key'

13. Finally, back in your setting.py file in django, insert the following near the bottom of the file:  

        STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
        STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
        STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

[⮪ Return back to readme](README.md) | [Back to Top 🠕](#deployment)