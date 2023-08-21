![Photo by Daniele Levis Pelusi on Unsplash](https://user-images.githubusercontent.com/2342458/202704431-d5eda12f-a1eb-4f05-be84-de14872b57db.png)

# Kinsta - Hello World - Flask

An example of how to deploy a flask application on Kinsta App Hosting services.

---
Kinsta is a developer-centric cloud host / PaaS. We’re striving to make it easier for you to share your web projects with your users. Focus on coding and building, and we’ll take care of deployment and provide fast, scalable hosting. + 24/7 expert-only support.

- [Start your free trial](https://kinsta.com/signup/?product_type=app-db)
- [Application Hosting](https://kinsta.com/application-hosting)
- [Database Hosting](https://kinsta.com/database-hosting)

## Dependency Management

During the deployment process Kinsta will automatically install dependencies defined in your `requirements.txt` file.

## Web Server Setup

### Start Command

When deploying an application Kinsta will automatically create a processes based on the Procfile in the root of the repository:

```
web: gunicorn helloworld.wsgi
```

## Watch How to Set Up a Flask Application on Kinsta
[![Watch the video](https://img.youtube.com/vi/80skDMcZK28/maxresdefault.jpg)](https://www.youtube.com/watch?v=80skDMcZK28)
