## Web Server Setup

### Start Command
When deploying an application Kinsta will automatically create a processes based on the Procfile in the root of 
the repository. Make sure to use this command to run your server:

```
web: gunicorn helloworld.wsgi
```