# Documentation
This document outlines all information on the backend APIs built in Python's Flask framework for my personal website.

**URL**<br>
`https://api.zanaaziz.com`

**Format**<br>
`JSON`

**Authorization**<br>
`Bearer`

---

**Endpoint**<br>
`POST /login`

**Description**<br>
Signs a user into their account.

**Parameters**
- username*
- password*

**Response**
- id
- access_token
- refresh_token

---

**Endpoint**<br>
`POST /logout`

**Description**<br>
Signs a user out of their account.

**Headers**<br>
- access_token*

**Parameters**
- refresh_token*

**Response**
- message

---

**Endpoint**<br>
`POST /refresh`

**Description**<br>
Refreshes a user's token.

**Headers**<br>
- refresh_token*

**Response**
- access_token

---

**Endpoint**<br>
`GET /posts`

**Description**<br>
Fetches all posts available.

**Response**<br>
- posts: [ ]
  - id
  - title
  - image_url
  - body
  - date_created
  - live

---

**Endpoint**<br>
`POST /posts`

**Description**<br>
Creates a new post.

**Headers**<br>
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

**Endpoint**<br>
`GET /posts/:id`

**Description**<br>
Fetches a specific post by ID.

**Response**
- id
- title
- image_url
- body
- date_created
- live

---

**Endpoint**<br>
`PUT /posts/:id`

**Description**<br>
Updates an existing post.

**Headers**
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

**Endpoint**<br>
`DELETE /posts/:id`

**Description**<br>
Deletes an existing post.

**Headers**
- access_token*

**Response**
- message
