# Task 1: Consume data from an API using curl

## ✅ Step 1: Check curl installation

```bash
curl --version
```
Expected Output:
Information about the installed version of curl and supported protocols (e.g., HTTP, HTTPS).

🌐 Step 2: Fetch HTML content of a webpage
```bash
curl http://example.com
```
Expected Output:
HTML content of the example page.

📦 Step 3: Fetch posts from JSONPlaceholder API
```bash
curl https://jsonplaceholder.typicode.com/posts
```
Expected Output:
JSON array of posts. Example:
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit..."
  },
  ...
]
```

🧾 Step 4: Fetch only headers from API
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

Expected Output:

HTTP/2 200 
content-type: application/json; charset=utf-8
...


📤 Step 5: Send a POST request
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Expected Output:
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

🧠 Summary Table
| Command                                              | Description                       |
| ---------------------------------------------------- | --------------------------------- |
| `curl --version`                                     | Check curl version and protocols  |
| `curl http://example.com`                            | Fetch content of a basic web page |
| `curl https://jsonplaceholder.typicode.com/posts`    | Get JSON data from API            |
| `curl -I https://jsonplaceholder.typicode.com/posts` | Get response headers only         |
| `curl -X POST -d ...`                                | Make a POST request to an API     |


