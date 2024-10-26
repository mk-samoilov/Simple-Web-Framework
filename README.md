# Simple Web Framework

This is a lightweight, Python-based web framework that allows you to create simple web applications with ease. It provides basic routing capabilities and a template rendering system.

## Features

- Simple routing system
- Basic HTTP method support (GET, POST, etc.)
- Template rendering with variable substitution
- Multithreaded server to handle multiple client connections

## Usage

1. Create a new Python file (e.g., `app.py`) and import the necessary components:

   ```python
   from wf import WApp, render_template
   ```

2. Create an instance of the `WApp` class:

   ```python
   app = WApp(host="localhost", port=80)
   ```

3. Define your routes using the `@app.route` decorator:

   ```python
   @app.route("/", methods=["GET"])
   def home():
       return render_template("index.html", title="Welcome", message="Welcome to the Simple Web Framework!")
   ```

4. Create your HTML templates in a `templates` folder (e.g., `templates/index.html`):

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{{title}}</title>
   </head>
   <body>
       <h1>{{message}}</h1>
   </body>
   </html>
   ```

5. Run your application:

   ```python
   if __name__ == '__main__':
       app.run()
   ```

6. Access your application by opening a web browser and navigating to `http://localhost:80` (or the host and port you specified).

## Customization

- You can change the host and port by modifying the `WApp` initialization:
  ```python
  app = WApp(host="0.0.0.0", port=8080)
  ```

- Add more routes and templates as needed for your application.

## Limitations

- This is a basic framework intended for learning purposes and simple applications.
- It does not include advanced features like database integration, form handling, or security measures found in production-ready frameworks.
