# Documentation
This document outlines all information on the backend APIs built in Python's Flask framework for my personal website.

**URL**<br>
`https://api.zanaaziz.com`

**Format**<br>
`JSON`

---

**Name**<br>
`/login`

**Description**<br>
Signs a user into their account.

**Protocol**<br>
POST

**Parameters**
- username*
- password*

**Response**
- id
- access_token
- refresh_token

---

**Name**<br>
`/logout`

**Description**<br>
Signs a user out of their account.

**Protocol**<br>
POST

**Authorization**<br>
- access_token*

**Parameters**
- refresh_token*

**Response**
- message

---

**Name**<br>
`/refresh`

**Description**<br>
Refreshes a user's token.

**Protocol**<br>
POST

**Authorization**<br>
- refresh_token*

**Response**
- access_token

---

**Name**<br>
`/posts`

**Description**<br>
Fetches all posts available.

**Protocol**<br>
GET

**Response**<br>
- posts: [ ]
  - id
  - title
  - image_url
  - body
  - date_created
  - live

---

**Name**<br>
`/posts`

**Description**<br>
Creates a new post.

**Protocol**<br>
POST

**Authorization**<br>
- access_token*

**Parameters**
- title*
- image_url
- body*

**Response**
- message
- post: { }
  - id
  - title
  - image_url
  - body
  - date_created
  - live

---

**Name**<br>
`/posts/<id>`

**Description**<br>
Fetches a specific post by ID.

**Protocol**<br>
GET

**Parameters**
- id*

**Response**
- post: { }
  - id
  - title
  - image_url
  - body
  - date_created
  - live

---

**Name**<br>
`/posts/<id>`

**Description**<br>
Updates an existing post.

**Protocol**<br>
PUT

**Authorization**
- access_token*

**Parameters**
- title*
- image_url
- body*
- live

**Response**
- message
- post: { }
  - id
  - title
  - image_url
  - body
  - date_created
  - live

---

**Name**<br>
`/posts/<id>`

**Description**<br>
Deletes an existing post.

**Protocol**<br>
DELETE

**Authorization**
- access_token*

**Response**
- message
