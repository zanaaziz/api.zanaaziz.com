# Documentation
This document outlines all information on how to use the API's for my personal website.

**URL**<br>
`https://api.zanadaniel.com/public/`

**Accepted data format**<br>
`JSON`

---

**Name**<br>
`login.php`

**Description**<br>
Signs a user into their account.

**Request**<br>
POST

**Parameters**<br>
- username*
- password*

**Response**<br>
- authentication
- message

---

**Name**<br>
`posts.php`

**Description**<br>
Fetches all posts available at this time.

**Request**<br>
GET

**Response**<br>
- message
- data
  - id
  - title
  - slug
  - image
  - body
  - date

---

**Name**<br>
`post.php`

**Description**<br>
Fetches a specific post by ID.

**Request**<br>
GET

**Parameters**<br>
- id*

**Response**<br>
- message
- data
  - id
  - title
  - slug
  - image
  - body
  - date

---

**Name**<br>
`create.php`

**Description**<br>
Creates a new post.

**Request**<br>
POST

**Parameters**<br>
- title*
- image
- body*

**Response**<br>
- message

---

**Name**<br>
`update.php`

**Description**<br>
Updates an existing post.

**Request**<br>
PUT

**Parameters**<br>
- id*
- title*
- image
- body*

**Response**<br>
- message

---

**Name**<br>
`delete.php`

**Description**<br>
Deletes an existing post.

**Request**<br>
DELETE

**Parameters**<br>
- id*

**Response**<br>
- message