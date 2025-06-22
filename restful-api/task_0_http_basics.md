# Task 0 - HTTP vs HTTPS and HTTP Basics

## ✅ Differences Between HTTP and HTTPS

| Feature         | HTTP                           | HTTPS                              |
|----------------|--------------------------------|------------------------------------|
| Security        | ❌ Unsecured                    | ✅ Secured with SSL/TLS encryption |
| Port            | 80                             | 443                                |
| Data Encryption | No                             | Yes                                |
| Use Cases       | Blogs, public info             | Login pages, payments              |
| URL Prefix      | http://                        | https://                           |

---

## 📦 HTTP Request & Response Structure

### Request Example:

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html


### ➤ HTTP Response Example:
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 123

<html>...</html> ```

🔁 Common HTTP Methods
| Method | Description                        | Example Use Case                 |
| ------ | ---------------------------------- | -------------------------------- |
| GET    | Retrieve data from the server      | Fetch blog post or page          |
| POST   | Send new data to the server        | Submit a contact form            |
| PUT    | Update existing data on the server | Edit a profile                   |
| DELETE | Remove data from the server        | Delete a comment or user account |


⚠️ Common HTTP Status Codes

| Code | Name                  | Description / Scenario               |
| ---- | --------------------- | ------------------------------------ |
| 200  | OK                    | Successful request (GET, POST, etc.) |
| 201  | Created               | Resource successfully created        |
| 400  | Bad Request           | Request is malformed or missing data |
| 404  | Not Found             | Resource not found on the server     |
| 500  | Internal Server Error | Server-side error occurred           |


