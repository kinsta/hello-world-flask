![Photo by Daniele Levis Pelusi on Unsplash](https://user-images.githubusercontent.com/2342458/202704431-d5eda12f-a1eb-4f05-be84-de14872b57db.png)

# Kinsta - Hello World - Flask

An example of how to deploy a flask application on Kinsta App Hosting services.

> Kinsta’s Application Hosting is a service to run your web apps and any databases side by side in a hassle-free environment, tailored for developer needs and ease of use. App Hosting is currently in an invite-only beta phase, sign up for a test account at [kinsta.com/application-hosting](https://kinsta.com/application-hosting/).

## Dependency Management

During the deployment process Kinsta will automatically install dependencies defined in your `requirements.txt` file.

## Web Server Setup

### Start Command

When deploying an application Kinsta will automatically create a processes based on the Procfile in the root of the repository:

```
web: gunicorn helloworld.wsgi
```
