# Webberry

**Template repository for the dockerized django apps based on postgresql database..**

> Default admin user is : `username: 'admin', password: '123456@@' ` for the django admin panel. 

> Check the `http://0.0.0.0:8006/accounts/login/` url to test middleware. Middleware will print somethings to the terminal.
___

## Preparing : 

0. Clone the repo
1. Copy `env.txt` to `app/.env`
2. Change the specific fields in `app/.env`
3. Update the entrypoint.sh file permissions locally: `chmod +x app/entrypoint.sh`
4. Build the image : `docker-compose build`
4. Run the container : `docker-compose up -d`
5.  Follow outputs alive and track errors, to make continuous development: `docker logs --follow webberry-app`

___

## Middlewares 

**Middleware :** Middleware is a framework of hooks into Django's request/response processing. It is a light, low-level "plugin" system for globally altering Django's input or output.

* **Django Middleware Use Case :** 
  * Filtering requests
  * Injecting data into request/response
  * Performing Logging/Page Analytics.
* You can see activated django middlewares of your project from `settings.py` on `MIDDLEWARE` list.
* `MIDDLEWARE` list describes all the middlewares that is currently activated on our django application.
* Order of the `MIDDLEWARE` list is the order in which data will pass through. The HTTP Request will pass from top to bottom and the HTTP Response will pass from bottom to top.
* Each middleware will take an request and also it need to pass that request over to the next middleware in the `MIDDLEWARE` list.
* A middleware can also return response directly instead of forwarding the request further down the chain. For example: `CSRF Middleware`
  

* **Security Middleware :** 
  * HTTP Strict Transport Security
  * Referrer Policy
  * SSL Redirect
* 
* **GZip Middleware :** 
  * Compresses content for browsers that understand GZip


# Typical HTTP Request-Response Cycle

```
|        |  > Http Request  > |  Web  |  > | URL Match | > |   View    | < | Database |
| Client |                    |       |                    |           |
|        |  < Http Response < | Server|  <     <    <    < | Processing| < | Template |
```

# An Example Django Middleware Cycle

```
|Client|> Http Request  >| Web  |>| Security |>| Session  |>| Common   |>|  View    |<|Database|
|      |< Http Response <|Server|<|Middleware|<|Middleware|<|Middleware|<|Processing|<|Template|
```
