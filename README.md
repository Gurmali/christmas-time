# ChristmasTime

ChristmasTime is a forum style website designed to share your christmas decorations with other peaople looking for inspiration for the holidays.

[This is a link to the live version](https://christmas-time-forum.herokuapp.com/)

<img src="media/images/responsive.jpg">


# Features

As of now, admins are able to make posts, and manage everything needed from the admin page.

Users are able to make an account, log in and out, leave comments and like posts by clicking on the tree under the post.

## Features left to implement

The ability for users to make their own posts, and manage them from a User account page. 
The ability for users to delete and edit comments direclty on the post view.

# Testing

- I have manualy tested the features thuroughly throughout the building process of this application.

  - Admin can log in, make posts, delete posts and comments

  - Users can make an acount with no issues

  - Users can log in and log out with no issues

  - Comment function works as expected

  - Like function works as expected

## Bugs

 - To log in to the admin page you can not simple write /admin at the end of the url

 - You have to write /admin/login/?next=/admin/

# Deployment

This project was developed using a GitPod workspace. The code was commited to Git and pushed to GitHub using the terminal.

## Deploying on Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:

   - Select "Create new app" in Heroku.
   - Choose a name for your app and select the location.

2. Attach the Postgres database:

   - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:

   - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
   - In your GitPod workspace, create an env.py file in the main directory.
   - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
   - Add the SECRET_KEY value to the Config Vars in Heroku.
   - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
   - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
   - In settings.py add the following sections:
      - Cloudinary to the INSTALLED_APPS list
      - STATICFILE_STORAGE
      - STATICFILES_DIRS
      - STATIC_ROOT
      - MEDIA_URL
      - DEFAULT_FILE_STORAGE
      - TEMPLATES_DIR
      - Update DIRS in TEMPLATES with TEMPLATES_DIR
      - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:

   - Create three directories in the main directory; media, storage and templates.
   - Create a file named "Procfile" in the main directory and add the following:
      - web: gunicorn project-name.wsgi
   - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository. Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.